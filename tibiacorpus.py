import requests
import re

# urls
npc_conversations = "https://resources.talesoftibia.com/data/npcs/transcripts.json"
npc_dialogues = "https://resources.talesoftibia.com/data/npcs/npc-data.json"
books = "https://resources.talesoftibia.com/data/books/books.json"

# get the data
npc_conversations_response = requests.get(npc_conversations)
npc_conversation_data = npc_conversations_response.json()
npc_dialogues_response = requests.get(npc_dialogues)
npc_dialogues_data = npc_dialogues_response.json()
books_response = requests.get(books)
books_data = books_response.json()

words = set()


# clean the words
def clean_word(word):
    # clean all but letters and numbers
    return re.sub(r'[^a-z0-9]', ' ', word.lower())

# split
def splitter(text):
    words.update(clean_word(text).split())


# make a set of all words in the conversations from all npcs
for npc in npc_conversation_data:
  for conversation in npc['conversation']:
    splitter(conversation['prompt'])
    for answer in conversation['answer']:
      splitter(answer)

# make a set of all words in the dialogues from all npcs
for npc in npc_dialogues_data:
  splitter(npc['name'])
  splitter(npc['job'])
  splitter(npc['race'])
  splitter(npc['location'])
  splitter(npc['subarea'])
  for dialogue in npc['dialogues']:
    splitter(dialogue)

# make a set of all words in the books
for book in books_data:
  splitter(book['text'])

# filter out empty words
words = [word for word in words if word]

# sort the words A-Z then 0-9, then by length
words = sorted(words, key=lambda word: (len(word), word))

# save the words to a file
with open('words.txt', 'w', encoding='utf-8') as f:
    for word in words:
        f.write(word)
        if word != words[-1]:
            f.write('\n')


