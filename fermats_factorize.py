#get it from CTF2015 Weak RSA
#use to split q and p
#from https://github.com/ctfs/write-ups-2015/tree/master/pragyan-ctf-2015/crypto/weak_rsa
import math
import gmpy2

N=gmpy2.mpz(E8953849F11E932E9127AF35E1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000051F8EB7D0556E09FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBAD55)

gmpy2.get_context().precision=2048
a=int(gmpy2.sqrt(n))

a2=a*a
b2=gmpy2.sub(a2,N)

while not(gmpy2.is_square(b2)):
    a=a+1
    b2=a*a-N

b2=gmpy2.mpz(b2)
gmpy2.get_context().precision=2048
b=int(gmpy2.sqrt(b2))

print a+b

print a-b

