#Đề bài: Viết chương trình nhập vào điểm số trung bình (thang điểm từ 0 đến 10) của một học sinh.
point = float(input("YOUR POINT: "))
if point > 10 or point < 0 :  
    print (" sai cú pháp điểm ")
elif 10>point > 9.0 :
    print("Xuất xắc")
elif 8.9> point > 8.0 :
    print("Giỏi")
elif 7.9> point>6.5 : 
    print(" Khá")
elif 6.4> point > 5 : 
    print("Trung bình")
else: 
    print("quá kém")