#Đề bài: Viết chương trình nhập vào 2 số thực và một ký tự phép toán (+, -, *, /).
a = int(input("Nhập số a: "))
b = int(input ("nhập số b: "))
phep = input("nhập kí tự: ")
if phep == "/" :
    if b == 0 :
        print ("Fail")
    else:
        print(f"kêt quả của bạn là:{a/b}")
elif phep == "+" :
    print(f"kết quả của bạn là:{a+b}")
elif phep == "-" :
    print(f"kết quả của bạn là:{a-b}")
elif phep == "*":
    print(f"kết quả của bạn là:{a*b}")
else:
    print("FAIL")