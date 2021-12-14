from kafka_tools import KafkaWeather
from pandas import Timestamp
from apscheduler.schedulers.background import BackgroundScheduler
import time
from kafka import KafkaConsumer, TopicPartition
import json
import ast

weather_center_names = [
    'center1',
    'center2',
    'center3',
    'center4'
]


# class hn_wrapper(object):
#     def __init__(self, it):
#         self.it = iter(it)
#         self._hasnext = None

#     def __iter__(self): return self

#     def next(self):
#         if self._hasnext:
#             result = self._thenext
#         else:
#             result = next(self.it)
#         self._hasnext = None
#         return result

#     def hasnext(self):
#         if self._hasnext is None:
#             try:
#                 self._thenext = next(self.it)
#             except StopIteration:
#                 self._hasnext = False
#             else:
#                 self._hasnext = True
#         return self._hasnext


# listener = KafkaConsumer(bootstrap_servers='18.118.248.88:9092')
# topics = listener.topics()
# listener_list = []
# for topic in topics:
#     listener_list.append(topic)

# cons_lst = []
# for lnr in listener_list:
#     new_listener = KafkaConsumer(bootstrap_servers='18.118.248.88:9092')
#     tp = TopicPartition(lnr, 0)
#     new_listener.assign([tp])
#     cons_lst.append((new_listener, tp))


# for i in range(50):
#     for consumer in cons_lst:
#         consumer[0].poll()
#         end_offset = new_listener.end_offsets([consumer[1]])[consumer[1]]
#         consumer[0].seek(consumer[1], end_offset - 1)
#         # nxt = next(consumer[0]).value.decode('utf-8').replace("'", '"')
#         nxt = ast.literal_eval(next(consumer[0]).value.decode('utf-8'))

#         print(nxt['rh'])
#         # print(json.loads(nxt)['rh'])

#     print('sleeping')
#     time.sleep(10)

# print(next(new_listener))
# listener.subscribe(topics=[str(station)])

kafka = KafkaWeather(weather_center_names, '18.118.248.88:9092')
res = kafka.get_GeoJSON_data()
print(len(res['features']))
print(res['features'][0])
# print(res)

# print(kafka.get_interpolated_list())
