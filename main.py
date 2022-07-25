import time

from kafka import KafkaConsumer, TopicPartition
import traceback


class KafkaHandler:

    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers

    def consumer(self, topic, auto_offset_reset="earliest", group_id=None):
        params = dict(
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset=auto_offset_reset,
            group_id=group_id
        )
        params = {
            k: params[k]
            for k in filter(lambda x: params[x], params)
        }
        print(params)

        consumer = KafkaConsumer(
            topic,
            **params
        )
        return consumer

    def consume(self, topic, auto_offset_reset="earliest", group_id=None):
        consumer = self.consumer(topic, auto_offset_reset, group_id)
        try:
            for message in consumer:
                print(message)
                # TODO need to do

        except:
            traceback.format_exc()

    def dumps(self, file, topic, auto_offset_reset="earliest", group_id=None, encoding="utf-8"):
        consumer = self.consumer(topic, auto_offset_reset, group_id)

        # 获取最新的offset
        partitions = [TopicPartition(topic, p) for p in consumer.partitions_for_topic(topic)]
        toff = consumer.end_offsets(partitions)
        last_offset_list = list(toff.values())
        last_offset_list.sort(reverse=True)
        current_offset = int(last_offset_list[0]) - 1
        print(current_offset)

        try:
            with open(file, "w", encoding=encoding) as f:
                for message in consumer:
                    print("offset:", message.offset)
                    if int(message.offset) >= current_offset or message.timestamp >= int(time.time() * 1000):
                        print("over!-----------------")
                        break
                    f.write(message.value.decode(encoding) + "\n")
        except:
            print(traceback.format_exc())


if __name__ == '__main__':
    topic = "test"

    k = KafkaHandler(bootstrap_servers='127.0.0.1:9092')
    # k.consume(topic)
    k.dumps("./test.txt", topic)
