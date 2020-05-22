#!/usr/bin/python3

import sqlite3
import yaml
import json
import time
import sys
import signal

def fetchData():
    print()

def handler(sig, frame):
    print('已停止')
    conn.close()
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

with open("config.yml", 'r') as stream:
    try:
        _config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print("讀取設定檔失敗！")
        print(exc)
        sys.exit(255)

print("正在檢查設定檔格式")

if(_config["token"] == None):
    print("設定錯誤：未填入 token")
    sys.exit(201)
if(not isinstance(_config["report"]["period"], int) or _config["report"]["period"] < 30):
    print("設定錯誤： report.period 必須是正整數，且不能小於 30")
    sys.exit(202)
if(not isinstance(_config["report"]["all"], bool)):
    print("設定錯誤： report.all 必須是 true 或 false")
    sys.exit(203)
if(not isinstance(_config["report"]["battleCount"], bool)):
    print("設定錯誤： report.battleCount 必須是 true 或 false")
    sys.exit(204)
if(not isinstance(_config["report"]["warningLevel"], int) or _config["report"]["warningLevel"] < 1 or _config["report"]["warningLevel"] > 3):
    print("設定錯誤： report.warningLevel 必須是 1, 2, 3 其一")
    sys.exit(205)

conn = sqlite3.connect('reports.sqlite3')
print("成功連接資料庫")

c = conn.cursor()

c.execute(
    ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='reports' '''
)
if c.fetchone()[0] == 1:
    print('資料表已存在，開始記錄')
else:
    print('資料表不存在，先建表')

conn.commit()
conn.close()

while True:
    print("loop")
    time.sleep(1)



