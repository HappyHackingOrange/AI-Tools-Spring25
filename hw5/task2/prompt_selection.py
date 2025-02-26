import sys

sys.path.append('../')

from utilities import ChatTemplate
import json

selectionTemplate = ChatTemplate.from_file('selection_chat.json')

while True:
    ask = input('ask: ')
    if ask == 'exit':
        break

    response = selectionTemplate.completion({'ask': ask})
    print(response.choices[0].message.content)

    selection = json.loads(response.choices[0].message.content)

    response = ChatTemplate.from_file(f"{selection['as']}_chat.json").completion({
        'action': selection['action'],
        'document': selection['document']})

    print(response.choices[0].message.content)
