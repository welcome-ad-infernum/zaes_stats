FROM python:3

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

ADD run.py /usr/src/app/run.py

CMD ["python", "/usr/src/app/run.py"]
EXPOSE 8000