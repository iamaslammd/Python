mon = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',}
stud = {'Kiran':23,'Kumar':20,'Dinesh':19,'Rakesh':21}

print("mon Dictionary is ",str(mon))
print("The element in the key position 3 is: ",mon[3])
print("The mon dictionary values are: ",mon.values())
print("The mon dictionary keys are: ",mon.keys())

print("Before addition")

for item in mon.values():
	print(item,end = '')
mon[7] = 'july'
print()
print("After addition")
for item in mon.values():
	print(item,end = '')
print()
print("Before Deletion")
for item in stud.values():
	print(item,end = '')
print()
del stud['Kumar']

print("After deletion")
for item in stud.values():
	print(item,end = '')
print("Before change")
print("stud Dictionary is",str(stud))
stud['Dinesh']=55
print("Before change")
print("stud Dictionary is",str(stud))

print("Key value pair of dictionary")
print(stud.items())
