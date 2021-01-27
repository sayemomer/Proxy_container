FROM continuumio/anaconda3:4.4.0
COPY . /usr/local/taskC/
EXPOSE 5000
WORKDIR /usr/local/taskC/
RUN pip install -r requirements.txt
CMD python main.py