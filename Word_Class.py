def try_except_meaning(meanings, type):
        try:
            return meanings[type]
        except:
            return None

options = ['Verb', 'Noun', 'Adverb', 'Adjective']

class Word():
    word_str = ""
    has_def = True

    def __init__(self, Word, meaning):
        self.word = str(Word[0].upper())
        self.word += str(Word[1:].lower())
        self.meanings = meaning
        self.make_word_str()
        self.print_meanings()
        

    
    def print_meanings(self):
        if self.meanings == None:
            print("Couldn't find a definition to ({0})".format(self.word))
            self.has_def = False
            return
        
        options = ['Verb', 'Noun', 'Adverb', 'Adjective']
        print(self.word + ":")
        for option in options:
            this_meaning = try_except_meaning(self.meanings, option)
            if this_meaning == None:
                continue
            print(option)
            for mean in this_meaning:
                print("- " + mean)
            print()
    
    def make_word_str(self):
        self.word_str = str(self.word + "\n")
        for option in options:
            this_meaning = try_except_meaning(self.meanings, option)
            if this_meaning == None:
                continue
            self.word_str += str(option + "\n")
            for mean in this_meaning:
                self.word_str += str("\t- " + mean + "\n")
        self.word_str += "_____\n"
