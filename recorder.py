#!/usr/bin/python3

import sqlite3
import yaml
import json
import time
import sys
import signal
import requests
from urllib import parse


def fetchData():
    c.execute("SELECT * FROM reports ORDER BY id DESC")

    lastRow = c.fetchone()

    if(lastRow != None):
        print(lastRow[-1])
    else:
        print(0)

    # data = requests.get(url=reportUrl, headers=headers).json()
    # for report in data["reports"]:
    #     print(report)


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


battleType = {'0': '友好切磋',
              '1': '認真決鬥',
              '2': '決一死戰',
              '3': '我要殺死你'}
reportUrl = "https://mykirito.com/api/reports"
headers = {
    'content-type': 'application/json;charset=UTF-8',
    'token': _config["token"],
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}


conn = sqlite3.connect('reports.sqlite3')
print("成功連接資料庫")

c = conn.cursor()

c.execute(
    ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='reports' '''
)
if c.fetchone()[0] == 1:
    print('資料表已存在，開始記錄')

    while True:
        fetchData()
        time.sleep(_config["report"]["period"])
else:
    print('資料表不存在，先建表')

    # id            資料 ID，主鍵
    # playerName    玩家暱稱
    # playerUid     玩家 ID
    # playerLevel   玩家等級
    # myLevel       我方等級
    # type          戰鬥種類（友好切磋, 認真決鬥, 決一死戰, 我要殺死你）
    # result        戰鬥結果（勝利, 戰敗）
    # reportId      戰報 ID
    # hasShout      是否留言（true, false）
    # timestamp     戰報時間（秒）
    conn.execute(
        '''
        CREATE TABLE reports
        (
            id INTEGER PRIMARY KEY  AUTOINCREMENT,
            playerName     TEXT     NOT NULL,
            playerUid      CHAR(30) NOT NULL,
            playerLevel    INT      NOT NULL,
            myLevel        INT      NOT NULL,
            type           TEXT     NOT NULL,
            result         TEXT     NOT NULL,
            reportId       CHAR(30) NOT NULL,
            hasShout       INT      NOT NULL,
            timestamp      INT      NOT NULL
        );
        '''
    )

    while True:
        fetchData()
        time.sleep(_config["report"]["period"])

conn.commit()
conn.close()
