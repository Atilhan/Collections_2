# shopping_list = {} #dict

# #function shoppinglist
# def shopping_list():
#     wish_list = input('What would you like to order on your shopping list? (type terminate to stop the exercise)')

#     if wish_list == 'terminate':
#         print (shopping_list)

#     else:
#         pass

#-------

def shopping_list():
    shopping = True
    question = {} #dict
    while shopping:
        wish_list = input('What would you like to order on your shopping list? (type terminate to stop the exercise)')
        if wish_list == "terminate":
            shopping = False

        elif not wish_list in question:
            question[wish_list] = 1

        else:
            question[wish_list] += 1

    return question
print(shopping_list())

    


