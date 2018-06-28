from Wordset import WordSet
from Purge import Purge

class Dictionary(WordSet, Purge):

    #construtor
    def __init__(self):
        WordSet.__init__(self)  #construtor da classe pai
        
    #carrega arquivo
    def load(self):
        try:
            fread = open('main-dict.txt', 'r')
        except OSError:
            print('Erro ao abrir arquivo!')
        else:
            self.removen(fread.readlines())
            fread.close()

    #salva arquivo ao fim do programa
    def save(self):
        fwrite = open('main-dict.txt', 'w')
        aux = WordSet.getWords(self)

        #escreve linha por linha no arquivo
        for a in aux:
            fwrite.write(a+'\n')

        #fecha arquivo
        fwrite.close()

    #remove de \n das pelavras
    def removen(self, words):
        for w in words:
            WordSet.add(self, w.rstrip())
            
        
