import sys
from confluent_kafka import Consumer, KafkaError

def consume_message(topic_name):
    conf = {'bootstrap.servers': 'localhost:9092',
            'group.id': 'mygroup',
            'auto.offset.reset': 'earliest',
            }
    consumer = Consumer(conf)
    consumer.subscribe([topic_name])
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print('Reached end of topic {} [{}] at offset {}'.format(msg.topic(), msg.partition(), msg.offset()))
                else:
                    print('Error occured: {}'.format(msg.error()))
            else:
                print('Received message: {}'.format(msg.value()))
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        consumer.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python {} <topic_name>".format(sys.argv[0]))
        sys.exit(1)
    topic_name = sys.argv[1]
    consume_message(topic_name)