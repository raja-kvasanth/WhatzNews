import requests
import time
from twilio.rest import Client

news_api_key="291d3e75e1f8457bbxxxxxxxxxxxxx"
content="India Pakistan conflict"
twilio_sid="AC431e80f1de699xxxxxxxxxx"
twilio_auth_token="94a88b9eb8051192xxxxxxxxxxx"
from_whatsapp_num="whatsapp:+14155238886"
to_whatsapp_num="whatsapp:+91962xxxxxxx"

client=Client(twilio_sid,twilio_auth_token)

def get_latest_news():
    url=(
        f"https://newsapi.org/v2/everything?"
        f"q={content}&"
        f"language=en&"
        f"sortBy=publishedAt&"
        f"pageSize=1&"
        f"apikey={news_api_key}"
    )
    response=requests.get(url)
    data=response.json()
    
    if data["status"] =="ok" and data["totalResults"] > 0:
        messages=[]
        for article in data["articles"]:
            title=article["title"]
            source=article["source"]["name"]
            published=article["publishedAt"]
            url=article["url"]
            message=f" *{title}*\n {source} |  {published}\n {url}"
            messages.append(message)
        return "\n\n".join(messages)
    else:
        return  " No recent news found on India Pakistan conflict."
    
def send_whatsapp_message(message):
    client.messages.create(
        from_=from_whatsapp_num,
        body=message,
        to=to_whatsapp_num
    )
    
while True:
    print("Checking for latest news")
    news=get_latest_news()
    print("Sending to Whatsapp")
    send_whatsapp_message(news)
    print("Done. Next message will be updated on next one hour..\n")
    time.sleep(3600)
