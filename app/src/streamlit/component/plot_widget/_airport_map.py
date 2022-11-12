from typing import List
import folium
from streamlit_folium import st_folium


def airport_map(selected_df):
    coordinate_pair: List[float] = list(selected_df[["lat", "lon"]].iloc[0, :])
    m = folium.Map(location=coordinate_pair, zoom_start=5)

    for _index, landmark in selected_df[["lat", "lon", "faa", "name"]].iterrows():
        tooltip = landmark["name"]
        folium.Marker(
            [landmark["lat"], landmark["lon"]],
            popup=landmark["name"],
            tooltip=tooltip,
        ).add_to(m)

    map_data = st_folium(m, key="fig1", width=1000, height=300)
    return map_data
