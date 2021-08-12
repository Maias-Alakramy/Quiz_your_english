# Quiz your English
**A program to make learning new English words easier**

## Usage guide:
1. Create a file called (ADD.txt) if it doesn't already exist.
2. Write any English word you want to add to your glossary in the ADD.txt file (make sure that each word is situated on a new line).
3. Run Program.py and follow the instructions.

> Note: If you don't want to add any new words just skip the first two steps.

## Restrictions:
Please don't delete or rename any file and especially don't edit anything in "Added_Words_List.txt" and "Added_Words.txt" files in "Words_files" folder.

## Additional notes:
- This program can't currently handle phrasal verbs, proverbs and idioms. It can only handle nouns, verbs, adjectives and adverbs
- When you add a new word the program will ask you to choose a type for it.
    - New word: this type is for the words that are totally new for you, when you quiz yourself with this type, you can view its meaning.
    - Known word: this type is for the words that you are familiar with but need some more practice, when you quiz yourself with this type, you can not view its meaning.
- Adding a new word requires a stable internet connection but channing the type of words or quizzing yourself doesn't.
- If a valid word (nouns, verbs, adjectives, adverbs) get rejected and added to "Rejected_Words.txt" file don't hesitate to rewrite it in "ADD.txt" file
- The program will work fine without "Rejected_Words.txt" file, I chose to add it to be just a reminder for the new words you want to learn which this program can't help you with them.

## Credits:
- [geekpradd](https://github.com/geekpradd/PyDictionary) for creating PyDictionary which I used it to create "EPyDictionary.py" (a slightly modified version)