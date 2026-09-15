nama_server = input("masukkan nama server....")
suhu = int(input("masukkan suhu cpu"))

if suhu <= 40:
  print("suhu terlalu rendah")
elif suhu <= 59:
  print("suhu normal")
elif suhu <= 79:
  print(" suhu cukup tinggi")
else:
  print("WARNING SUHU CPU TINGGI")