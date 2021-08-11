def print_word_list(wl):
    for i, iteam in enumerate(wl):
        print(i+1,"- ",iteam,sep="",end="")

def change_type(choice):
    if choice >= len(wlf_lines) or choice < 0:
        print("Invalid input")
    elif wlf_lines[choice][1] == 'N':
        wlf_lines[choice] = "<K>" + wlf_lines[choice][3:]
    elif wlf_lines[choice][1] == 'K':
        wlf_lines[choice] = "<N>" + wlf_lines[choice][3:]

wlf = open("Words_files/Added_Words_List.txt","r")
wlf_lines = wlf.readlines()
wlf.close()

quit = False
while(not quit):
    print_word_list(wlf_lines)
    try:
        i_choice = int(input("Enter the number of the word you want to change its type: "))
    except:
        print("Enter a number please")
        continue
    change_type(i_choice -1)

    p_choice = input("press (q) to quit or (Enter) to continue.\n")
    if p_choice.lower() == 'q':
        quit = True

file = open("Words_files/Added_Words_List.txt", "w")
for a in wlf_lines:
	file.write(a)
file.close()
print("All changes have been saved.")