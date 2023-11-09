FROM python:3.8-alpine
EXPOSE 5000
ENV PYTHONPATH=/${APP_FOLDER}
WORKDIR /${APP_FOLDER}
COPY requirements.txt .
USER root
RUN apk update \
  && apk add --no-cache \
    gcc \
    libffi-dev
RUN pip install -r requirements.txt
COPY ${FLASK_APP} /${APP_FOLDER}

ARG USER_UID=12345
ARG GROUP_GID=23456
RUN addgroup -g ${GROUP_GID} app
RUN adduser -u ${USER_UID} -D -G app flask
USER flask

CMD python ${FLASK_APP}


