import pandas as pd
import pymysql
import datetime

db = pymysql.connect(host='localhost', port=3306, user='ssafy', passwd='mandarindev', db='ssafy', charset='utf8')
file = pd.read_csv('doro.txt', delimiter='|', encoding='CP949',
                   names=['도로명코드', '도로명', '도로명로마자', '읍면동일련번호', '시도명', '시도 로마자', '시군구명', '시군구 로마자', '읍면동명',
                          '읍면동로마자',
                          '읍면동구분', '읍면동코드', '사용여부', '변경사유', '변경이력정보', '고시일자', '말소일자'])

mask1 = (file.get('시도명') == '광주광역시')
filtered_file = file[['도로명코드', '도로명', '읍면동일련번호', '시도명']].loc[mask1, :]
# filtered_file.to_csv('doro_csv_gwangju.csv', encoding='utf-8')

cursor = db.cursor()

for idx, row in filtered_file.iterrows():
    code = row['도로명코드']
    name = row['도로명']
    serial_nubmer = row['읍면동일련번호']
    city_name = row['시도명']
    user_id = 'compurain'
    date = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    print(code, name, serial_nubmer, city_name)
    sql = f"INSERT INTO addr (code,name,serial_number,city_name,user_id,date) values ({str(code)},'{name}','{serial_nubmer}','{city_name}','{user_id}','{date}')"
    print(sql)
    cursor.execute(sql)

    db.commit()
db.close()