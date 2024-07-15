FROM node:16.1-alpine

#Set WORKDIR
WORKDIR /usr/src/app

# Copying Node Checking script

COPY app.py .

#Update and install unzip
RUN apk update && apk add unzip python3 curl

# Curl the repository

RUN curl -L https://github.com/docker-hy/material-applications/archive/refs/heads/main.zip -o frontend.zip && \
  unzip frontend.zip

# Set WORKDIR where the Frontend project has been uncompressed

WORKDIR /usr/src/app/material-applications-main/example-frontend/

RUN ls

#Expose port as specified in the project
EXPOSE 5000

# Add ENV

ENV REACT_APP_BACKEND_URL=http://localhost:8000/

# Run npm build

RUN npm install && npm run build

# Install Serve

RUN npm install -g serve

#Default to bash
CMD [ "serve", "-s", "-l", "5000", "build" ]

# Running node check script

#RUN python app.py
