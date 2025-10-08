# Simple Cryptarithmetic: SEND + MORE = MONEY
import itertools

letters = "SENDMORY"   # unique letters
for perm in itertools.permutations("0123456789", len(letters)):
    s,e,n,d,m,o,r,y = map(int, perm)
    if s==0 or m==0:  # no leading zero
        continue

    send  = 1000*s + 100*e + 10*n + d
    more  = 1000*m + 100*o + 10*r + e
    money = 10000*m + 1000*o + 100*n + 10*e + y

    if send + more == money:
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        break
