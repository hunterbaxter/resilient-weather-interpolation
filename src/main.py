import argparse
from retriever.retriever import retrieve_cycle
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep
import logging

# FIXME: required should be true in production
parser = argparse.ArgumentParser(
    description='Set the kafka broker ip & the database ip.')
parser.add_argument('--kafka_ip', default=None, type=str, required=False)
parser.add_argument('--lat', default=None, type=str, required=False)
parser.add_argument('--lon', default=None, type=str, required=False)
args = parser.parse_args()

# TODO: Store secrets for production key (this is a test key)
key = "0e8aeccfa150491880a30ffb53a3e4ba"

logging.basicConfig(filename='retriever.log',
                    format='%(asctime)s %(message)s',
                    encoding='utf-8',
                    level=logging.DEBUG)

scheduler = BackgroundScheduler()
scheduler.add_job(retrieve_cycle,
                  'interval',
                  minutes=15,
                  args=(args.kafka_ip, args.lat, args.lon, key))
scheduler.start()
while True:
    # FIXME: find out the highest performant way of doing this.
    sleep(2)
