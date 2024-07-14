FROM golang:1.23rc1-alpine3.20

# Set workdir

WORKDIR /usr/src/app

# Update & download curl

RUN apk update && apk add curl

# Download through curl repo

RUN curl -L https://github.com/docker-hy/material-applications/archive/refs/heads/main.zip -o backend.zip

# unzip backend

RUN unzip backend.zip

# Set workdir

WORKDIR /usr/src/app/material-applications-main/example-backend/

RUN ls

# build project

RUN go build

# Expose Port

EXPOSE 8000

#Set ENV Port

ENV PORT=8000
ENV REQUEST_ORIGIN=http://localhost:5000

# run server

CMD [ "./server"]
