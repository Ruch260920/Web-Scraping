import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('my-topic')

producer.send(('Hello Pulsar!').encode('utf-8'))

print('Message sent successfully')

client.close()
