FROM python:3.6

COPY . /src

COPY ./requirements.txt /src/requirements.txt

WORKDIR src

EXPOSE 3000:3000

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]