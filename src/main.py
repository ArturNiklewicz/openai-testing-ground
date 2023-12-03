import openai
from streamlit_test import table

openai.api_key = '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'

completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You generate funny titles for my blog posts"},
    {"role": "user", "content": "Generate a ridiculous title for my boring app displaying just a table"},
  ] )

table(completion.choices[0].message.content)
# table(completion.choices[0].text)
# print(completion.choices[0].message)
