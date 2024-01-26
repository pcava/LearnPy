# https://platform.openai.com/docs/quickstart?context=python

import os
from dotenv import load_dotenv

from openai import OpenAI

client = OpenAI(
  api_key = os.getenv("OPENAI_API_KEY"),
)

# chat completions
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  # model = "gpt-4-turbo-preview",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message.content)


# embeddings
response = client.embeddings.create(
  model="text-embedding-ada-002",
  input="The food was delicious and the waiter..."
)

print(response.data[0].embedding)


# images
response = client.images.generate(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)

print(response.data[0].url)
print(response.data[1].url)
