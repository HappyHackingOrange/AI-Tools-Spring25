import sys
sys.path.append('../')

from utilities import ChatTemplate
import json

selectionTemplate = ChatTemplate.from_file('selection.json')

while True:
    # our example: "please write a poem about ASL"
    ask = input('ask: ')
    if ask == 'exit':
        break
    
    # first LLM call. This time, AI returned a json file which looks like:
    #   {"as": "writer", "action": "compose", "document": "a poem about American Sign Language."}
    response = selectionTemplate.completion({'ask': ask})
    print(response.choices[0].message.content)

    # load the json file to memory (basically translate the json file to a python object)
    selection = json.loads(response.choices[0].message.content)

    '''
    `selection` object:
    - as: writer
    - action: compose
    - document: a poem about american sign language
    '''
    # making the second LLM call. 
    #   here, we need to tell the AI to look for the right template, which is `writer_chat.json`.
    #   note that `selection['as']` is `writer` in this case, 
    #   thus selection['as'] + '_chat.json' -> writer_chat.json
    response = ChatTemplate.from_file(selection['as'] + '_chat.json').completion({
        'action': selection['action'],
        'document': selection['document']})
    
    print(response.choices[0].message.content)