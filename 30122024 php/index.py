# print("nhap vao 1 so: \n ")
# inputStr = input()
# age = int(inputStr)
# print("so ban vua nhap la",age)
# if(age % 2 == 0):
#     print("so ban vua nhap la so chan")
# else:
#     print("so ban vua nhap la so le")

# a= float(input("canh a"))
# b= float(input("canh b"))
# c= float(input("canh c"))
# if(a>0 and b>0 and c>0):
#     if(a+b>c or a+c>b or b+c >a):
#         print("{a},{b},{c} la 3 canh cua tam giac")
#     else:
#         print("{a},{b},{c} ko phai la 3 canh cua tam giac")

# import time
# d = int(input("nhap nam sinh"))
# y = int(input("nhap tuoi"))
# x = time.localtime()
# year = x[0]
# e = year - d
# print("tuoi cua ban la ",e)
# j = y - year
# print("nam sinh cua ban la ",-j)

# n = int(input("nhap so "))
# if(n%2==0 and n%3 ==0):
#     print(f"{n} chia het cho 2,3")
# elif(n%2==0):
#     print(f"{n} chia het cho 2")
# elif(n%3 ==0):
#     print(f"{n} chia het cho 3")
# else:
#     print(f'{n} ko hop le ')
    

# import math
# a = float(input("Nhập hệ số a: "))
# b = float(input("Nhập hệ số b: "))
# c = float(input("Nhập hệ số c: "))
# if(a==0):
#     if(b==0):
#         if(c==0):
#             print("phuong trinh vo so nghiem")
#         else:
#             print("phuong trinh vo nghiem")
#     else:
#         x = -c/b
#         print(f"phuong trinh co nghiem duy nhat : x={x}")
# else:
#     delta = b**2-4*a*c
#     if (delta<0):
#         print(f"phuong trinh vo nghiem")
#     elif(delta==0):
#         x = -b / (2*a)
#         print(f"Phương trình có nghiệm kép: x = {x}")
#     else:
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")

# for i in range(80,101):
#     if i%2 ==0 and i%3==0:
#         print(i)

dem=1
while(dem<10):
    print("dang trong while",dem)
    dem = dem+1
    if (dem%2==0):
         break
else:
    print("dang o trong while")
print("dang o ngoi while")
 




    


    



