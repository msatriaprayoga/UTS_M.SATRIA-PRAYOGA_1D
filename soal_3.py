storebarang = 0
while True:
    jumlahbarang = int(input(f'Masukan Jumalah Barang {i}: '))
    for i in range(1, jumlahbarang + 1):
        jumlahbarang = 0
        hargabarang = int(input('Masukan Harga Brang : '))
        storebarang += hargabarang

penggabungan = storebarang + jumlahbarang
print(f'Total Belanjaan : Rp. {penggabungan}')
