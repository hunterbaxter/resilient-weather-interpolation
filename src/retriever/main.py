import argparse
from retriver import retrieve_and_send_current

parser = argparse.ArgumentParser(
    description='Set the kafka broker ip & the database ip.')
parser.add_argument('--kafka_ip', default=None, type=str, required=True)
parser.add_argument('--lat', default=None, type=str, required=True)
parser.add_argument('--lon', default=None, type=str, required=True)
args = parser.parse_args()

key = "0e8aeccfa150491880a30ffb53a3e4ba"

retrieve_and_send_current(ip=args.kafka_ip,
                          lat=args.lat,
                          lon=args.lon,
                          key=key)
