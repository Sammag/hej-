# Program för att hitta summan av alla nummer som är lagrade i en lista

# Lista på nummer som man kan ändra 
numbers = [6, 5, 3, 8, 3, 2, 5, 4, 11,#]

# variabel för att lagra summan
summa = 0

# iterera över listan
for val in numbers:
	summa = summa+val

# summan 57
print("The sum is", summa)