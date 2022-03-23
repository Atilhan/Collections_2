#14-3-2022 #99024233
import random
import string
from unicodedata import digit

#lists
lower_characters = [random.choice(string.ascii_lowercase) for i in range(3)]#De eerste 3 characters worden een lowercase alfabet letter.Die worden gelijk ook randomized.
lower_characters_2 = [random.choice(string.ascii_lowercase) for i in range(4)]#De laatste missende letters worden dan hier in dit list bijtoegevoegd met een append.
upper_characters = [random.choice(string.ascii_uppercase) for i in range(random.randint(2,6))]#Hoofdletters worden bijgevoegd tussen 2 & de 6 
digits = [random.choice(string.digits)for i in range(random.randint(4,7))]#Cijfers worden toegevoegd in de password met tussen de 2 cijfers & 6.
symbols = [random.choice(string.punctuation)for i in range(3)]#Bij de symbols worden er  max & min 3 symbolen toegevoegd.

#variables
#shuffles
randomize_LC_UC_1 = lower_characters_2 + upper_characters + digits + symbols 
random.shuffle(randomize_LC_UC_1)#dit zorgt ervoor dat de bovenste list word geshuffled. ^
randomize_LC_UC = lower_characters+randomize_LC_UC_1 # Dit zorgt ervoor dat de laatste missende letters ook worden geshuffled.
if len(randomize_LC_UC) <24: # De characters van de password mogen niet boven de 24 characters.
	aantal = len(randomize_LC_UC) - 24
	for i in range(abs(aantal)): #absolute , als je 20 characters bv krijgt, gaat er altijd -24 af, dan krijgj e bv -4 (20-24 negative number is -4) met absolute word een negatieve nummer altijd positive, dus 4, en dan word er 4 lowercase bijgevuld.
		randomize_LC_UC.append(random.choice(string.ascii_lowercase))#De missende letters worden hier met een append toegevoegd.

#print execute
print(''.join (randomize_LC_UC)) #.join zorgt ervoor dat de list in een string word veranderd, dus je ziet de aanhalings tekens en commas niet meer in de terminal.
print('Aantal Karakters:',len( ''.join(randomize_LC_UC))) #Laat zien hoeveel characters er zijn in de password.







