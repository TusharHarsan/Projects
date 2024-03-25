import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
import datetime
import requests
import random

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    # openai.api_key = "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"
    chatStr += f"Tushar: {query}\n Jarvis: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speaker.Speak(response["choices"][0]["text"])
    chatStr += response["choices"][0]["text"]
    return response["choices"][0]["text"]

def shutdown(query):
    speak("Shutting down the computer. Goodbye!")
    os.system("shutdown /s /t 1")


def businessnews(query):
    main_api = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=98665c9335254550b21ff7690b5c0bed"

    news = requests.get(main_api).json()
    articles = news['articles']
    news_article = [arti['title'] for arti in articles]

    # Ensure there are at least 5 articles
    if len(news_article) >= 5:
        selected_articles = random.sample(news_article, 5)
        for article_title in selected_articles:
            print(article_title)
            speaker.Speak(article_title)
    else:
        print("Not enough articles to select 5 random news.")


def Technews(query):
    main_api = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=98665c9335254550b21ff7690b5c0bed"

    news = requests.get(main_api).json()
    articles = news['articles']
    news_article = [arti['title'] for arti in articles]

    # Ensure there are at least 5 articles
    if len(news_article) >= 5:
        selected_articles = random.sample(news_article, 5)
        for article_title in selected_articles:
            print(article_title)
            speaker.Speak(article_title)
    else:
        print("Not enough articles to select 5 random news.")


def weather(query):
    weather.apikey = "30d4741c779ba94c470ca1f63045390a"
    city = ''.join(query.split('in')[1:])
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={weather.apikey}"
    )
    weater = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    print(f"The weather in {city} is: {weater}, and the temperature in {city} is: {temp} degrees fahrenheit")
    speaker.Speak(f"The weather in {city} is: {weater}, and the temperature in {city} is: {temp}degrees fahrenheit")


def ai(prompt):
    # openai.api_key = "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"
    text = f"Openai response for prompt: {prompt} \n *******************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
    except Exception as e:
        print(f"An error occurred: {e}")

    with open(f"Openai/prompt- {''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)


speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    os.system(f"say{text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:

        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('PyCharm')
    speaker.Speak("good evening sir,Jarvis here")

    while True:

        print("Listening.....")

        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.Google.com"], ["armorgames", "https://armorgames.com/"]]
        for site in sites:

            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} sir.... ")
                webbrowser.open(site[1])

        if "open music" in query:
            speaker.Speak("Opening Spotify sir")
            Spotify = "https://open.spotify.com/"
            webbrowser.open("Spotify")

        elif "open alarm" in query:
            speaker.Speak("Opening alarm sir")
            os.system("python jarvis_alarm.py")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speaker.Speak(f"Sir time is {hour} bajjkkkkee {min} minutes")

        elif "close".lower() in query.lower():
            speaker.Speak("Shutting Down")
            exit()

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "what's the weather" in query:
            weather(query)

        elif "the business news" in query:
            businessnews(query)
        elif "the technology news" in query:
            Technews(query)
        elif "game".lower() in query.lower():
            speaker.Speak("Opening game")
            os.system("python ticc2222.py")
        elif "shutdown".lower() in query.lower():
            shutdown(query)
        else:
            chat(query)


