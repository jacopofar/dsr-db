FROM python:3.9
COPY myapp /opt/myapp
COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt
ENV FLASK_APP=myapp:app
WORKDIR /opt
EXPOSE 5000
CMD ["flask", "run",  "--host", "0.0.0.0"]
# even better:
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "myapp:app"]