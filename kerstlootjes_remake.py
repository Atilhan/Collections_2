#import random  #importeert de mogelijkheid om iets te randomizen.

# namen = True
# loten = []

# while namen:
#     namen_aanvragen = str(input("Vul de gewenste namen hier | type : 'stop' als je geen namen wilt toevoegen."))
#     loten.append(namen_aanvragen)

#     if namen_aanvragen.lower() == "stop":
#         namen = False
#         del loten[-1]
#         print(loten)
#     else:
#         dubbel = any(loten.count(similar) > 1 for similar in loten) #Any zorgt ervoor dat de bool returned word als het True is & count telt / controleert of de waardes het zelfde zijn in een lijst.

#         if dubbel == True:
#             del loten[-1] #Verwijderd de laatste value dat je hebt ingetyped van de list als er meerdere tegelijk op True zijn.

#         else:
#             loten.append(namen_aanvragen) # Als er niets duplicated is worden ze aan de lijst toegevoegd.

import random
active = True
loten = []

# def namen_vragen(loten_lijst):
#     namen_invoeren = input('Insert your names here, type stop if youre finished. ')
#     if not namen_invoeren in loten_lijst:
#         loten_lijst.append(namen_invoeren)
#         loten_lijst.split()
#     return loten_lijst

participants = [[]]

def get_participants(participant_list):
    while True:
        name = input("Enter participant name (enter 'next' to go to next pair of participants): ")
        if name in participant_list[-1]:
            print("This name has been added already, retry with another name!")
            continue
        if name == "next":
            participant_list.append([])
            break
        participant_list[-1].append(name)

while True:
    get_participants(participants)
    print(participants)
def tickets():
    None

while True:
    insert_participants(participants)
    print(participants)
# while active:
#     print(namen_vragen(loten))

print(insert_participants((participants)))



        

    
        




    


