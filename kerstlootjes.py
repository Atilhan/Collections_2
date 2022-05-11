import random

insert_names = True
tickets = []

while insert_names:
    name =str(input("Insert your names here. Type: 'Stop' when you're finished: "))
    if name == "Stop":
        insert_names = False
    else:
        tickets.append(name) 

def ticket_lottery():
    name_control = []
    name_controle_2 = []
    control = True
    while control:
        ticket_1 = random.choice(tickets)
        ticket_2 = random.choice(tickets)
        straw_pull_1 = ticket_1
        straw_pull_2 = ticket_2
        loot = straw_pull_1, straw_pull_2
        
        if straw_pull_1 in name_control or straw_pull_2 in name_controle_2:
            pass
        elif ticket_1 != ticket_2:
            print(loot)
            name_control.append(straw_pull_1)
            name_controle_2.append(straw_pull_2)
            if name_control == loot:
                control = False
            else:
                pass

ticket_lottery()