catNames=[]
while True:
    print('enter the cat¡¯s name'+str(len(catNames)+1)+';')
    name=input()
    if name=='':
        break
    catNames=catNames+[name]
print('the cats name are;')
for name in catNames:
    print(name)