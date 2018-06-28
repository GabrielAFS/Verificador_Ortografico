
class WordSet:
    
    #construtor
    def __init__(self):
        self.__words = []

    #verifica se palavra está contida no dicionario
    def contains(self, word):
        
        #caso esteja contida
        if word in self.__words:
            return True
        #caso não esteja contida
        else:
            return False
        
    #adiciona palavra ao conjunto
    def add(self, word):
        self.__words.append(word)

    #getter de words
    def getWords(self):
        return self.__words

    #setter de words
    def setWords(self, words):
        self.__words = words
