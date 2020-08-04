import pandas as pd
import pymysql
import datetime

db = pymysql.connect(host='localhost', port=3306, user='ssafy', passwd='mandarindev', db='ssafy', charset='utf8')
file = pd.read_csv('medical.csv', encoding='CP949')
filtered_file = file[file['주소 '].str.contains("광주광역시")]
cursor = db.cursor()

for idx, row in filtered_file.iterrows():
    seq = row['연번']
    do = row['시도']
    city = row['시군구']
    address = row['주소 ']
    med_name = row['의료기관명 ']
    phone = row['대표 전화번호']
    user_id = 'compurain'
    date = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    print(seq, do, city, med_name, address, phone, user_id, date)
    sql = f"INSERT INTO medical (seq, do, city, med_name, address,phone, user_id, date) values ({str(seq)},'{do}','{city}','{med_name}','{address}','{phone}','{user_id}','{date}')"
    print(sql)
    cursor.execute(sql)

    db.commit()
db.close()
