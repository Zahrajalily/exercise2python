#اشتراک گیری بین دوتا لیست 
vollyball = [ "zahra" ,"shahin" ,"maryam" ,"maral" ,"farid" ,"mohsen" ,"nafas" ]
fitness = [ "zahra" ,"maral" ,"faranak" ,"nahid" ,"shiva" ,"nazanin" ,"nafas" ,"ali" ]
same=[]
for v in vollyball :
   for f in fitness:
    if v == f:
      same.append(v)

print(same)
