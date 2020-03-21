FROM python:3.7.7-stretch as base

FROM base as install-env

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

COPY [ "./requirements.txt", "." ]

RUN pip install --upgrade pip && \
    pip install --user --no-warn-script-location -r ./requirements.txt

FROM base

LABEL maintainer="Lucca Pessoa da Silva Matos - luccapsm@gmail.com" \
        org.label-schema.version="1.0.0" \
        org.label-schema.release-data="2020-03-18" \
        org.label-schema.url="https://github.com/lpmatos" \
        org.label-schema.alpine="https://alpinelinux.org/" \
        org.label-schema.python="https://www.python.org/" \
        org.label-schema.name="Corona Tracker" 

ENV HOME=/usr/src/code \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONUTF8=1 \
    TZ=America/Sao_Paulo \
    LOG_PATH=/var/log/coronatracker \
    LOG_FILE=file.log \
    LOG_LEVEL=DEBUG \
    LOGGER=Corona-API-Tracker-Logger \
    ENDPOINT_BING=https://www.bing.com/covid/data \
    ENDPOINT_REST_COUNTRIES=https://restcountries.eu/rest/v2/ \
    ENDPOINT_THE_TRACKER_VIRUS=https://thevirustracker.com/ \
    TELEGRAM_TOKEN=

RUN mkdir -p ${HOME} && mkdir -p {LOG_PATH} && \
    touch {LOG_PATH}/{LOG_FILE} && \
    rm -rf /var/lib/apt/lists/*

WORKDIR ${HOME}

USER root

COPY --from=install-env [ "/root/.local", "/usr/local" ]

COPY [ "./code", "." ]

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;

ENTRYPOINT []

CMD [ "python", "./main.py" ]
