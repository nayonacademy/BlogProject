FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /BlogProject
WORKDIR /BlogProject
ADD requirements.txt /BlogProject/
RUN pip install -r requirements.txt
ADD . /BlogProject/