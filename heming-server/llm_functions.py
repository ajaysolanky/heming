import requests
import os
import anthropic


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

OPENAI_MODEL = 'gpt-4-turbo-preview'

headers = {
    'Authorization': f'Bearer {OPENAI_API_KEY}',
    'Content-Type': 'application/json',
}

def openai_call(messages):
    print("CALLING OPENAI")
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

def claude_call(messages):
    print("CALLING CLAUDE")
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    # Prepare the messages in the format required by Claude

    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024 * 4,
            messages=messages
        )
        
        # Assuming the structure of the response, adjust based on actual response
        server_response = response.content
        response_data = {"response": server_response[0].text}
        
        return response_data
    except Exception as e:
        raise Exception(f"Failed to fetch response from Claude: {str(e)}")