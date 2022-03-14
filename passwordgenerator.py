import random
import string
from unicodedata import digit

#lists
lower_characters = [random.choice(string.ascii_lowercase) for i in range(3)]
lower_characters2 = [random.choice(string.ascii_lowercase) for i in range(4)]
upper_characters = [random.choice(string.ascii_uppercase) for i in range(random.randint(2,6))]
digits = [random.choice(string.digits)for i in range(random.randint(4,7))]
symbols = [random.choice(string.punctuation)for i in range(3)]

#variables

randomize_LC_UC1 = lower_characters2 + upper_characters + digits + symbols
random.shuffle(randomize_LC_UC1)
randomize_LC_UC = lower_characters+randomize_LC_UC1
if len(randomize_LC_UC) <24:
	aantal = len(randomize_LC_UC) - 24
	for i in range(abs(aantal)):
		randomize_LC_UC.append(random.choice(string.ascii_lowercase))
#print execute
print(''.join (randomize_LC_UC))
print('test:',len( ''.join(randomize_LC_UC)))







