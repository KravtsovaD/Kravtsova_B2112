#1007

N = float(input())
res = int(N)*2
print(res)

#1008

P, K = map(float, input().split())
P_float= P-int(P)
res =round(P_float*K)
print(res)

#1009

a1, b1, a2, b2 = map(int, input().split())
S1 = a1*b1
S2 = a2*b2
S = abs(S1-S2)
print(S)

#1010

num = int(input())
dec = num//10
digit = num%10
res = dec*digit
print(res)

#1012

a = int(input())
a = a**3
print(a)



