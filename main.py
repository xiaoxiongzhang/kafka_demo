
from kafka import KafkaConsumer, TopicPartition
from kafka.errors import kafka_errors
import traceback


topic = "test"
consumer = KafkaConsumer(
    topic,
    bootstrap_servers='127.0.0.1:9092',
    auto_offset_reset="earliest",
    group_id="test"
)

try:
    partitions = [TopicPartition(topic, p) for p in consumer.partitions_for_topic(topic)]

    print("start to cal offset:")

    # total
    toff = consumer.end_offsets(partitions)
    toff = [(key.partition, toff[key]) for key in toff.keys()]
    toff.sort()
    print("total offset: {}".format(str(toff)))

    # current
    coff = [(x.partition, consumer.committed(x)) for x in partitions]
    coff.sort()
    print("current offset: {}".format(str(coff)))

    # cal sum and left
    toff_sum = sum([x[1] for x in toff])
    cur_sum = sum([x[1] for x in coff if x[1] is not None])
    left_sum = toff_sum - cur_sum
    print("kafka left: {}".format(left_sum))
    for message in consumer:
        print(message)
except kafka_errors:  # 抛出kafka_errors
    traceback.format_exc()


if __name__ == '__main__':
    name = 'phil'
    n, a, m, e = list(name)

    x = ['p', 'h', 'i', 'l']
    y = ''.join(['p', 'h', 'i', 'l'])
    z = 'p' + 'h' + 'i' + 'l'
    # print(n, a, m, e, list(name), x, y, z)
    # print('x is list(name):', x is list(name))
    # print('name is y:', name is y)
    # print('name is z:', name is z)
