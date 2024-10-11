FROM python:3.12

COPY . /app

#
WORKDIR /app

RUN python3 -m pip install -r requirements.txt

# this applies the flag -p 5000:5000 by default
EXPOSE 5000

CMD ["flask", "--app", "with_numpy", "run", "--host", "0.0.0.0"]
