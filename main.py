import requests
from twilio.rest import Client
from config import *

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


}
stock_responce = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
stock_responce.raise_for_status()
data = stock_responce.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_close_price = data_list[0]["4. close"]
before_yesterday_close_price = data_list[1]["4. close"]
abs_difference = abs(float(yesterday_close_price) - float(before_yesterday_close_price))
pers_difference = abs_difference / float(yesterday_close_price) * 100


news_responce = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
news_responce.raise_for_status()
last_news = news_responce.json()["articles"][:3]
three_news = [f"Headline: {article['title']}. \nBrief: {article['description']}"for article in last_news]

if pers_difference > 5:
    client = Client(account_sid, auth_token)
    for article in three_news:
        message = client.messages.create(
            body=article,
            from_='+19793644765',
            to='+905515945600'
        )

        print(message.status)


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

