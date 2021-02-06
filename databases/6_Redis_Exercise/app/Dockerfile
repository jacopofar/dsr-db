FROM python:3.9

# Python Requirements installation
ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . /app-code
WORKDIR /app-code

ENTRYPOINT ["python", "app.py"]
