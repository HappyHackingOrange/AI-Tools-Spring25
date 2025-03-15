import sys

sys.path.append('../')

from utilities import ChatTemplate
import re


def step(template_file, pattern, parameters=None):
    if parameters is None:
        parameters = {}

    chat_template = ChatTemplate.from_file(template_file)
    print(chat_template.template['messages'][-1]['content'])

    while True:
        prompt = input('User: ')
        chat_template.template['messages'].append({'role': 'user', 'content': prompt})

        message = chat_template.completion(parameters).choices[0].message

        if 'DONE' in message.content:
            return re.search(pattern, message.content, re.DOTALL).group(1).strip()

        print(f'{message.content}')
        chat_template.template['messages'].append({'role': message.role, 'content': message.content})


# Get problem description
problem = step('first_template.json', r'PROBLEM(.*)DONE')

# Get device info and priority with the problem as a parameter
priority = step('second_template.json', r'PRIORITY(.*)DONE', {"problem": problem})

print("\nTech Support Ticket Created:")
print(f"Issue: {problem}")
print(f"Priority: {priority}")
print("A support technician will contact you shortly.")
