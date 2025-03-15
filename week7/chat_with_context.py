import sys
sys.path.append('../')

from utilities import ChatTemplate

chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are an AI chat program.'},
                  {'role': 'user', 'content': '{{prompt}}'}]})

while True:
    prompt = input('user: ')
    if prompt.lower() == 'exit':
        break

    # 1. store the user input in memory
    chat.template['messages'].append({'role': 'user', 'content': prompt})

    # 2. call the model with the user input
    response = chat.completion({'prompt': prompt})

    # 3. extract message content
    message = response.choices[0].message
    print(f"{message.role}: {message.content}")

    # 4. store the model response in memory
    chat.template['messages'].append({'role': message.role, 'content': message.content})
