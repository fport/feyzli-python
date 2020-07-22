#print(*"Galatasaray",)              
#print(*"FenerBahahce",sep=".")
#
#sayilar = [x for x in range(1,100) if x % 5 == 0]
#print(sayilar)
#print(*sayilar )

def goster(*args):
    for i in args:
        print(i)

#goster(1,2,3,4,5,6)
goster(*[1,2,3,4,5,6])  