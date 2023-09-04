# create python image and install java and configure java_home path

FROM python:3.11

RUN apt-get update --fix-missing

RUN apt-get install default-jdk -y
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin
RUN java -version

# install odbc driver for debian 12
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc
RUN curl https://packages.microsoft.com/config/debian/11/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN apt-get install -y unixodbc-dev


WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./app .

CMD ["uvicorn", "main:app",  "--host", "0.0.0.0", "--port", "80", "--reload"]
