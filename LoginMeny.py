# Loginmeny
# Skelettkod till uppgiften
import webbrowser
import random

def random_yt_url():
    bas64 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'
    url_end =''
    for i in range(11):
        url_end += bas64[random.randint(0,63)]
    print("https://www.youtube.com/watch?v="+url_end)
    return "https://www.youtube.com/watch?v="+url_end



lista = ['https://www.youtube.com/watch?v=3LmmCYxe5k0','https://www.youtube.com/watch?v=D9Sv4XHWc7o','https://www.youtube.com/watch?v=WOdTUOeDAtY','https://www.youtube.com/watch?v=jE2Tp67OlVo']

accounts = {}
logged_in = False

while True:
    menyval = input(
        "\n1. Skapa konto\n"
        "2. Logga in\n"
        "3. Kolla på en rolig video\n"
        "4. Logga ut\n"
        "5. Avsluta program\n"
    )

    if menyval == "1":
        username = input("\nWhat is your USERNAME?:")
        if username in accounts:
            print("User Already Exists")
        else:
            accounts[username]= input("What is your PASSWORD?:")
        
        
        # TODO Skapa ett konto genom att lägga till ett key-value par i accounts
        # username = key, password = value
        # Bonus: Kolla först så att användaren inte redan finns
        
    
    elif menyval == "2":
        if not logged_in:
            for i in range(3):
                print("\nLogin Attempt:", i+1)
                username = input("\nEnter Username:")
                if username in accounts:
                    password = input("Enter Password:")
                    if accounts[username]==password:
                        logged_in = True
                        print("\nLogin Succesful!!")
                        break
                    else:
                        print("INCORRECT PASSWORD!\n")
                else:
                    print("INCORRECT USERNAME!\n")
            else:
                print("LOGIN FAILED")
        else:
            print("You're Already Logged In\n")
       
        # TODO Användaren ska få logga in med username och password
        # Ändra variabeln logged_in till True om de lyckas logga in
        # Bonus: Ge användaren ett visst antal försök att logga in
        

    elif menyval == "3":
        # TODO skriv ut en rolig historia, men bara om användaren är inloggad
        # Bonus: Skriv ut en tråkig historia om de inte är inloggade
        if logged_in:
            webbrowser.open(random.choice(lista))
        else:
            webbrowser.open(random_yt_url())
    elif menyval == "4":
        if logged_in:
            c = input("Do you want to log out? (y/n):")
            if c == 'y':
                logged_in = False
                print("Logged out")
            # TODO Ändra variabeln logged_in till False
            # Bonus: Fråga om de är säkra först
        else:
            print("You're not logged in")

    elif menyval == "5":
        break