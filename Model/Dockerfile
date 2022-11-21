FROM ubuntu
WORKDIR /src
RUN apt-get update 
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-requests-file
COPY /src .
RUN pip3 install -r requirements.txt
VOLUME /src
CMD ["/src/modelAPI.py"]
EXPOSE 8000
CMD ["uvicorn", "modelAPI:api", "--host", "0.0.0.0", "--port", "8000"]