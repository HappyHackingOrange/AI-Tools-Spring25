import sys
sys.path.append('../')

from utilities import ChatTemplate

selection = ChatTemplate.from_file('selection.json')

response = selection.completion(
    {'ask': 'I need an open-source license document'})

print(response.choices[0].message.content)

response = selection.completion(
    {'ask': 'I need a funny skit'})

print(response.choices[0].message.content)