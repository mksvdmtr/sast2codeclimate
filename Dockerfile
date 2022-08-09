FROM python:3.10

WORKDIR /app

COPY sast2codeclimate.py .

CMD [ "python", "sast2codeclimate.py" ]

