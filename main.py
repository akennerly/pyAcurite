import requests
import pprint
import json
import threading
import time
import datetime
import sys
import os
from flask import request
from flask import Flask

app = Flask(__name__)

station_data = {
    'ID': os.environ['STATION_ID'],
    'PASSWORD': os.environ['STATION_KEY'],
    'realtime': '1',
    'rtfreq': int(os.environ['FREQUENCY']),
    'softwaretype': 'PyAcurite'
}
raw_station_data = {}
pp = pprint.PrettyPrinter(indent=4)


def log_it(title, message, err=False):
    pretty_date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    sys.stdout.write('[%s] %s: %s\n' % (pretty_date, title, message))
    sys.stdout.flush()
    if err:
        sys.stderr.write('[%s] %s: %s\n' % (pretty_date, title, message))
        sys.stderr.flush()


def send_it():
    threading.Timer(station_data['rtfreq'], send_it).start()
    if 'tempf' in station_data:
        pretty_data = json.dumps(station_data)
        pretty_data = pretty_data.replace(station_data['PASSWORD'], '*****')
        log_it('Sending data', pretty_data)
        r = requests.get(url='https://rtupdate.wunderground.com/weatherstation/updateweatherstation.php', params=station_data)
        if 'success' not in r.text:
            log_it('ERROR SENDING DATA', r.text, True)

@app.route('/weatherstation/updateweatherstation')
def capture_it():
    if (request.args['mt'].startswith('5N1x')):
        global station_data
        global raw_station_data
        new_station_data = request.args.copy()
        raw_station_data = request.args.copy()
        new_station_data.pop('id', None)
        station_data.update(new_station_data)

    return ('', 204)

send_it()

if __name__ == "__main__":
            app.run(host ='0.0.0.0', port = 5001)
