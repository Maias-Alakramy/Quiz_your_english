from EPyDictionary import PyDictionary
from Word_Class import Word

def delet_element(arrray, word, has_n):
    if has_n:
        word += "\n"
    arrray.remove(word)

def add_to_file(meaning, type):
    wf.write(meaning.word_str)
    wlf.write("<{0}> {1}\n".format(type.upper(), meaning.word))
    delet_element(words, word, has_n)

def regect_word(words, word, has_n):
    print("it's been added to the \"Rejected_Words\" file.\n\n".format(word))
    word += "\n"
    rf.write(word)
    if not has_n:
        word = word[:-1]
    print(words, word, has_n)
    delet_element(words, word, has_n)

dictionary = PyDictionary()

file = open("ADD.txt", "r")
file_lines = file.readlines()
words = file_lines.copy()
file.close()

wf = open("Words_files/Added_Words.txt","a")
wlf = open("Words_files/Added_Words_List.txt","a")
rf = open("Words_files/Rejected_Words.txt","a")

for word in file_lines:
    has_n = False
    if word[-1:] == "\n":
        has_n = True
        word = word[:-1]
    
    if len(word.split()) > 1:
        print("Can't get the meaning of ({0}) because it consist of more than a word".format(word))
        regect_word(words, word, has_n)
        continue

    meaning = Word(word, dictionary.meaning(word))
    if not meaning.has_def:
        regect_word(words, word, has_n)
        continue

    choice = input("Do you want to label this word as \"New word\" or "\
        "as \"Known words\"? (press n for New or K for Known): ")
    if choice.lower() not in ['n','k']:
        print("please press only \"n\" or \"k\" and not any other key.")
        print("( " + word + " ) has NOT been added to any file.\n\n")
        continue
    add_to_file(meaning, choice)
    print("( " + meaning.word + " ) has been added to the file.\n\n")

wf.close()
rf.close()

file = open("ADD.txt", "w")
for a in words:
	file.write(a)
file.close()

print("All words have been added.")