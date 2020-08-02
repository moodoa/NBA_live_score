# NBA_live_score

![alt text](https://miro.medium.com/max/875/0*KxPKgcOZ1eWQdrM7.jpeg)

## livebox.py

### class LiveBox
#### get_today_game_urls
* 以 selenium 進入 watch NBA( https://watch.nba.com/ )，並取得今日賽程URL。
* 回傳值範例如下：`['https://watch.nba.com/game/20200726/PHIOKC', 'https://watch.nba.com/game/20200726/HOUMEM']`。

#### get_live_score
* 將 `get_today_game_urls` 取得的URL傳入，並取得比賽中球賽的 page_source。

#### yell_score_currently
* 將 `get_today_game_urls` 取得的URL以及 `get_live_score` 的 source 傳入，並 print 出當前比賽狀態。
* 狀態如下：`節數 客場隊伍：客場得分 比賽時間 主場隊伍：主場得分`。



## Requirements
python 3

## Usage
`livebox.py`

```
1.取得今日所有比賽的 URL:

today = LiveBox()


2.若該場比賽進行中，傳入該場比賽的 URL 並取得 source。得到 source 後印出比賽狀態。(每 50 秒更新一次):

today_game_urls = today.get_today_game_urls()

while True:
    source = today.get_live_score(today_game_urls[0]) #假設 today_game_urls[0] 這場比賽正在進行中。
    today.yell_score_currently(today_game_urls[0],source)
    time.sleep(50)

```
`yell：`
![alt text](https://i.imgur.com/lxaGOje.png)

## Installation
* `pip install -r requriements.txt`
* 注意 `selenium` 的 driver 是否與 Chrome 版本相符。


