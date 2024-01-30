FROM debian

RUN apt update -y && apt install python3 python3-pip -y

COPY . /home/

WORKDIR /home

EXPOSE 6666

ENTRYPOINT ["python3", "main.py"]