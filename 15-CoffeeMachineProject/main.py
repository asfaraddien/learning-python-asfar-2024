from bahan import MENU, resources



def cek_bahan(cek):
    for i in cek:
        if cek[i] > resources[i]:
            return f"Maaf, {i} kami habis. Silahkan order lainnya."
        return False


def bayar_kembali(harga):
    sen1 = int(input("masukan 1 sen! :")) * 0.01
    sen5 = int(input("masukan 5 sen! :")) * 0.05
    sen10 = int(input("masukan 10 sen! :")) * 0.10
    sen25 = int(input("masukan 25 sen! :")) * 0.25
    total = sen1 + sen5 + sen10 + sen25
    print(f"Uang anda adalah ${total}")
    if harga > total:
        return False
    return round(total - harga, 2)


def restock():
    nama = input("Bahan: ")
    resources[nama] += int(input("Tambah: "))
    again = input("lagi? (Y or N): ").lower()
    if again == "n":
        return
    restock()


def cafe():
    """Cafe yang sangat fancy!"""
    tanya = input("Mau Apa? :").lower()
    if tanya == "stock":
        for i in resources:
            print(f"{i}: {resources[i]}")
        cafe()
    elif tanya == "restock":
        restock()
        cafe()
    elif tanya == "off":
        print("Mesin mati dan semua te-reset ke setelan pabrik.")
        return
    elif tanya == "latte" or "cappuccino" or "espresso":
        order = MENU[tanya]
        bahan = order["ingredients"]
        harga = order["cost"]
        hasil_cek = cek_bahan(bahan)
        if not hasil_cek:
            print(f"Harga {tanya} adalah {harga}. Silahkan bayar!")
            kembali = bayar_kembali(harga)
            if not kembali:
                print("Maaf uang anda tidak cukup.")
                cafe()
            else:
                print(f"Kembalian :${kembali}\nSilahkan menikmati {tanya} anda.")
                for i in bahan:
                    resources[i] -= bahan[i]
                cafe()
        else:
            print(cek_bahan(bahan))
            cafe()
    else:
        cafe()


cafe()
