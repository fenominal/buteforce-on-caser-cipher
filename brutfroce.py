def decryption(ct,key):
 cflist = list(ct) #take  text  string in to list
 pt = " "
 for i in cflist:
     asc = ord(i)
     asc = asc - (key % 26)
     if i.isupper():# chek uper case
         if asc <65:
             asc = asc + 26
     elif i.islower():#chek lower case
             if asc < 97:
                 asc = asc + 26
     newch = chr(asc)
     pt = pt + newch
 return pt


cf = input("Enter any text:- ")
print("------print all possible key----")
for key in range(1,27):
 
 pt = decryption(cf,key)
 print ("encrypt text: %s key = %d"%(pt,key)) #brute force all key value
