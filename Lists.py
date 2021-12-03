#nimed=["Anna","Inna"]#список
#for i in range(3):#цикл 3 раза спрашивать у пользователя
#	nimi=input("Sisesta nimi => ")
#	nimed.append(nimi)#добавление в список имя
#print(nimed)
#nimed.sort(reverse=True)#сортирует список и разворачивает список
#print(nimed)
#nimed.sort()#сортирует список
#print(nimed)
#nimed.insert(1,input("Sisesta veel nimi => "))#куда добавить это имя
#print(nimed)
#nimed.remove("Anna")#удаление имя
#print(nimed)
#nimed.pop(2)#удаление второго
#print()
#print(len(nimed))
#nimed.count(nimed[0])
#print(nimed)
#Maakonnad=["Tallinn","Narva", "Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa", "Lääne-Virumaa", "Jõgevamaa","Tartu linn","Tartumaa", "Põlvamaa", "Võrumaa", "Valgamaa","Viljandimaa", "Järvamaa", "Harjumaa", "Raplamaa","Pärnumaa","Läänemaa", "Hiiumaa", "Saaremaa"]
#while 1:
#	try:
#		index=int(input("Index =>"))
#		if 10000<=index<=99999:
#			break
#	except ValueError:
#		print("Vale index!")
#index_1=index//10000
#print(Maakonnad[index_1-1])
#if index_1 in [1,2,3]:
#	print("Оставайтесь дома!")
#else:
#	print("Носите маски!")
#from random import*
#sps=[]
#N=randint(4,30)
#for i in range(N):
#	sps.append(randint(-50,50))
#print(sps)
#while 1:
#	try:
#		k=int(input("Mis positsioonist alustada vahetus => "))
#		if k<=N//2:
#			break
#	except ValueError:
#		print("Arv peab olema väiksem kui",N//2)
#k-=1
#for i in range(k,-1,-1):#k....0
#	print(sps[i],end="<->")
#	print(sps[N-i-1])
#	a=sps.pop(i)
#	sps.insert(N-i-1-1,a)
#	a=sps.pop(N-i-1)
#	sps.insert(i,a)
#print(sps)
#from random import*
#sps=[]
#N=randint(4,30)
#for i in range(N):
#	sps.append(randint(-50,50))
#print(sps)
#max=-50
#for element in sps:
#	if element>max: max=element
#new_max=max/len(sps)#N
#ind=sps.index(max)
#sps.remove(max)
#sps.insert(ind,new_max)
#print(sps)
#from random import*
#sps=[]
#for i in sps:
#	sps.append(abs(i))
#print(sps.sort())
#print(sps.sort(reverse=True))
#print()
#l=['крот', 'белка', 'выхухоль']
#nl=[]
#max=0
#for e in l:
#	x=len(e)
#	if x>max:
#		max=x
#for e in l:
#	nl.append(e.ljust(max,"_"))
#print(nl)
#s1=['крот', 'белка', 'выхухоль']
#s2=['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
#s3=['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
#ss=[s1,s2,s3]
#N=0
#while N<len(ss):
#	print(ss[N])
#	max=0
#	Sn_=[]
#	for s in ss[N]:
#		pikkus=len(s)
#		if pikkus>max: max=pikkus
#	for s in ss[N]:
#		Sn_.append(s.ljust(max,"_"))
#	print(Sn_)
#	N+=1
glas="aeiou"
cogl="bcdfghjklmpqrstwxyz"
a=[]
b=[]
abc=[]
while 1:
	try:
		nimi=str(input("Sisestage oma nimi =>"))
		break
	except ValueError:
		print("Ainult kirju!")
print()
print("Welcome!",nimi.title())
print()
#nimi.isalpha()
#nimi.split(" ")
for i in nimi:
	if i in glas:
		a.append(i)
print("Vokaalid => ",len(a))
for e in nimi:
	if e in cogl:
		b.append(e)
print("Kaashäälikud => ",len(b))
print()
abc=list(nimi.lower())
uksikud=[x for x in abc if abc.count(x)>=1]
uksikud=list(set(uksikud))
print(uksikud)
n=["A"," E"," I"," O", "U"]
l=["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S"," T", "V", "W", "X"," Y", "Z"]
