import sys
sys.path.append('../')

from utilities import ChatTemplate

response = ChatTemplate.from_file('writer.json').completion(
    {'action': 'compose',
     'document': 'a haiku about American Sign Language'})

print(response.choices[0].message.content)