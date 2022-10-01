FROM alpine:3.14

ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

WORKDIR /usr/src/app

COPY API_User_Moudle.py /usr/src/app/
COPY Asset_Picker_Logic_Moudle.py /usr/src/app/
COPY Data_Collecter_Moudle.py /usr/src/app/
COPY File_Manager_Moudle.py /usr/src/app/
COPY Handler_Moudle.py /usr/src/app/
RUN  chmod +x Handler_Moudle.py
COPY Time_Counter_Moudle.py /usr/src/app/

RUN pip3 install pandas 
RUN pip3 install numpy 
RUN pip3 install csv
RUN pip3 install tradingview_ta
RUN pip3 install datetime

RUN mkdir Data

CMD [“python3”, “./Handler_Moudle.py]