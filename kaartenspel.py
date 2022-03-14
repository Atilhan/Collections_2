import random 

colors = [
    'harten',
    'klaveren',
    'schoppen',
    'ruiten'
]

color_values = [2,3,4,5,6,7,8,9,10, 'vrouw' , 'heer', 'boer' , 'aas']

empty_list = []

for i in colors:
    for x in color_values:
        empty_list.append(i + " " + str(x))
random.shuffle(empty_list)

print(empty_list)

for e in range(1,8):
    index = random.randint(0,len(empty_list)-1)
    card = (empty_list.pop(index))
    print(f"Card {e}: {card}")
print("\n[DECK]",empty_list)



