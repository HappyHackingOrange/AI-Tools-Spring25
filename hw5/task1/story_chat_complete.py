import json
from utilities import ChatTemplate

# Load the stories from the JSON file
with open('stories.json', 'r') as f:
    stories_data = json.load(f)

# Loop through each story in the stories list
for story in stories_data['stories']:
    response = ChatTemplate.from_file('story_chat.json').completion(
        {
            'character': story['character'],
            'setting': story['setting'],
            'conflict': story['conflict']
        }
    )

    # Print the generated story
    print(response.choices[0].message.content)
    print("\n---\n")  # Separator between stories
