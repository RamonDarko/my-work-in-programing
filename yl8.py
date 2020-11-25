n =int(input("sisestage aasta: "))
if n%4==0 and n%100!=0 or n%400==0:
    print("jah on liigaasta")
else: 
    print("pole liig aasta")