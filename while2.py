name= input("Enter the name : ")
i=0
tcount = ""
while i< len(name):
    if name[i] not in tcount:
        tcount += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1