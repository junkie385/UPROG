# Napišite program koji unosi broj n. Ako je n paran ispisuje se ''trokut'' od znakova ''x'' a ako je 
# neparan ''trokut'' je od znakova ''*''. 


unosBroj = int(input('Koliko redaka ce imati "trokut": '))

if(unosBroj % 2 == 0):
    for i in range(1, unosBroj + 1):
        for j in range (i):
            print("x", end = "")
        print()
else:
    for i in range(1, unosBroj + 1):
        for j in range (i):
            print("*", end = "")
        print()