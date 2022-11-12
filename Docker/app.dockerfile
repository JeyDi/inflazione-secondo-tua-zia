FROM python:3.9-buster

# Metadata
LABEL name="InflaziaDashboard"
LABEL maintainer="Pollo Watzlawick"
LABEL version="0.1"

ARG YOUR_ENV="virtualenv"
ARG POETRY_VERSION="1.1.15"

ENV YOUR_ENV=${YOUR_ENV} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=${POETRY_VERSION} \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

ENV PATH="$POETRY_HOME/bin:$PATH"

# Install libraries
RUN DEBIAN_FRONTEND=noninteractive apt update && apt install -y \
    libpq-dev gcc wget gnupg2 curl openssh-client git make build-essential \
    make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

RUN  wget -O install-poetry.py https://install.python-poetry.org/ \
    && python install-poetry.py --version ${POETRY_VERSION}

WORKDIR /streamlit

#Copy all the project files
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY /app ./app
COPY script/launch.sh .

# Copy the .streamlit configurations inside the default
COPY .streamlit/config.prod.toml /root/.streamlit/config.toml

#Launch the main (if required)
RUN chmod +x launch.sh
CMD ["bash", "launch.sh"]