import random


def intro():
    print('-----------------------------------------------------------------------')
    print('                      Welcome to Dobbel Trobbel                        ')
  
def scoreboard():
    print('-----------------------------------------------------------------------')
    print('Position: |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |')
    print('-----------------------------------------------------------------------')


def dobbelstenen():
    blauw_dobbelsteen = random.randint(1,6)
    rood_dobbelsteen = random.randint(1,6)
    #list shuffled #wit dobbelsteen
    witte_dobbelsteen_list = [1,1,1,2,2,3]
    wit_dobbelsteen = random.choice(witte_dobbelsteen_list)
    return (blauw_dobbelsteen,rood_dobbelsteen,wit_dobbelsteen)


def berekening():
    optie_1 = blauw + rood + wit
    optie_2 = blauw + rood - wit
    optie_3 = blauw + rood
    return (optie_1,optie_2,optie_3)
    vraag_1 = input("Kies uit : | A | B | C | D |")


active = True
while active:
    intro()
    scoreboard()
    blauw,rood,wit = dobbelstenen()
    uitkomst_1,uitkomst_2,uitkomst_3 = berekening()
    print("\n","Blauw 🎲:",blauw,"\n","Rood  🎲:",rood,"\n","Wit   🎲:",wit,"\n")
    print("A: ","【🔵 】",blauw,"+","【🔴 】",rood,"+","【⚪ 】",wit,"=", uitkomst_1)
    print("B: ","【🔵 】",blauw,"+","【🔴 】",rood,"-","【⚪ 】",wit,"=", uitkomst_2)
    print("C: ","【🔵 】",blauw,"+","【🔴 】",rood,"=", uitkomst_3)
    active = False
#function execute


