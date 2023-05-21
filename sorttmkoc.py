# Contributed by @AryAgain

import json
import re

# Load the JSON file
try:
    with open('tmkoc.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Jethiyaa JSON file not found.")
    exit()
except json.JSONDecodeError:
    print("Babuji Invalid JSON format.")
    exit()
except Exception as e:
    print("Tappu sena An error occurred while loading the JSON file:", e)
    exit()

# Check if 'episodes' key exists in the loaded data
if 'episodes' not in data:
    print("Jaya No 'episodes' key found in the JSON data.")
    exit()

# Sort the episodes by episode number
sorted_episodes = sorted(data['episodes'], key=lambda x: int(re.split(r'[:\s]', x['episode'])[1]))

# Print the sorted episodes
# for episode in sorted_episodes:
#     print(episode['episode'])

# Create a new dictionary with sorted episodes
sorted_data = {'episodes': sorted_episodes}

# Write the sorted data to a new JSON file
output_file = 'sorted_tmkoc.json'
try:
    with open(output_file, 'w') as f:
        json.dump(sorted_data, f, indent=4)
    print(f"Tarak Bhai Sorted JSON file '{output_file}' has been generated.")
except Exception as e:
    print("Bhide An error occurred while writing the sorted JSON file:", e)
