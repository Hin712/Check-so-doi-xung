"""

  Ý tưởng:
    - Nhập n, ép kiểu thành số nguyên
    - Khai báo hàm kiểm tra số đối xứng trong Pyt>
    - Nếu flag = 1, số vừa nhập là số đối xứng, f>

"""
def symmetrical_num(n):

    flag =0;
    if ( n[::-1] == n):
      flag = 1
    return flag

n = input("Nhap mot so tu nhien: ")
check = symmetrical_num(n);

if check == 1:
    print(n,"la so doi xung")
else:
    print(n,"khong phai la so doi xung")
