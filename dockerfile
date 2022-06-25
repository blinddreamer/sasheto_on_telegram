FROM python:3.8-slim-buster
WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY sasheto_on_telegram.py /python-docker
COPY sasheto_on_epic.py /python-docker
CMD [ "python3", "./sasheto_on_telegram.py"]