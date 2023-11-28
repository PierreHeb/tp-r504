FROM python:3
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip install -r requirements.txt
COPY app1.py /
CMD ["flask","--app","app1","run","--host=0.0.0.0"]
