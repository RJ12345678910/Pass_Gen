import random
import os
# Define each letter using a list of strings
P = [
    "P$P$P ",
    "P   P ",
    "P$P$P ",
    "P     ",
    "P     "
]

A = [
    "A$A$A ",
    "A   A ",
    "A$A$A ",
    "A   A ",
    "A   A "
]

S = [
    "S$S$S ",
    "S     ",
    "S$S$S ",
    "    S ",
    "S$S$S "
]

G = [
    "G$G$G ",
    "G     ",
    "G  GG ",
    "G   G ",
    "G$G$G "
]

E = [
    "E$E$E ",
    "E     ",
    "E$E$E ",
    "E     ",
    "E$E$E "
]

N = [
    "N$N$N ",
    "N   N ",
    "N N N ",
    "N   N ",
    "N   N "
]

# Combine each line from the letters
for i in range(5):
    print(P[i] + A[i] + S[i] + S[i] + "-" + G[i] + E[i] + N[i])


CHARS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nums = ["1","2","3","4","5","6","7","8","9","0"]
sp_chars = ["!","@","#","$","%","^","&","*","(",")","-","_","+"]
all_Chars = CHARS + chars + nums + sp_chars

print("\nWelcome to the Pass-Gen here you'll be able to generate strong random passwords for your personal or temprory use...")

leng = int(input("\nFirst suggest the length of your password..."))

if leng < 50:
    print("Valid Length...")
    passw = ''.join(random.choice(all_Chars) for __ in range(leng))
    option1 = input("Would you like to make a list to save multiple passwords...? (y/n)")
    option2 = input("Have you ever saved your passwords using Pass-Gen before on this device...? (y/n)")
    dirPath = "C:/Users/HRISHIKESH/OneDrive/Documents/Passwords/" #Paste the path where you want your passwords directory to exist...

    if option1 == "y":
        if option2 == "n":
            Usrname = input("Enter your name: ")
            appName = input("For which application/website this password will be used for: ")
            AppName = appName.upper()

            try:
                os.makedirs(dirPath)
                filepath = f"C:/Users/HRISHIKESH/OneDrive/Documents/Passwords/{Usrname}"

                content = f"{AppName} : {passw}"
                with open(filepath, "w", encoding= "utf-8") as file:
                    file.write(content)
            except FileExistsError:
                print(f"You have used Pass-Gen before on this device perhaps you forgot? Here's the location of your Passwords folder: {dirPath}")

            except Exception as e:
                print("There was an error Creating your Passwords folder... ",e)

            print(passw)

        elif option2 == "y":
            Usrname = input("Enter your name: ")
            appName = input("For which application/website this password will be used for: ")
            AppName = appName.upper()
            filepath = dirPath+Usrname

            content = f"\n{AppName} : {passw}"
            with open(filepath, "a", encoding= "utf-8") as file:
                file.write(content)

            print(passw)
        
        else:
            print("Invalid input...")
            print("Here's your password: ", passw)
    
    elif option1 == "n":
        print("Here is your Randomly Generated Password...: ", passw)

    else:
        print("Invalid input...")
        print("Here is your Randomly Generated Password...: ", passw)
        

else:
    print("Invalid Length entered should be less than 50.")

