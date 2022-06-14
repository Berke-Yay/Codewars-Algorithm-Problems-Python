def sifrele(metin, anahtar):
    sifreli=""
    for harf in metin:
        asciikodu=ord(harf)
        asciikodu+=int(anahtar)
        karakter=chr(asciikodu)
        sifreli=sifreli+karakter
    print("Girdiğiniz değer: "+metin+" / Şifreli karşılığı: "+sifreli)

def sifrecoz(metin):
    cozulen=""
    for harf in metin:
        asciikodu=ord(harf)
        asciikodu=asciikodu-2
        karakter=chr(asciikodu)
        cozulen=cozulen+karakter
    print("Girdiğiniz: "+metin+" / Çözülmüş karşılığı: "+cozulen)
    
kelime=input("Şifrelemek istediğiniz metni girin: ")
anahtar=input("Metni şifrelemek için bir anahtar numara giriniz(Metnin çözülmesi için bu numaranın bilinmesi gerekecektir): ")
sifrele(kelime, anahtar)
