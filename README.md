# pyAcurite

Forked from `https://github.com/therippa/pyAcurite` whom created the original Flask app for PyAcurite. This repository was created to add minor updates to the app and Dockerize it.

A simple service that takes the data from the Acurite SmartHub (to be discontinued Summer 2018 due to Acurite being a bad and stupid company), and sends it off to Weather Underground.

I started setting up weewx, but it seemed like a lot of overhead for a simple thing, so I made this.

This uses the "listen" method, so you must be able to configure your router to point the DNS entry of hubapi.myacurite.com to something listening on your local network (PC or raspberry pi).  Traffic that the SmartHub sends out will now be routed to that device.

This could also easily be used with the "sniffing" method - just forward the data to `http://<pyacurite-device>/weatherstation/updateweatherstation`

## Configuration

Find your STATION_ID and STATION_KEY.  These can be found on your Weather Underground station setting page.  Along with the FREQUENCY with which to send data to Weather Underground, these values will be set later as environment variables when we start PyAcurite.

## Usage

Clone this repository:

`git clone https://github.com/akennerly/pyAcurite.git`

### Docker method

`docker build -t pyacurite:latest .`

`docker run -p 80:5000 -e STATION_ID="KCASANFR9999" -e STATION_KEY="xxxxxx" -e FREQUENCY=30 --name PyAcurite pyacurite`

### Native python app

First, install the requirements:

`pip install -r requirements.txt`

Then, run the app on port 80 using something like this:

`sudo STATION_ID='KCASANFR9999' STATION_KEY='xxxxxxx' FREQUENCY=30 FLASK_APP=main.py flask run --host=0.0.0.0 --port=80`

or run it on its default port (5000) and set up a reverse proxy with nginx or apache.
