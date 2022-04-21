import random

blauw_b =[-2,"","","","","","","","",""]
rood_r  =["","","","","","","","","",-2]
wit_w   =["","","","",""]

def intro():
    print('-----------------------------------------------------------------------')
    print('                      Welcome to Dobbel Trobbel                        ')
  
def scoreboard():
    print('-----------------------------------------------------------------------')
    print('Position: |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |')
    print('-----------------------------------------------------------------------')
    print("Blauw Lijst:", blauw_b)
    print("Rood Lijst :", rood_r)
    print("Wit lijst  :", wit_w)

def dobbelstenen():
    blauw_dobbelsteen = random.randint(1,6)
    rood_dobbelsteen = random.randint(1,6)
    witte_dobbelsteen_list = [1,1,1,2,2,3]
    wit_dobbelsteen = random.choice(witte_dobbelsteen_list)
    return (blauw_dobbelsteen,rood_dobbelsteen,wit_dobbelsteen)


def berekening(blauw_b,rood_r,wit_w):
    optie_1 = blauw_b + rood_r + wit_w
    optie_2 = blauw_b + rood_r - wit_w
    optie_3 = blauw_b + rood_r
    optie_4 = optie_1 - optie_2
    return (optie_1,optie_2,optie_3,optie_4)

def keuzen():
    keuzenlijst = ["A","B","C","D"]
    keuze = input("kies. A | B | C | D | : ").upper()
    index = keuzenlijst.index(keuze)
    return index

def lijst_kleur(blauw,rood):
    if blauw < rood:
        return "Rood"
    elif rood < blauw:
        return "Blauw"
    keuzen = input("In welke lijst wil je het hebben? Rood / Blauw:? ").lower()
    return keuzen 

def position_lijst(lijst_kleur,index_1):
    if lijst_kleur == "blauw":
        positie = int(input('in welke index van de lijst wil je het hebben.'))
        if blauw_b[positie -1] == "":
           blauw_b[positie -1] = uitkomsten[index_1]
        #    checkingtheindex(blauw_b,positie,uitkomsten[index_1])

    elif lijst_kleur == "rood":
        positie = int(input('in welke index van de lijst wil je het hebben.'))
        if rood_r[positie -1] == "":
           rood_r[positie -1] = uitkomsten[index_1]
        #    checkingtheindex(rood_r,positie,uitkomsten[index_1])
        
        else:
            print("er zit al een waarde in de index.")
            position_lijst(lijst_kleur,index_1)
            
# def checkingtheindex(lijst,index_2,nummer):
#     teller_1 = 1
#     teller_2 = 1
#     while True:
#         if len(lijst) > index_2 + teller_1 and lijst[index_2 + teller_1] =="":
#             teller_1 +=1
#         elif len(lijst) == index_2+teller_1 or lijst [index_2 + teller_1] > nummer:
#             if lijst[index_2 - teller_2] == "":
#                 teller_2 +=1
#             elif lijst[index_2 - teller_2] < nummer:
#                 return True
#             else:
#                 print("dat niet mogelijk")
#                 return False          
#         else:
#             print("dat niet mogelijk")
#             return False
        

#whileloop
active = True
position_w = 0
while active:
    intro()
    scoreboard()
    blauw,rood,wit = dobbelstenen()
    uitkomsten = berekening(blauw,rood,wit)
    print("\n","Blauw 🎲:",blauw,"\n","Rood  🎲:",rood,"\n","Wit   🎲:",wit,"\n")
    print("A: ","【🔵 】",blauw,"+","【🔴 】",rood,"+","【⚪ 】",wit,"=", uitkomsten[0])
    print("B: ","【🔵 】",blauw,"+","【🔴 】",rood,"-","【⚪ 】",wit,"=", uitkomsten[1])
    print("C: ","【🔵 】",blauw,"+","【🔴 】",rood,"=", uitkomsten[2])
    minimun = min(blauw,rood,wit)
    maximum = max(blauw,rood,wit)
    totaal = (maximum - minimun)
    print ("D", maximum, "-", minimun, "=", totaal)
    gekozen_nummer = keuzen()
    uitkomsten[gekozen_nummer]
    gekozen_lijst = lijst_kleur(blauw,rood)
    position = position_lijst(gekozen_lijst,gekozen_nummer)
    if gekozen_nummer == 2 or gekozen_nummer == 3:
        wit_w[position_w] = wit
        position+=1

        
    # checkingtheindex(gekozen_lijst,gekozen_nummer,uitkomsten[gekozen_nummer])
    # index = keuzen()
    # uitkomsten[index]
    # keuzen_lijst = lijst_kleur(blauw,rood)
    # active = False



#function execute


