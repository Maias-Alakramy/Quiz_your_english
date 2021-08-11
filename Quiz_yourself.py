import random

def printInfo(index):
    if index == 0:
        start = 0
    else:
        start = end_ind[index-1]+1
    end = end_ind[index]
    
    print()
    for i in range(start,end):
        print(wf_lines[i],end="")
    print()



def printRan(a,type):
	choice=[1 for a in a]
	quit=False
	while not quit:
		print("The random word is:",end=" ")
		rand = random.choices(range(len(a)),weights=choice,k=1)
		choice[rand[0]]=0.01*choice[rand[0]]
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

end_ind = []
for i,line in enumerate(wf_lines):
    if line == '_____\n':
        end_ind.append(i)

wlf = open("Words_files/Added_Words_List.txt","r")
wlf_lines = wlf.readlines()
wlf.close()

known_ind = []
new_ind = []
for i,line in enumerate(wlf_lines):
    if line[1] == 'K':
        known_ind.append(i)
    else:
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