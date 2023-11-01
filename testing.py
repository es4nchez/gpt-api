import os
import openai
import json
openai.api_key = os.getenv("OPENAI_API_KEY")
from datetime import datetime

models = openai.Model.list()
models_dict = {model['id']: model['created'] for model in models['data']}
sorted_models_dict = dict(sorted(models_dict.items(), key=lambda item: item[1]))

formatted_models_dict = {k: datetime.utcfromtimestamp(v).strftime('%Y-%m-%d %H:%M:%S') for k, v in sorted_models_dict.items()}

print(json.dumps(formatted_models_dict, indent=4))


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a professional programmer in C language."},
    {"role": "user", "content": "Can you give guidelines, 3 steps of one sentences each, to developp a shell"}
  ]
)

print(completion.choices[0].message)