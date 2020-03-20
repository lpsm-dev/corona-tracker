ARG PYTHON_VERSION=3.8-alpine3.11

FROM python:${PYTHON_VERSION} as base

FROM base as install-env

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

COPY [ "./requirements.txt", "." ]

RUN apk add --no-cache --virtual .build-deps \
        gcc=9.2.0-r3 \
        libc-dev=0.7.2-r0 \
        libffi-dev=3.2.1-r6 \
        openssl-dev=1.1.1d-r3 && \
    pip install --upgrade pip && \
    pip install --user --no-warn-script-location -r ./requirements.txt && \
    apk del .build-deps

FROM base

LABEL maintainer="Lucca Pessoa da Silva Matos - luccapsm@gmail.com" \
        org.label-schema.version="1.0.0" \
        org.label-schema.release-data="2020-03-18" \
        org.label-schema.url="https://github.com/lpmatos" \
        org.label-schema.alpine="https://alpinelinux.org/" \
        org.label-schema.python="https://www.python.org/" \
        org.label-schema.name="Corona API Tracker" 

ENV HOME=/usr/src/code \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONUTF8=1 \
    TZ=America/Sao_Paulo \
    LOG_PATH=/var/log/corona-api-tracker \
    LOG_FILE=file.log \
    LOG_LEVEL=DEBUG \
    LOGGER=Corona-API-Tracker-Logger \
    ENDPOINT_BING=https://www.bing.com/covid/data \
    ENDPOINT_REST_COUNTRIES=https://restcountries.eu/rest/v2/ \
    ENDPOINT_THE_TRACKER_VIRUS=https://thevirustracker.com/

RUN set -ex && \
    addgroup -g 1000 python && \
    adduser -u 999 -G python -h ${HOME} -s /bin/sh -D python && \
    mkdir -p ${HOME} && mkdir -p {LOG_PATH} && \
    chown -hR python:python ${HOME} && \
    touch {LOG_PATH}/{LOG_FILE}

RUN apk update && \
    apk add --update --no-cache 'su-exec>=0.2'

WORKDIR ${HOME}

COPY --chown=python:python --from=install-env [ "/root/.local", "/usr/local" ]

COPY --chown=python:python [ "./code", "." ]

COPY [ "./docker-entrypoint.sh", "/usr/local/bin/" ]

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;

ENTRYPOINT [ "docker-entrypoint.sh" ]

CMD [ "python", "./main.py" ]
