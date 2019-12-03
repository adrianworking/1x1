# - copyright (c) Adrian Hom 2019
#  _    _                                          _      
# | |  | |                                        | |     
# | |__| | ___  _ __ ___   ___ _ __ ___   __ _  __| | ___ 
# |  __  |/ _ \| '_ ` _ \ / _ \ '_ ` _ \ / _` |/ _` |/ _ \
# | |  | | (_) | | | | | |  __/ | | | | | (_| | (_| |  __/
# |_|  |_|\___/|_| |_| |_|\___|_| |_| |_|\__,_|\__,_|\___|
                            




#- - - - - - - - - - - - - - - - - - - - #
#    Importiere wichtige Bibliotheken    #
#- - - - - - - - - - - - - - - - - - - - #


from sys     import *
from os      import *

#- - - - - - - - - - - - - - - - - - - - #
#          Shell gestalten               #
#- - - - - - - - - - - - - - - - - - - - #


print ("  _____ _             _               ")
print (" / ____| |           | |              ")
print ("| (___ | |_ __ _ _ __| |_ ___         ")
print (" \___ \| __/ _` | '__| __/ _ \        ")
print ("  ____) | || (_| | |  | ||  __/_ _ _  ")
print (" |_____/ \__\__,_|_|   \__\___(_|_|_) ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")



def quizfrage(frage, loesung):
    global punkte
 
    antwort = input(frage)
 
    if antwort == loesung:
        print(antwort, "ist richtig")
        punkte = punkte + 1
    else:
        print(antwort, "ist falsch, richtig ist", loesung)
 
#- - - - - - - - - - - - - - - - - - - - #
#               Fragen                   #
#- - - - - - - - - - - - - - - - - - - - #
 
punkte = 0
 
frage = "Was ist 13 mal 4?   "
loesung = "52"
 
quizfrage(frage, loesung)
 
frage = "Was ist 15 mal 5     "
loesung = "75"
 
quizfrage(frage, loesung)
 
frage = "Was ist 6 mal 8     "
loesung = "48"
 
quizfrage(frage, loesung)

frage = "Was ist 5 mal 5     "
loesung = "25"

quizfrage(frage, loesung)

frage = "Was ist 8 mal 3     "
loesung = "24"

quizfrage(frage, loesung)

if punkte == 5:
    print (" ")
    print("Geil alda!")
elif punkte == 2 or punkte == 1:
    print (" ")
    print("Ich würd nochmal Mathe lernen...")
else:
    print (" ")
    print("Du musst mal wieder Mathe lernen")
 
print("Du hast", punkte, "Punkte erreicht")
