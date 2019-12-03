# - copyright (c) Adrian H. 2019
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
 
frage = "- Frage -   "
loesung = " Antwort "
 
quizfrage(frage, loesung)
 
frage = "- Frage -  "
loesung = " Antwort "
 
quizfrage(frage, loesung)
 
frage = "- Frage - "
loesung = " Antwort "
 
quizfrage(frage, loesung)

frage = "- Frage -"
loesung = " Antwort "

quizfrage(frage, loesung)

frage = " - Frage -"
loesung = " Antwort "

quizfrage(frage, loesung)

if punkte == 5:
    print (" ")
    print("Gut")
elif punkte == 2 or punkte == 1:
    print (" ")
    print("Ich würd nochmal lernen")
else:
    print (" ")
    print("Du musst mal wieder lerne")
 
print("Du hast", punkte, "Punkte erreicht")
