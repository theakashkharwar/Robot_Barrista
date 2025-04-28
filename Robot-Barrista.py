#-----------------------------------------------------------------------------------Let's a Build a robot barista---------------------------------------------------------------------

print("\n\n---------------------------------------------Hello Welcome to our Barista!!!!!!!!!!!!!!------------------------------------------------\n\n\n\n")

# ----------------------------------------------------------------------------------------Detail of Customer-----------------------------------------------------------------------------------


# Using if else statements to to check, the identity of the customer 

# Checking If : They are Ben, Patricia, or Loki.
#               Are they Evil or not??
#               How Many good deeds they have done today.

name = (input("What is your Name?\n"))
if name == "Ben" or name == "Patricia" or name == "Loki":

    Ques = input("Are You Evil????\n")
    Heroism = int(input("\nHow many good deeds have u done today?? It would be really nice if u tell us\n")) 

    if Ques == "Yes" and Heroism < 4:
        print("\nYou'r Not welcom here " + name + "!!!!!!!!!!!!!!!!!!!!!!!")
    else: 
        print("\nYou'r Welcome here " + name + ". You are doing a great job we are Proud of You.\n")




# Checking: How long is their beard as people with long beard are our priority customers.

Ques1 = input("\nDo you have beard???\n")
Ques2 = input("\nIs your beard length more than 1 inch???\n")

if Ques1 == "Yes":
    if Ques2 == "Yes":
        print("\nYou can skip the Line and Go to the front, For your order!!!!\n")
else: 
    print("You Have to wait in the line as a regular customer\n\n\n")
         
    


#  -------------------------------------------------------------------------------Greetings and asking for order-----------------------------------------------------------------------


# CONCEPT :- Variables = its the data that changes according to user, situation etc. that is its not a constant data stored in memory, instead we create particular space in the memory for the information user have to share, for that we use varibales

print("-----------------------------------------------------At the Counter-------------------------------------------------------------------\n\n\n")
print("Welcome To Our Barrista " + name +", We are happy to have you with us.\n")


menu = "Coffee\nLatte\nChai\nVenti\n"

menu = menu + "Frappuccino"

order = input("Here's the menu: \n" + menu + "\nWhat would u like to order??\n")

# Using elif statements for differents order and different price


if order == "Coffee":
    price = 15

elif order == "Latte":
    price = 20
    Extras = input("Do you want whipped cream??\n")
    if Extras == "Yes":
        price = 23

elif order == "Chai":
    price = 10

elif order == "Venti":
    price = 25

elif order == "Frappuccino":
    price = 40
else:
    print("Sorry, We don't have that in here")
    exit()


print("How many cups do you want Sir??")
cups = int(input())
print("Here's your '" + order + "' Thank you for ordering.")
# result = price 
print("Your total charge is q",price * cups)