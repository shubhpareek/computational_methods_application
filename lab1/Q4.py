import numpy as np
import string
import random

class TextGenerator:
    #innitialisation
    firword = ""
    secword = ""

    sizefodicforwords = {}  
    # size of adjacency list
    
    dicforwords = {}  
    # map of words
    unique_words_array = []

    # function to read file and make prefix dictionary
    def assimilateText(self, file):
        #openfile in read mode
        f = open(file, 'r')
        content = f.read()
        f.close()

        words = content.split()
        # splinting the file with space
        
        #to get rid of ", "
        table = str.maketrans('', '', string.punctuation)

        aftertrans = [w.translate(table) for w in words]

        # checking  if words contain  alphabets
        aftertrans = [word for word in aftertrans if word.isalpha()]

        # converting all the words to lower case
        aftertrans = [word.lower() for word in aftertrans]

        # taking only unique words
        self.unique_words = set(aftertrans)
        self.unique_words_array = list(self.unique_words)

        # initializing the adj list and its size for all pair of words
        for firstw in self.unique_words:
            self.sizefodicforwords[firstw] = {}
            self.dicforwords[firstw] = {}
            for sWord in self.unique_words:
                self.dicforwords[firstw][sWord] = []
                self.sizefodicforwords[firstw][sWord] = 0

        for i in range(len(aftertrans)-2):
            self.dicforwords[aftertrans[i]][aftertrans[i+1]].append(aftertrans[i+2])
            self.sizefodicforwords[aftertrans[i]][aftertrans[i+1]] += 1

    def nextrandword(self, firword, secword):
        prob = []
        next_word = []

        try:
            # see if the firword is valid key
            if self.dicforwords.get(firword) is not None:
                # see if the secword is valid key
                if self.dicforwords.get(firword).get(secword) is not None:
                    #  if current word has non-zero len adjacency list than use it
                    if self.sizefodicforwords[firword][secword]:
                        next_word = np.random.choice(self.dicforwords[firword][secword])
                    # otherwise select random word
                    else:
                        next_word = np.random.choice(self.unique_words_array)

                    return next_word
                else:
                    raise Exception(
                        "Unable to produce text with the specified start word.")

            else:
                raise Exception(
                    "Unable to produce text with the specified start word.")

        except Exception as inst:
            print(type(inst))
            print(inst)

    def generateText(self, n, word=""):
        if word != "":
            firstw = word
            for sWord in self.unique_words:
                if self.dicforwords.get(firstw) is not None:
                    if self.dicforwords.get(firstw).get(sWord) is not None:
                        if self.dicforwords[firstw][sWord] != []:
                            self.firword = firstw
                            self.secword = sWord
        else:
            for firstw in self.unique_words:
                for sWord in self.unique_words:
                    if self.dicforwords.get(firstw) is not None:
                        if self.dicforwords.get(firstw).get(sWord) is not None:
                            if self.dicforwords[firstw][sWord] != []:
                                self.firword = firstw
                                self.secword = sWord

        print(self.firword)
        print(self.secword)
        print(self.dicforwords[self.firword][self.secword])

        try:
            if self.firword == "" or self.secword == "":
                raise Exception(
                    "Unable to produce text with the specified start word.")

        except Exception as inst:
            print(type(inst))
            print(inst)
            return

        ansText = []
        ansText.append(self.firword)
        ansText.append(self.secword)

        # calling random word function for n-2 times to generate the full text
        for i in range(n-2):

            word = self.nextrandword(self.firword, self.secword)
            # print("word: ", word)
            self.firword = self.secword
            self.secword = word
            # print("word:", word)
            if word == None:
                break
            else:
                ansText.append(word)

        # print(ansText)
        print(*ansText, sep=" ")

def main():
    t = TextGenerator()
    t.assimilateText('sherlock.txt')
    t.generateText(50)
if __name__ == "__main__":
    main()
