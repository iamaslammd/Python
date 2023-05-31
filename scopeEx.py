########Scope Example########
# enemies = 1
# def increase_enimies():
#     enemies = 2
#     print(f"Enemies inside functon: {enemies}")

# increase_enimies()
# print(f"Enemies outside function: {enemies}")

# ###Local scope###
# def local_fun():
#     var = 2
#     print(var)
# local_fun()
# # print(var) here you get cause the var(Scope) is defined inside funtion

# ###Global Scope###
# var2 = 10 #This is a global scope it can use inside and outsind the function
# def global_fun():
#     var3 =  7 ## This is the local var can only be used inside the function
#     print(var2)
#     print(var3)
# print(var2)
# global_fun()

# ### There is no Block space in python ###
# variable = 3
# fruits = ["Appple","Banana", "Orange"]
# if variable <5:
#     new_fruit = fruits[0]
# print(new_fruit)

# variable2 = 2
# def fruits_():
#     fruits = ["Appple","Banana", "Orange"]
#     if variable2 <5:
#      new_fruit2 = fruits[0]
#      print(new_fruit2)## This is valid as it is inside the function 
# #print(new_fruit2)## Now this gives error as it is outside the function

# ### Modifing a global Scope ###
# #vegitables = 3## Global Scope
# #def  increase_vegitables():
#  #   global vegitables ## This takes the global variable which is defined outside the function so that we could use global scope and modify it inside the function
#   #  vegitables += 7
#    # print(f"Vegitbles inside funtion:{vegitables}")
# #increase_vegitables()
# #print(f"Vegitbles outside funtion:{vegitables}")
# # This method is bug prone so it is not recommended to use often

# # Instead we use return
# vegitables = 3
# def  increase_vegitables():
#     print(f"Vegitbles inside funtion:{vegitables}")
#     return vegitables + 2
# vegitables =  increase_vegitables()
# print(f"Vegitbles outside funtion:{vegitables}")

#### Global Constants ####
pi = 3.14159