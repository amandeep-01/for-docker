FROM python:3.10.0-alpine3.15
WORKDIR /demo1
COPY required.txt required.txt
RUN pip install -r required.txt
COPY . /demo1
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]