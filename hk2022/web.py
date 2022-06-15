import requests
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
hddata = {'User-agent':agent}
req = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105', headers=hddata)

html = req.text
print(html)