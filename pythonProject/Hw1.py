#https://itstepedu-my.sharepoint.com/:u:/g/personal/kravtsova_d_student_itstep_org/EUkb5ejgc8BDjtkWL8jMP6ABgKGtQNGEa6i4qA6bvZvdag?e=4hIIgB

#1004

p = float(input())
round_num = round(p)
integer = int(p)
double = p-integer
print(round_num)
print(integer)
print(f"{p-integer:.1f}")

#1005

x, y = map(int, input().split())
res = x**3+((x+1)/(y**2+1))
print(f"{res:.1f}")

#1006

x, y = map(int, input().split())
print(x - y)