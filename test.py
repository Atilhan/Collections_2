# import turtle
# import colorsys
# # t = turtle.Turtle()
# # s = turtle.Screen()
# # s.bgcolor("black")
# # t.speed(0)
# # n=36
# # h=0
# # for i in range(460):
# #     c=colorsys.hsv_to_rgb(h,1,0.9)
# #     h+=1/n
# #     t.color(c)
# #     t.left(145)
# #     for j in range(5):
# #         t.forward(300)
# #         t.left(150)


# blue = ['2-', "", "", "", "", "", "", "", "", ""]

# def position_list():
#     position_blue = int(input('What index in the list blue would you like to put a number in?'))
#     if blue[position_blue] == "":
#         value_blue = input('Enter value')
#         blue[position_blue] = value_blue
#     else:
#         print("Enes dit is allemaal jou schuld")
#         position_list()


# active = True
# while active:
#     position_list()
#     print(blue)  

# a = True
# b = False

# print(a or a and b and a)

# l = ["a","b","c","d"]

# result = ''.join(l)

# print(result)

# x = 0
# while x <= 18:
#     print(x)
#     x += 7
    
# print(x)


# tables = input("Chose your table number")

# for i in range(1,11):
#     print(i,"x", tables, "=", i*tables)


# numbers = int(input('Insert table numbers !: '))
# for loop in range(1,11):
#     print(loop,"+", numbers, "=", loop*numbers)

# split = int(input('Insert numbers here !: '))
# for loop_1 in range(1,11):
#     print(loop_1, "/", split, "=", loop_1/split)

# import pyautogui,time,mouse


# # for i in range(10):
# #     time.sleep(2)
# #     pyautogui.leftClick()


# mouse.get_position()
# # mouse.drag(0,0,100,100,duration = 0.9)
# mouse.move(100,100,absolute = False,duration = 0.8)
# mouse.click('left')



import re

vowels = 'aeiouAEIOU'

given_str = input("Enter a string : ")
final_str = given_str

for c in given_str:
    if c in vowels:
        final_str = final_str.replace(c,"")

print(final_str)
