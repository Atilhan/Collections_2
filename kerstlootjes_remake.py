import random  #importeert de mogelijkheid om iets te randomizen.

namen = True
loten = []

while namen:
    namen_aanvragen = str(input("Vul de gewenste namen hier | type : 'stop' als je geen namen wilt toevoegen."))
    #loten.append(namen_aanvragen)

    if namen_aanvragen.lower() == "stop":
        del loten [-1]
        print(loten) 
        namen = False


    else:
        dubbel = any(loten.count(similar) > 1 for similar in loten) 

        if dubbel == True:
            del loten[-1]

        else:
            loten.append(namen_aanvragen)





    


