FROM python:3.6-slim
#RUN apt-get install python-dev
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
