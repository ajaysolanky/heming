import requests
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

OPENAI_MODEL = 'gpt-4-turbo-preview'

headers = {
    'Authorization': f'Bearer {OPENAI_API_KEY}',
    'Content-Type': 'application/json',
}

def openai_call(messages):
    data = {
        'model': OPENAI_MODEL,
        'messages': messages,
    }

    print("REQUEST:")
    print(data)

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

    if response.status_code == 200:
        openai_response = response.json()
        server_response = openai_response['choices'][0]['message']['content']
        response_data = {"response": server_response}
    else:
        raise Exception("Failed to fetch response from OpenAI")

    return response_data
