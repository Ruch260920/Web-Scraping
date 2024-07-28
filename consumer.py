import pulsar

client = pulsar.Client('pulsar://localhost:6650')

consumer = client.subscribe('my-topic', 'my-subscription')

msg = consumer.receive()

try:
    print("Received message: '%s'" % msg.data().decode('utf-8'))
    consumer.acknowledge(msg)
except:
    consumer.negative_acknowledge(msg)

client.close()
