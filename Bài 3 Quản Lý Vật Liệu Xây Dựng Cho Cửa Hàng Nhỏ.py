class VatLieuTot:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

class ChucNang:
    def __init__(self):
        self.vatlieus = []
    
    def them_vat_lieu(self, vatlieu):
        self.vatlieus.append(vatlieu)
        print(f"Them vat lieu {vatlieu.name} thanh cong!")
        
    def hien_thi_danh_sach(self):
        if self.vatlieus:
            for vatlieu in self.vatlieus:
                print(f'{vatlieu.name} - Gia: {vatlieu.price}, So luong: {vatlieu.amount}')
        
    def tim_kiem_vat_lieu(self, name):
        found_vatlieu = [ vatlieu for vatlieu in self.vatlieus if vatlieu.name == name]
        if found_vatlieu:
            for vatlieu in found_vatlieu:
                print(f'Tim thay {vatlieu.name} - Gia: {vatlieu.price}, So luong: {vatlieu.amount}')
        else:
            print('khong tim thay vat lieu phu hop')
        
    def cap_nhat_ton_kho(self, name, price=None, amount=None):
        for vatlieu in self.vatlieus:
            if vatlieu.name == name:
                if price:
                    vatlieu.price = price
                if amount:
                    vatlieu.amount = amount
                print("Cap nhat thong tin vat lieu thanh cong!")
                return
        print("Khong tim thay vat lieu!")
            
        
        
    def xoa_vat_lieu(self, name):
        for vatlieu in self.vatlieus:
            if vatlieu.name == name:
                self.vatlieus.remove(vatlieu)
                print("Da xoa vat lieu!")
                return
        print("Khong tim thay vat lieu phu hop!")




def main():
    cn = ChucNang()
    while True:
        print('\n--- Menu ---')
        print('1. Them vat lieu moi')
        print('2. Hien thi danh sach vat lieu')
        print('3. Tim kiem vat lieu theo ten')
        print('4. Cap nhat so luong ton kho')
        print('5. Xoa vat lieu khoi danh sach')
        print('6. Thoat chuong trinh')
        
        luachon = int(input("Nhap lua chon cua ban: "))
        
        if luachon == 1:
            name = input("Ten vat lieu: ")
            price = input("Gia: ")
            amount = input("So luong ton kho: ")
            cn.them_vat_lieu(VatLieuTot(name, price, amount))

        elif luachon == 2:
            print("====== Danh sach vat lieu ======")
            cn.hien_thi_danh_sach()
            print("="*32)
        elif luachon == 3:
            name = input("Nhap ten vat lieu can tim: ")
            cn.tim_kiem_vat_lieu(name)
        elif luachon == 4:
            name = input("Nhap ten vat lieu can cap nhat: ")
            price = input("Nhap gia moi ")
            amount = input("Nhap so luong moi ")
            cn.cap_nhat_ton_kho(name,price,amount)
        elif luachon == 5:
            name = input("Nhap ten vat lieu can xoa: ")
            cn.xoa_vat_lieu(name)
        elif luachon == 6:
            print('Cam on ban da su dung chuong trinh!')
            break
        else:
            print("Lua chon khong hop le, vui long thu lai")
            
if __name__ == "__main__":
    main()