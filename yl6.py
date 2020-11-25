m =int(input("sisestage esimene arv: "))
n =int(input("sisestage teine arv: "))
o =int(input("sisestage kolmas arv: "))
if m < n and o < n :
    print(n)
elif o < m and n < m:
    print(m)
else:
    print(o)
