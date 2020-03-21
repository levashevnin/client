from opcua import Client
import time
print(12312321)

url = "opc.tcp://127.0.0.1:8080"
print(12312321)
client = Client(url)

client.connect()
print("client connect")

  while True: 
Temp = client.get_node("ns=2;i = 2").get_value()
print(Temp)
time.sleep(1)
