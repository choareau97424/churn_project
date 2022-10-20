FROM ubuntu
WORKDIR /src
RUN apt-get update 
RUN apt-get install -y python3 
RUN apt-get install -y python3-requests-file
COPY /src .
VOLUME /src
CMD ["/src/modelAPI.py"]
EXPOSE 8080
ENTRYPOINT ["python3"]
ADD requirements.txt .
RUN pip install -r requirements.txt