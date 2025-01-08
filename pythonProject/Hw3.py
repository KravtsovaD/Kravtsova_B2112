#https://itstepedu-my.sharepoint.com/:u:/g/personal/kravtsova_d_student_itstep_org/Ebz8W_-vPvlHld1xcTEohuEBmC0lp6eGMuiJszN8_cnxqw?e=KvJS8y

#1023

x,y = map(float,input().split())
if x<0 and y>0:
 print('Yes')
else:
 print('No')

#1024

x,y = map(int,input().split())
if x>0 and y>0:
 print(1)
elif x<0 and y>0:
 print(2)
elif x<0 and y<0:
 print(3)
elif x>0 and y<0:
 print(4)

# #1025

x,y,z = map(int,input().split())
if x+y>z and y+z>x and x+z>y:
 print('Yes')
else:
 print('No')

# #1026

a,b,c,d=map(int,input().split())
if a<b<c<d:
 print('Yes')
else:
 print('No')

#1027

num = int(input())
a = num //1000
b = num //100 %10
c = num //10 %10
d = num %10
print(max(a,b,c,d))

#1028

N=input()
sq = int(N)**2
cube = (int(N[0])+int(N[1]))**3

diff = abs(int(N[0])-int(N[1]))
suma = int(N[0])+int(N[1])
if sq==cube:
    print(suma)
else:
    print(diff)
