FROM selenium/standalone-chrome


ENV TZ=Europe/Berlin
WORKDIR /home/seluser

RUN sudo apt update && sudo apt upgrade -y

#python3 is already installed

RUN sudo apt install python3-pip -y


RUN sudo pip3 install selenium pyyaml


COPY selenium.py .

COPY pdftest.pdf .

COPY configfile.yaml .


#will be executed after the creation of the image
ENTRYPOINT [ "python3", "/home/seluser/selenium.py" ]  
