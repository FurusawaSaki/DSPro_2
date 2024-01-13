from bs4 import BeautifulSoup
import requests
import time

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
      print(temp)
