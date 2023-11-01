import os
import openai
import json
from datetime import datetime

class GPT_API:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.models = self.list_models()

    def print_models(self):
        print(json.dumps(self.models, indent=4))

    def list_models(self):
        models = openai.Model.list()
        models_dict = {model['id']: model['created'] for model in models['data']}
        sorted_models_dict = dict(sorted(models_dict.items(), key=lambda item: item[1]))
        formatted_models_dict = {k: datetime.utcfromtimestamp(v).strftime('%Y-%m-%d %H:%M:%S') for k, v in sorted_models_dict.items()}
        return formatted_models_dict

    def generate(self, model):
        if model not in self.models:
            print(f'Error: model \"{model} not found nor availaible')
            exit(1)
        else:
            self.model = model
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a professional programmer in C language."},
                {"role": "user", "content": "Can you give guidelines, 3 steps of one sentences each, to developp a shell"}
            ]
        )
        print(completion.choices[0].message)