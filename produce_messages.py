import sys
from confluent_kafka import Producer

def produce_message(topic_name):
    conf = {'bootstrap.servers': 'localhost:9092'}
    producer = Producer(conf)

    def delivery_callback(err, msg):
        if err:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    for i in range(10):
        message = 'This is message number {}'.format(i)
        producer.produce(topic_name, value=message.encode('utf-8'), callback=delivery_callback)
        producer.flush()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python {} <topic_name>".format(sys.argv[0]))
        sys.exit(1)
    topic_name = sys.argv[1]
    produce_message(topic_name)