from random import randint 

player = 0
#x = [0, 2, 4, 6, 8]

val = 0 

hand = []
kort = 0
TYP  = 0
svit = 0

print("Hej och välkommen till mitt finns i sjön")
print("har du kort x sant får kort falskt kort ur sjön")
print("väjl val A : A")
print("välj val B : ♥")
print("välj val C : ♦")
print("välj val D : ♣")

    while kort != 100:
        
     if typ = "1": 
     svit  = "A"
     elif typ = "2": 
     svit  = "♥"
     elif typ = "3": 
     svit  = "♦"
     elif typ = "4": 
     svit  = "♣"
     else: 
        typ = 0 
        svit = ""

    kort = int(input("skriv in ett kort:"))
    hand.append(kort)

fort  k in hand:
    PRINT(k)
thislist.append(1,4)


while typ < 1 or typ > 4:
    typ = int(intput("vilken typ av kort,4 ♥ ♦ ♣"))
    kor = int(input("skriv in ett kort"))


while val !=14 or lek <= 52:
    lek = lek + 1
    player = randint(0,14)
    ai = randint(0,14)
    val = int(input("välj ditt val 0-14"))

    if val == ai:
        print("du gissade rätt ta kort från motståndaren")
    else: 
        print("du gissade fel ta upp ett kort från sjön")