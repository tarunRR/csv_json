FROM python:3
LABEL Author="Tarun Kumar Singh"
LABEL E-mail="tarunchauhan138@gmail.com"
LABEL version="0.0.1"
WORKDIR /
COPY source/ source/
COPY config/ config/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5001
CMD [ "python" , "source/main.py"] 