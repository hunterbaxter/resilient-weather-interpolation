import argparse
from retriever import retrieve_cycle
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

# FIXME: this didn't work: encoding='utf-8',
logging.basicConfig(filename='retriever.log',
                    format='%(asctime)s %(message)s',
                    level=logging.DEBUG)

while True:
    retrieve_cycle(args.kafka_ip, args.authentication)
    sleep(60 * args.interval)
