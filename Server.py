from opcua import Server
import time
import random

server = Server()

url = "opc.tcp://127.0.0.1:8080"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()


Param = node.add_object(addspace, "Parametrs")

Press = Param.add_variable(addspace, "Pressure", 0)
Hum = Param.add_variable(addspace, "Hudimitry", 0)
TempRoom = Param.add_variable(addspace, "TemperatureRoom", 0)
WSTemp = Param.add_variable(addspace, "WSTemperature", 0)
pH = Param.add_variable(addspace, "pH", 0)
Mass = Param.add_variable(addspace, "Mass", 0)
FF = Param.add_variable(addspace, "FF", 0)
CO2 = Param.add_variable(addspace, "CO2", 0)

Press.set_writable()
Hum.set_writable()
TempRoom.set_writable()
WSTemp.set_writable()
pH.set_writable()
Mass.set_writable()
FF.set_writable()
CO2.set_writable()

server.start()

while True:
    Press.set_value(random.uniform(30, 150))
    Hum.set_value(random.uniform(0, 120))
    TempRoom.set_value(random.uniform(10, 30))
    WSTemp.set_value(random.uniform(50, 100))
    pH.set_value(random.uniform(750, 780))
    Mass.set_value(random.uniform(30, 50))
    FF.set_value(random.uniform(5, 10))
    CO2.set_value(random.uniform(30, 50))

    time.sleep(1)