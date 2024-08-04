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


# https://learn.deeplearning.ai/genai4e/lesson/2/activity2
def llm_response(prompt):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user','content':prompt}],
        temperature=0
    )
    return response.choices[0].message.content

all_reviews = [
    'The mochi is excellent!',
    'Best soup dumplings I have ever eaten.',
    'Not worth the 3 month wait for a reservation.',
    'The colorful tablecloths made me smile!',
    'The pasta was cold.'
]
# all_reviews

all_sentiments = []
for review in all_reviews:
    prompt = f'''
        Classify the following review 
        as having either a positive or
        negative sentiment. State your answer
        as a single word, either "positive" or
        "negative":

        {review}
        '''
    response = llm_response(prompt)
    all_sentiments.append(response)
#  all_sentiments

num_positive = 0
num_negative = 0
for sentiment in all_sentiments:
    if sentiment == 'positive':
        num_positive += 1
    elif sentiment == 'negative':
        num_negative += 1
print(f"There are {num_positive} positive and {num_negative} negative reviews.")
