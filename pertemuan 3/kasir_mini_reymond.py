nama_barang = input("Masukkan nama barang: ")
harga_barang = int(input("Masukkan harga barang: Rp "))
jumlah_barang = int(input("Masukkan jumlah barang: "))
uang_pembayaran = int(input("Masukkan Nominal: Rp "))                   

total = harga_barang * jumlah_barang
kembalian = uang_pembayaran - total

print("=== KASIR MINI ===")
print("Nama barang :", nama_barang)
print("Harga       : Rp", harga_barang)
print("Jumlah      :", jumlah_barang)
print("Total bayar : Rp", total)
print("kembalian   : Rp", kembalian)