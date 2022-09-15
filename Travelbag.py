
# Travelbag
# Skelettkod till uppgiften

travelbag = []

while True:
   menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program\n")

   if menyval == "1":

       print(*travelbag)

   elif menyval == "2":
       ny_sak = input("Lägg till något:")
       travelbag.append(ny_sak)

   elif menyval == "3":
       tabort = input("Ta bort:")
       travelbag.remove(tabort)

   elif menyval == "4":
       break