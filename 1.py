import datetime
from clickhouse_driver import Client
from datetime import datetime

c = Client(host='192.168.3.101')


def insert_data(client, insert_data, db_name="test", table_name="iot5"):
    columns = ', '.join(insert_data.keys())
    query = 'insert into {}.{} ({}) values'.format(db_name, table_name, columns)
    
    data = []
    data.append(insert_data)
    client.execute(query, data)
    print("done")

data={'name':"test",'counter':100,'open':datetime.now()}
insert_data(client=c,insert_data=data)
