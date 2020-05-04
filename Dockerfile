FROM python:3.8-slim

ADD ./ ./

RUN pip3 install -r requirements.txt

RUN python3 -m nltk.downloader punkt

CMD ["python3","-u", "api.py"]