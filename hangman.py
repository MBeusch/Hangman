import numpy as np 
import random


rightLetters = []   #Zustand des Spiels, erratene Buchstaben
dummyLetters = []   #erratene Buchstaben mit entsprechender Häufigkeit im Wort um zu prüfen, ob Wort schon erraten wurde
wrongLetters = []
wrongGuesses = 0
word_list = np.loadtxt('words.txt', dtype='str')


def getWord():
    '''
    Gibt zufälliges Wort in Großbuchstaben zurück.
    '''
    word = random.choice(word_list)
    return word.upper()


def start(word):
    '''
    Suche ein Anfangswort und gebe Anzahl an Buchstaben in Strichen aus.
    '''

    print('\nFinde das Wort! \n')
    string = '___ '*len(word)
    print(string, '\n')



def compareLetters(word, letter):
    '''
    Schaut ob Buchstabe im zu erratenden Wort vorhanden. Wenn JA: Rückgabe aller Indizes, wenn NEIN: Rückgabe von Boolean None.
    '''
    global rightLetters
    global wrongLetters
    global dummyLetters
    #letter = letter.upper()

    if letter in word:
        indices = [index for index, l in enumerate(word) if l == letter]
        rightLetters.append(letter)
        dummyList = [letter]*len(indices)
        dummyLetters += dummyList
        return indices
    else:
        wrongLetters.append(letter)
        return False


def drawHangman(guesses):

    i = '   |            -| '
    j = '   |            -|- '
    l = '   |             /\  '
    e = '   --------------'
    f = '   |             |'
    g = '   |             O'
    h = '   |             | '
    k = '   |             /  '
    d = '   |   '
    c = '   _   '
    b = ' /   \ '
    a=  '|     |'

    nr1 = c+'\n'+b+'\n'+a +'\n'
    nr2 = d+'\n'+d+'\n'+d+'\n'+d+'\n'+d+'\n'+ nr1
    nr3 = e+'\n' + nr2 
    nr4 = e+'\n' + f+'\n' + d+'\n'+d+'\n'+d+'\n'+d+'\n' + nr1
    nr5 = e+'\n' + f+'\n' + g+'\n'+d+'\n'+d+'\n'+d+'\n' + nr1
    nr6 = e+'\n' + f+'\n' + g+'\n'+h+'\n'+d+'\n'+d+'\n' + nr1
    nr7 = e+'\n' + f+'\n' + g+'\n'+i+'\n'+d+'\n'+d+'\n' + nr1
    nr8 = e+'\n' + f+'\n' + g+'\n'+j+'\n'+d+'\n'+d+'\n' + nr1
    nr9 = e+'\n' + f+'\n' + g+'\n'+j+'\n'+k+'\n'+d+'\n' + nr1
    nr10 = e+'\n' + f+'\n' + g+'\n'+j+'\n'+l+'\n'+d+'\n' + nr1

    
    if guesses == 1:
        print(nr1)
    if guesses == 2:
        print(nr2)
    if guesses == 3:
        print(nr3)
    if guesses == 4:
        print(nr4)
    if guesses == 5:
        print(nr5)
    if guesses == 6:
        print(nr6)
    if guesses == 7:
        print(nr7)
    if guesses == 8:
        print(nr8)
    if guesses == 9:
        print(nr9)
    if guesses == 10:
        print(nr10)



def print_underscores(word):
    '''
    Zusammensetzung des Worts mit bereits erratenen Buchstaben. Rausgeworfene Buchstaben in Klammern dahinter.
    '''
    global wrongLetters
    wrongString = '   ('+','.join(wrongLetters)+')'

    global rightLetters
    output = ''
    for c in word:
        if c in rightLetters:
            output += str(c) + ' '
        else:
            output+='__ '
    print(output+ wrongString +'\n')



def play(word):
    '''
    Schleife bis Spiel zu Ende.
    '''
    global wrongGuesses
    global rightLetters
    global dummyLetters

    while wrongGuesses <= 9 and len(dummyLetters) < len(word):
        guess_letter = input('\nNeuer Buchstabe: ')  #Eingabe eines Buchstabens im Terminal
        while guess_letter=='' or len(guess_letter) > 1:
                print('Ungültige Eingabe!')
                guess_letter = input('\nNeuer Buchstabe: ') 
        
        guess_letter = guess_letter.upper()
        print('\n')

        guess_result = compareLetters(word, guess_letter)
        if not guess_result:
            wrongGuesses +=1
            drawHangman(wrongGuesses)
            print_underscores(word)
        else:
            print_underscores(word)

    if wrongGuesses > 9:
        print('Du bist ein absoluter LOSER!')
    else:
        print('Prima, du hast das Spiel hart gerockt!')




def main():
    word = getWord()  #Wort aus Liste zufällig wählen
    #print(word)
    start(word)       #Erster Hint in Form von Strichen
    play(word)



main()