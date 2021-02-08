# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bs = 15 #  smallPizza
bm = 20 # mediuPizza
bl = 25 # LargePizza
bsp = 2 # small pepperoni
bop = 3 # Other pepperoni
bec = 1 # extra cheese

pizza = 0 #selected pizza prise
pepper = 0 #selected pepper prise
cheese = 0 #selected cheese prise

if  size == "S" :
  pizza = bs
elif size == "M" :
  pizza = bm
elif size == "L":
  pizza = bl
else:
  pizza = 0


if extra_cheese == "Y":
  cheese = bec
else :
  cheese = 0

if add_pepperoni == "Y" :
  if size == "S" :
    pepper = bsp
  elif size == "M" :
    pepper = bop
  elif size == "L" :
    pepper = bop
  else :
    pepper = 0
    
fbill = pizza + cheese + pepper

print(f"Welcome to Python Pizza Deliveries!\nYour final bill is: ${fbill}.\n' ")