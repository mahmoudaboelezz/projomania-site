FROM python:3.8-slim-buster
WORKDIR /projomania_website-main
COPY req.txt req.txt
RUN pip3 install -r req.txt
COPY . .
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]