s=input("Enter the string")
c=0
for i in s:
  if(i.isdigit() or i.isalpha()):
    continue
  else:
    c+=1
print(c)
