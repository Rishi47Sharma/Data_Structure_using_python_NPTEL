def dcf(m,n):
  i = min(m,n)
  while i>0:
   if(m%i==0 and n%i==0):
     return(i)
   else:
     i-=1
 print(dcf(49,40))
