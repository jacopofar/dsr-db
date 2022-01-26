FROM python:3.9

COPY . /myapp

RUN pip install -r /myapp/requirements.txt

ENV FLASK_APP=myapp:app
WORKDIR /myapp
CMD ["flask","run", "--host", "0.0.0.0"]
EXPOSE 5000
