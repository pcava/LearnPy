# https://www.udemy.com/course/chatgpt-complete-masterclass/learn/lecture/39426094#overview

import os
from textblob import TextBlob
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI(
  api_key = os.getenv("OPENAI_API_KEY"),
)


conversation_history = []
persona= input("What persona you want me to be: ")
while True:
  user_input = input("User Input: ")
  if user_input == "Change Persona":
    persona= input("What persona you want me to be: ")
  if user_input == "Quit":
    break
  conversation_history.append({"role": "user", "content": user_input})
  conversation_history.append({"role": "system", "content": persona})
  
  ai_response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages= conversation_history,
  max_tokens=1000,
  temperature=0.6 
  )

  ai_output = ai_response.choices[0].message.content
  print("AI Answer:" , ai_output)
  conversation_history.append({"role": "system", "content": ai_output})

blob = TextBlob(ai_output)
sentiment = blob.sentiment


sentiment_label = "Neutral"
if sentiment.polarity > 0:
    sentiment_label = "Positive"
elif sentiment.polarity < 0:
    sentiment_label = "Negative"

print("This is the sentiment: ", sentiment_label )

conversation_history.append({"role": "user", "content": "Please briefly summarize this conversation."})

ai_response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages= conversation_history,
  max_tokens=1000,
  temperature=0.6 
  )

ai_output = ai_response.choices[0].message.content
print("This the summary of the conversation: ", ai_output)
