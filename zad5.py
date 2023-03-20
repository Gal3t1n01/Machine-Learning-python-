list = open("song.txt","rt")

broj = dict()

for line in list:
    reci=line.split()

for brreci in reci:
    if brreci not in broj:
        broj[brreci] = 1
    else:
        broj[brreci] +=1

print("Koliko reci se pojavljuju samo jednom",broj)

