import argparse
from retriever import retrieve_cycle
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep
import logging

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--kafka_ip', default=None, type=str, required=True)
parser.add_argument("-a", '--authentication',
                    default=None, type=str,
                    required=True)
parser.add_argument("-i", '--interval', default=15,
                    type=float, required=False)
args = parser.parse_args()

# default="0e8aeccfa150491880a30ffb53a3e4ba",

# TODO: Store secrets for production key (this is a test key)

logging.basicConfig(filename='retriever.log',
                    format='%(asctime)s %(message)s',
                    level=logging.DEBUG)
                    # encoding='utf-8',

scheduler = BackgroundScheduler()
scheduler.add_job(retrieve_cycle,
                  'interval',
                  minutes=args.interval,
                  args=(args.kafka_ip, args.authentication))
scheduler.start()
while True:
    # FIXME: find out the highest performant way of doing this.
    sleep(2)
