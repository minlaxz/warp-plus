FROM python:3.10.0-alpine as base

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip setuptools wheel
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

FROM python:3.10.0-alpine

RUN mkdir -p /home/app
ENV APP_HOME=/home/app/warpapp
WORKDIR ${APP_HOME}

RUN addgroup -S app && adduser -S app -G app

RUN pip install -U pip setuptools wheel
COPY --from=base /usr/src/app/wheels /wheels
COPY --from=base /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*
RUN rm -rf /wheels

COPY . .
RUN chown -R app:app $APP_HOME
USER app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]