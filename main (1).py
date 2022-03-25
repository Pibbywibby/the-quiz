
username = input("Enter Instagram user name:" )
autopnames = ["POOPTAILZ", "HUTAO.FOOTJOB", "LILSEXZ", "SEXTAILS"]

def pspam(username):
    i = 1
    while i < 72:
        print(username.upper() + " YOU ARE A PEDO")
        i += 1


if username.upper() in autopnames:
    pspam(username)
else:
    print("Hello,",username)


age = int(input("How old are you: "))

if age >= 30:
    pspam(username)
elif age >= 18 and age < 30:
    print("We will keep an eye on you")
else:
    print("watchout for pooptailz!!!")
    
    
has_joked = input("have you ever made a pedo joke [y]/[n]: ")

if has_joked.upper() == "Y":
    pspam(username)
elif has_joked.upper() == "N":
    print("Very good",username)
else:
    print("dumbass mf put a 'y' or a 'n'")
    has_joked = input("have you ever made a pedo joke [y]/[n]: ")


is_irony = input("Do you currently own an irony page [y]/[n]: ")

if is_irony.upper() == "Y" and age >= 18:
    pspam(username)
elif is_irony.upper() == "Y" and age < 18:
    print("You might turn out like pooptailz",username)
elif is_irony.upper() == "N":
    print("What a relief",username)
else:
    print("you retarded or something enter a 'y' for yes or a 'n' for no")
    is_irony = input("Do you currently own an irony page [y]/[n]: ")


the_blunt = input("Do you like kids [y]/[n]: ")

if the_blunt.upper() == "Y" and age >= 18:
    pspam(username)
elif the_blunt.upper() == "Y" and age < 18:
    print("since you are",str(age),"i will let it slide" )
elif the_blunt.upper() == "N" and has_joked == "Y":
    print("you are lying",username)
elif the_blunt.upper() == "N" and has_joked == "N":
    print("What a relief",username)
else:
    print("are you braindead type 'y' for yes or 'n' for no")
    the_blunt = input("Do you like kids [y]/[n]")
    

print("You finished the quiz",username)