import requests
from datetime import *
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
VANTAGE_API_KEY = "S039EK1ZR1778AKV"
NEWS_API = "73964898165b4a02bd5524d4790a9096"


account_sid = 'ACf212da148153b87f50920f9192ea0186'
auth_token = '42a5f44f556f7e8da872bc766ec09a6b'
client = Client(account_sid, auth_token)

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : VANTAGE_API_KEY
}

now = datetime.now()
yesterday = str(now.date() - timedelta(days = 1))
day_before_yesterday = str(now.date() - timedelta(days = 2))
print(yesterday)

news_params = {
    "q": "Tesla",
    "name": COMPANY_NAME,
    "from": now.date() - timedelta(days = 5),
    "searchIn": "title",
    "to": now.date(),
    "language": "en",
    "sortBy": "popularity",
    "pageSize": 3,
    "apiKey": NEWS_API

}
'''
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url = "https://www.alphavantage.co/query", params = stock_params )
stock_data = stock_response.json()
print(stock_data)
closing_stock = float(stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"])
opening_stock = float(stock_data["Time Series (Daily)"][yesterday]["1. open"])'''

response = requests.get(url = "https://www.alphavantage.co/query", params=stock_params)
data = response.json()["Time Series (Daily)"]
print(data)
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_response = requests.get(url = "https://newsapi.org/v2/everything", params = news_params)
news_data = news_response.json()


news = {"title":[], "description":[], "url":[]}


for i in news_data["articles"]:
    title = i["title"]
    description = i["description"]
    url = i["url"]
    news["title"].append(title)
    news["description"].append(description)
    news["url"].append(url)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
if yesterday_closing_price > day_before_yesterday_closing_price:
    increment = ((yesterday_closing_price - day_before_yesterday_closing_price)/yesterday_closing_price)*100
    symbol = "🔺"
else:
    increment = ((yesterday_closing_price - day_before_yesterday_closing_price) / yesterday_closing_price) * 100
    symbol = "🔻"

if increment <= 5:
    for i in range(0,3):
        message = client.messages.create(
            from_='+18146463187',
            body=f'{STOCK}: {symbol}{increment}% \n Headline: {news["title"][i]}\n Brief: {news["description"][i]}\n Url: {news["url"][i]}',
            to='+918296807476'
    )



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

