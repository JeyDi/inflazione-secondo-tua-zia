import os
import requests

import pandas as pd
from bs4 import BeautifulSoup
from stqdm import stqdm


from app.src.lib.config import settings


def get_base_data(website_url: str = settings.DATA_URL):

    form_options = {}
    for input_name in ["f[PROVINCIA]", "f[TIPO_RECORD_MISE]", "ANNO", "MESE"]:

        specific_path: str = "ANNO=2021&MESE=7&f%5BPROVINCIA%5D=Roma&f%5BTIPO_RECORD_MISE%5D=altri_alim&submit=Applica"
        response = requests.get(website_url + specific_path)

        soup = BeautifulSoup(response.text, features="lxml")
        select = soup.find(attrs={"name": input_name})

        options = []
        for option in select.find_all("option"):
            options.append(option["value"].replace(" ", "%20"))
        form_options[input_name] = options

    return form_options


def download_data(website_url: str = settings.DATA_URL, form_options: dict = {}):
    """
    Download the data from the website

    Args:
        website_url (str, optional): The website base url. Defaults to settings.DATA_URL.
        form_options (dict, optional): The data object used to filter the web table. Defaults to {}.

    Returns:
        pd.DataFrame: The dataframe with the data.
    """
    all_tables = []
    # form_options["MESE"] = [9]  # less data! TODO: all
    form_options = get_base_data(website_url)

    for anno in stqdm(form_options["ANNO"], desc="Sto scaricando i dati..."):
        for mese in form_options["MESE"]:
            for provincia in form_options["f[PROVINCIA]"]:
                for tipologia in form_options["f[TIPO_RECORD_MISE]"]:

                    url = (
                        website_url
                        + f"ANNO={anno}&MESE={mese}&f%5BPROVINCIA%5D={provincia}&f%5BTIPO_RECORD_MISE%5D={tipologia}&submit=Applica"
                    )

                    # download the data
                    table = pd.read_html(url)[0]
                    table.sort_values("Descrizione Prodotto").reset_index(drop=True)

                    # Add metadata
                    table["anno"] = anno
                    table["mese"] = mese
                    table["provincia"] = provincia.replace("%20", " ")
                    table["tipologia"] = tipologia

                    all_tables.append(table)

    prezzi = pd.concat(all_tables)

    # download to csv
    prezzi.to_csv(os.path.join(settings.DATA_PATH, "prezzi.csv"), index=False)

    return prezzi
