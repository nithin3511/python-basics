n=int(input())

for n in range(2,n+1):
   isprime=True
   for i in range(2,int(n**0.5)+1):
       if n%i==0:
         isprime=False
         break
   if isprime:
      print(n)
