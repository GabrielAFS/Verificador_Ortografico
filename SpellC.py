from Dictionary import Dictionary
from Purge import Purge

class SpellChecker(Purge):

    #construtor
    def __init__(self):
        self.__ignored = []  #lista de palavras ignoradas pelo usuário
        self.__vtext = []  #lista com textos inseridos pelo usuário
        self.__mtext = []  #lista que contém lista com as palavras de vtext, por linha

    #metodo principal
    def main(self):
        dic = Dictionary()  #inicializa dicionário
        dic.load()  #carrega palavras
        self.__load_document()  #carrega documento de entrada

        for txt in self.__mtext:
            for i in range(0, len(txt)):
                if not dic.contains(txt[i]) and txt[i] not in self.__ignored:
                    self.__consult_user(dic, txt, i)
                else:
                    pass

        self.__save_document()  #salva texto corrigido no documento de saída
        dic.save()  #salva dicionário

    #documentos de entrada
    def __load_document(self):
        try:
            finput = open('input.txt', 'r')  #carrega arquivo a ser verificado
        except OSError:
            print('Erro ao abrir arquivo!')
        else:
            self.removen(finput.readlines())  #lista com textos a serem carregados
            finput.close()  #fecha arquivo
            
            for e in self.__vtext:
                self.__mtext.append(e.split())  #cada linha é transformada em uma lista

    #documentos de saída
    def __save_document(self):
        try:
            foutput = open('output.txt', 'w')  #carrega arquivo de saída
        except OSError:
            print('Erro ao abrir arquivo!')
        else:
            for txt in self.__mtext:
                foutput.write(' '.join(txt) + '\n')  #junta cada frase e escreve no arquivo
                
            foutput.close()  #fecha arquivo

    #interação com o usuário
    def __consult_user(self, dic, words, i):
        print(f'Palavra {words[i]} não está contida no dicionário')
        print(28*'=')
        print('1- Ignorar')
        print('2- Aceitar')
        print('3- Substituir')
        op = int(input('Digite a opção desejada: '))

        if op == 1:
            self.__ignored.append(words[i])  #palavra adicionada a lista de ignorados
            print('Palavra adicionada a lista de ignorados')
        elif op == 2:
            dic.add(words[i])  #adiciona palavra ao dicionário
            dic.getWords().sort()  #ordena dicionário
            print(f'\n{words[i]} foi adicionada ao dicionário')
        elif op == 3:
            newWord = str(input('\nDigite a nova palavra: ')).lower()
            words[i] = newWord  #palavra corrigida pelo usuário
        
    #remove \n do texto
    def removen(self, texts):
        for t in texts:
            self.__vtext.append(t.rstrip())


##########################################################################################################
s = SpellChecker()  #instancia classe
s.main()  #inicia programa
