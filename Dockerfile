ARG PYTHON_VERSION=3.7.7-stretch

FROM python:${PYTHON_VERSION} as base

FROM base as install-env

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

COPY [ "./requirements.txt", "." ]

RUN pip install --upgrade pip && \
    pip install --user --no-warn-script-location -r ./requirements.txt

FROM base

LABEL maintainer="Lucca Pessoa da Silva Matos - luccapsm@gmail.com" \
        org.label-schema.version="2.0.0" \
        org.label-schema.release-data="2020-03-23" \
        org.label-schema.url="https://github.com/lpmatos" \
        org.label-schema.alpine="https://alpinelinux.org/" \
        org.label-schema.python="https://www.python.org/" \
        org.label-schema.name="Corona Tracker" 

ENV HOME=/usr/src/code

RUN mkdir -p ${HOME} && mkdir -p {LOG_PATH} && \
    touch {LOG_PATH}/{LOG_FILE} && \
    rm -rf /var/lib/apt/lists/*

WORKDIR ${HOME}

COPY --from=install-env [ "/root/.local", "/usr/local" ]

COPY [ "./code", "." ]

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;

ENTRYPOINT []

CMD [ "python", "./main.py" ]
