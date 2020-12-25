import requests
import MySQLdb
from datetime import datetime

url = 'https://data.epa.gov.tw/api/v1/aqx_p_314?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&format=json'
r = requests.get(url)
# print(r.status_code)
list_of_dicts = r.json()

conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="ph_rain")
c = conn.cursor()
# print(c)
conn.set_character_set('utf8')
# print(conn)
sql = "DELETE FROM hourly_data" #刪除舊資料
try:
    c.execute(sql)
    conn.commit()
except MySQLdb.Error as e:
    print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

for i in list_of_dicts["records"]:
    County = i['County']
    SiteId = i['SiteId']
    SiteName = i['SiteName']
    ItemId = i['ItemId']
    ItemName = i['ItemName']
    ItemEngName = i['ItemEngName']
    ItemUnit = i['ItemUnit']
    MonitorDate = i['MonitorDate']
    Concentration = i['Concentration']

    sql = "insert into hourly_data(County,SiteId,SiteName,ItemId,ItemEngName,ItemName,ItemUnit,MonitorDate,Concentration) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        c.execute(sql,(County,SiteId,SiteName,ItemId,ItemEngName,ItemName,ItemUnit,MonitorDate,Concentration) )
        conn.commit()
    except MySQLdb.Error as e:
        print("Mysql Error %d: %s" % (e.args[0], e.args[1]))