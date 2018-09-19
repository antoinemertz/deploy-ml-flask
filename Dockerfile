# Python base image
FROM python:3.6.3

# Where the API server lives
WORKDIR /app/

# Install required dependencies
COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

# API server
COPY server.py /app/
COPY models/svm.pckl /app/models/
# Container port on which the server will be listening
EXPOSE 5000
# Launch server app
ENTRYPOINT python ./server.py
