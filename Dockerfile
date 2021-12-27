FROM python:3.7-stretch
COPY . /usr/local/
EXPOSE 5000
WORKDIR /usr/local/
RUN pip install -r requirements.txt
CMD python main.py  