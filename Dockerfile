FROM python:3.7-alpine

EXPOSE 5000

ENTRYPOINT ["gunicorn"]

CMD ["--workers=4", "--bind=0.0.0.0:5000", "app:my_app"]

RUN mkdir /flask_api && \
    apk upgrade --update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev && \
    pip install pipenv

COPY . /flask_api
WORKDIR /flask_api

RUN pipenv install --system --deploy
