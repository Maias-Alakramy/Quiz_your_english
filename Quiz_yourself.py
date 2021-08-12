'''
This program will choose a random word of the type you chose and low its probability to appear
so much so that it's almost never going to reappear unless all the other words does first 

The generale form of Added_Words file this program will read:

word1
multi
line
meaning
_____
word2
multi
line
meaning
_____

The generale form of Added_Words_List file this program will read:

<'type'> word1
<'type'> word2
<'type'> word3

where 'type' can be only (K) or (N)
'''

import random

def printInfo(index): # Print the meaning of a chosen word
    if index == 0: # It's the first word
        start = 0
    else:
        start = end_ind[index-1]+1
    end = end_ind[index]
    
    print()
    for i in range(start,end):
        print(wf_lines[i],end="")
    print()



def printRan(a,type): # Print a random word of a chosen type
	choice=[1 for a in a] # The probability of choosing an index
	quit=False
	while not quit:
		print("The random word is:",end=" ")
		rand = random.choices(range(len(a)),weights=choice,k=1)
		choice[rand[0]]=0.01*choice[rand[0]] # Reduce the probability of the choice
		print(wlf_lines[a[rand[0]]][4:])
		p = input("press (i) to show info, (q) to quit"\
			" or press Enter to get another word.\n")
		quit=(p.lower() == "q")
		
		if(p=="i"):
			if(type == 'K'):
				print("You should know the meaning by yourself ;)",end="\n\n")
				continue
			printInfo(a[rand[0]])


wf = open("Words_files/Added_Words.txt","r")
wf_lines = wf.readlines()
wf.close()

end_ind = [] # The indices of the last line of a word ("_____\n" line) in "Added_Words.txt" file
for i,line in enumerate(wf_lines):
    if line == '_____\n':
        end_ind.append(i)

wlf = open("Words_files/Added_Words_List.txt","r")
wlf_lines = wlf.readlines()
wlf.close()

known_ind = [] #The indices of the known in "Added_Words_List.txt" file
new_ind = [] #The indices of the new in "Added_Words_List.txt" file
for i,line in enumerate(wlf_lines):
    if line[1] == 'K': #The word's type is (Known)
        known_ind.append(i)
    else: #The word's type is (New)
        new_ind.append(i)

choice = input("press (n) for new words or (k) for known words.\n")
while choice != "q":
    if choice.lower() == "n":
        printRan(new_ind, choice.upper())
    elif choice.lower() == "k":
        printRan(known_ind, choice.upper())
    else:
        print("Invalid input.")
    choice = input("press (q) to exit the programe, (n) for new words or (k) for known words.\n")