import random

talet = random.randint(1,100)

while True:
    gissning = int(input("Gissa talet:"))
    if gissning < talet <gissning +2:
        print("väldigt nära, lite till")
    elif gissning > talet >gissning -2:
        print("Väldigt nära, lite mindre")
    
    elif gissning < talet and (gissning <talet < gissning +10):
        print("Lite större")
    elif gissning >talet and (gissning >talet > gissning -10):
        print("Lite mindre")
    elif gissning < talet:
        print("Större")
    elif gissning > talet:
        print("Mindre")
    elif gissning == talet:
        print("rätt")
        talet = random.randint(1,100)
