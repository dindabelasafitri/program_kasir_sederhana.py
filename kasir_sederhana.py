simpan_barang = []
while True:
      nama = input("masukkan nama barang: ")
      try:
         harga = int(input("masukkan harga barang: "))
      except ValueError:
         print("harga harus angka!")

      data_barang = {"nama": nama, "harga": harga}
      simpan_barang.append(data_barang)

      #lanjut atau tidak?
      lanjut = input("mau tambah barang? (y/n): ")
      if lanjut.lower() != "y":
         break

print("\nData Barang")
for s in simpan_barang:
    print(f"Nama: {s['nama']}, Harga: {s['harga']}")

total = sum(y["harga"] for y in simpan_barang)
print("total belanja: ", total)
