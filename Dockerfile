FROM python:3.7.3 
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r ./requirements.txt

ADD templates /app/templates
COPY app.py /app
CMD ["python", "app.py"]~
