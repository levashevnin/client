from opcua import Server
import time
from random import randint
server = Server()

url = "opc.tcp://127.0.0.1:8080"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parametrs")

Temp = Param.add_variable(addspace, "Temperature", 0)

Temp.set_writable()

server.start()
print(url)
  while True:
Temperature = randint(10,50)
print(Temperature)
Temp.set_value(Temperature)

time.sleep(2)
