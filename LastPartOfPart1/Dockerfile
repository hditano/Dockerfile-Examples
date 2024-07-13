FROM amazoncorretto:8

#Set workdirectory to copy .sh file
WORKDIR /usr/src/app

COPY script.sh .

#Grant permissions to script.sh, update and download unzip

RUN chmod +x script.sh && \
  yum update && yum install -y unzip

#Download Spring Project

RUN curl -L https://github.com/docker-hy/material-applications/archive/refs/heads/main.zip -o spring-example-project.zip

#Unzip Spring Project

RUN unzip spring-example-project

#Set Workdir for where spring project got uncompressed

WORKDIR /usr/src/app/material-applications-main/spring-example-project/

# Expose Port 8080 as indicated on the README file

EXPOSE 8080

#Unpackage project with Maven and Start it

RUN ./mvnw package && java -jar ./target/docker-example-1.1.3.jar

# Run Script created by me

RUN ./script.sh

