choice = -1
while(choice != 4):
    try:
        choice = int(input("Choose what you want to do (Enter the number of the choice):\n"\
            "1- Add the new words in ADD.txt.\n"\
            "2- Change the type of some words in your glossary.\n"\
            "3- Quiz yourself.\n"\
            "4- Quit the program.\n"))
        if choice < 1 or choice > 4:
            raise Exception
    except:
        print("Enter a number between 1 and 4.")
        choice = -1
        continue
    if choice == 1:
        import Add_words
    elif choice == 2:
        import Change_words
    elif choice == 3:
        import Quiz_yourself
    
