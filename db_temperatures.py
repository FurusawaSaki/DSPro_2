from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=1&view=a2'

r = requests.get(url)
r.raise_for_status()  # エラーの場合は例外を発生させる

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(r.text, 'html.parser')
print(type(soup))

# 最高気温のデータを含むテーブル行を探す
# 最高気温は通常、表の第8列に位置する
rows = soup.find_all('tr', class_='mtx')

# 13日から31日の最高気温を抽出
max_temperatures = []
for row in rows[16:35]:  # 12月13日から31日までの行を選択
    cells = row.find_all('td')
    if len(cells) > 11:  # 最高気温のセルが存在するか確認
        max_temp = cells[11].get_text().strip()
        if max_temp and max_temp != '-':  # 空またはハイフンでない場合のみ追加
            max_temperatures.append(max_temp)

# 最高気温の値を表示
for temp in max_temperatures:
      time.sleep(1)
    #   print(temp)



      
import sqlite3
# DBファイルを保存するためのファイルパス

# Google Colab
# path = '/content/'

# ローカル（自分のMac）
path = '/Users/furusawasaki/DSPro2/db_temperatures.py'

# DBファイル名
db_name = 'temp.sqlite'

# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect(path + db_name)

# DBへの接続を閉じる
con.close()


step_data = pd.read_csv('/Users/furusawasaki/DSPro2/step.csv')

# 1．DBに接続する
con = sqlite3.connect(path + db_name)

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．実行したいSQLを用意する
# テーブルを作成するSQL
sql_create_table_temperature = 'CREATE TABLE temp(date int, temperature int, step int);'

# 4．SQLを実行する
cur.execute(sql_create_table_temperature)

# 5．必要があればコミットする（データ変更等があった場合）
# 今回はテーブル作成なのでコミットが必要
con.commit()

# 6．DBへの接続を閉じる
con.close()


# # データベースに接続
# con = sqlite3.connect(path + db_name)
# cur = con.cursor()

# for i, row in step_data.iterrows():
#     date = row['date']  # CSVから日付を取得
#     step = row['step']  # CSVから歩数を取得
#     temperature_data = temp[i] if i < len(temp) else None  # 温度データを取得（リストの長さを超えないように）

#     # データを挿入
#     cur.execute('INSERT INTO temperature (date, temperature, step) VALUES (?, ?, ?)',
#                 (date, temperature_data, step))
    
# # コミットしてデータベースをクローズ
# con.commit()
# con.close()



