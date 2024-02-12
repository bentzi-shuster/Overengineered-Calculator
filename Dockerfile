FROM python:slim-buster
RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install --upgrade setuptools &&\
    adduser myuser
WORKDIR /home/myuser
COPY --chown=myuser:myuser . .
ENTRYPOINT ["python3"]
FROM python:slim-buster
RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install --upgrade setuptools &&\
    adduser myuser
WORKDIR /home/myuser
COPY --chown=myuser:myuser . .
WORKDIR /home/myuser
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]

#for windows ( POWERSHELL )
# docker run -v ${pwd}:/home/myuser qrcode
# docker run -v ${pwd}:/home/myuser -e QR_CODE_IMAGE_DIRECTORY="TEST" qrcode [name of file.py]
# docker run -v ${pwd}:/home/myuser -e QR_CODE_IMAGE_DIRECTORY='"homework"' -e QR_CODE_DEFAULT_FILE_NAME="GmailQrCOde.png" -e QR_CODE_DEFAULT_URL="https://www.gmail.com" qrcode hello.py