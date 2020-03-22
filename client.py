import opcua
import cryptography
import time
import clickhouse_driver
from datetime import datetime

url = "opc.tcp://127.0.0.1:8080"

client = opcua.Client(url)

clientDB = clickhouse_driver.Client("127.0.0.1")

client.connect()

#clientDB.execute("CREATE DATABASE test")
#clientDB.execute("CREATE TABLE Values(name String,value Float64, alarm UInt8, time UInt16) ENGINE = MergeTree() PRIMARY KEY time ORDER BY time;")

while True:
    times = datetime.now().strftime('%S')
    Press = client.get_node("ns=2;i = 2").get_value()
    if Press < 40 or Press > 140:
        alarm = 1
    else:
        alarm = 0
    clientDB.execute("INSERT INTO Values VALUES ('Press', %(value)s, %(alarm)s, %(date)s);",
    {'value': Press, 'alarm': alarm, 'date': times})
    Hum = client.get_node("ns=2;i = 3").get_value()
    if Hum < 20 or Hum > 100:
        alarm = 1
    else:
        alarm = 0
    clientDB.execute("INSERT INTO Values VALUES ('Hum', %(value)s, %(alarm)s, %(date)s);",
    {'value': Hum, 'alarm': alarm, 'date': times})
    TempRoom = client.get_node("ns=2;i = 4").get_value()
    if TempRoom < 18 or TempRoom > 25:
        alarm = 1
    else:
        alarm = 0
    clientDB.execute("INSERT INTO Values VALUES ('TempRoom', %(value)s, %(alarm)s, %(date)s);",
    {'value': TempRoom, 'alarm': alarm, 'date': times})
    WSTemp = client.get_node("ns=2;i = 5").get_value()
    if WSTemp < 60 or WSTemp > 80:
        alarm = 1
    else:
        alarm = 0
    clientDB.execute("INSERT INTO Values VALUES ('WSTemp', %(value)s, %(alarm)s, %(date)s);",
    {'value': WSTemp, 'alarm': alarm, 'date': times})
    pH = client.get_node("ns=2;i = 6").get_value()
    if pH < 760 or pH > 770:
        alarm = 1
    else:
        alarm = 0
    clientDB.execute("INSERT INTO Values VALUES ('pH', %(value)s, %(alarm)s, %(date)s);",
    {'value': pH, 'alarm': alarm, 'date': times})
    Mass = client.get_node("ns=2;i = 7").get_value()
    if Mass < 35 or Mass > 45:
        alarm = 1
    else:
        alarm = 0
    clientDB.execute("INSERT INTO Values VALUES ('Mass', %(value)s, %(alarm)s, %(date)s);",
    {'value': Mass, 'alarm': alarm, 'date': times})
    FF = client.get_node("ns=2;i = 8").get_value()
    if FF < 6 or FF > 8:
        alarm = 1
    else:
        alarm = 0
    clientDB.execute("INSERT INTO Values VALUES ('FF', %(value)s, %(alarm)s, %(date)s);",
    {'value': FF, 'alarm': alarm, 'date': times})
    CO2 = client.get_node("ns=2;i = 9").get_value()
    if CO2 < 40 or CO2 > 45:
        alarm = 1
    else:
        alarm = 0
    clientDB.execute("INSERT INTO Values VALUES ('CO2', %(value)s, %(alarm)s, %(date)s);",
    {'value': CO2, 'alarm': alarm, 'date': times})

    time.sleep(1)