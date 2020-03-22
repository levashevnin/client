import clickhouse_driver
from datetime import datetime

time = datetime.now().strftime('%S')
print(time)
client = clickhouse_driver.Client("127.0.0.1")

#client.execute("INSERT INTO Values VALUES ('Press', 15.3, 1, %(f)s);", {'f': time})

A = client.execute("SELECT name, value, alarm, time FROM Values WHERE time = 03 LIMIT 8;")
Press = str(A[0])
Press = Press[1:len(Press)-1]
Press = Press.split(', ')
H = str(A[1])
H = H[1:len(H)-1]
H = H.split(', ')
Base_hui = []
v = 0
print(A)
