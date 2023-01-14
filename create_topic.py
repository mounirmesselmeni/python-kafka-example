import sys
from confluent_kafka.admin import AdminClient, NewTopic

def create_topic(topic_name):
    conf = {'bootstrap.servers': 'localhost:9092'}
    admin_client = AdminClient(conf)
    new_topic = admin_client.create_topics([NewTopic(topic_name, num_partitions=1, replication_factor=1)])
    for topic, future in new_topic.items():
        try:
            future.result()
            print("Topic {} created successfully".format(topic))
        except Exception as e:
            print("Failed to create topic {}: {}".format(topic, e))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python {} <topic_name>".format(sys.argv[0]))
        sys.exit(1)
    topic_name = sys.argv[1]
    create_topic(topic_name)