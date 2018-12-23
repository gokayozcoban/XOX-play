playboard = [["___","___","___"],
             ["___","___","___"],
             ["___","___","___"]]
print("\n"*1)
for i in playboard:
    print("\t".expandtabs(30),*i,end="\n"*2)
    
kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]

X_durumu = []
o_durumu = []


sıra = 1
while True:
    if sıra %2 == 0:
        işaret = "X".center(3)
    else:
        işaret = "O".center(3)
    sıra += 1
    print()
    print("İŞARET: {}\n".format(işaret))
    
    x = input("yukarıdan aşağı [1,2,3]: ".ljust(30))
    if x == "q":
        break

    y = input("soldan sağa [1,2,3]: ".ljust(30))
    if y == "q":
        break
    x = int(x)-1
    y = int(y)-1



