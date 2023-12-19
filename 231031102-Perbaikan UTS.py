mdata = ['RESKY RAMADHANI',
         'Rezky6249@ith.ac.id',
         'PT. ABC DESIGN',
         'JLN.BALAIKOTA NO.1 PAREPARE',
         'Gojo Satoru',
         '25 oktober 2023']

print('manager:', mdata[0])
print('email:', mdata[1])
print('perusahaan:', mdata[2])
print('alamat:', mdata[3])
print('kasir:', mdata[4])
print('tanggal lahir:', mdata[5])

ps = 80

print('\n')
print(mdata[2].center(ps))
print(mdata[3].center(ps))
print(mdata[1].center(ps))

djual = [['Kertas', 'Pensil', 'Peraut', 'Paper Clip', 'Buku'],
         ['D0001', 'D0002', 'D0003', 'D0004', 'D0005'],
         [20000, 15000, 559000, 50000, 25000],  # Harga satuan sebagai angka
         [3, 3, 3, 3, 3]]

print('\n')
print(f'''MANAGER           : {mdata[0]}
KASIR             : {mdata[4]}
Tanggal Pembelian : {mdata[-1]}''')
print('-' * (77))
print('No. Kode Barang'.ljust(16) + '|' + 'Nama Barang'.center(19) + '|' + 'H. Satuan'.center(15) + '|' + 'Jumlah'.center(14) + '|')
print('-' * (77))

# Membuat loop untuk mencetak data barang
subtotal = 0  # Menyimpan total harga
for i in range(len(djual[0])):
    nama_barang = djual[0][i]
    kode_barang = djual[1][i]
    harga_satuan = djual[2][i]
    jumlah = djual[3][i]
    total = harga_satuan * jumlah
    subtotal += total  # Menambahkan total harga barang ke subtotal
    print(f'{i + 1}.  {kode_barang}'.ljust(16) + '|' + f' {nama_barang}'.ljust(19) + '|' +
          f'Rp{harga_satuan * jumlah},-'.rjust(15) + '|' + f'{jumlah}'.center(8) + '|' +
          'Total'.center(14) + '|' + f'Rp{total},-'.center(14) + '|')

# Menambahkan subtotal ke akhir
print('-' * (77))
print(f'SUBTOTAL:'.ljust(63) + f'Rp{subtotal},-'.center(14) + '|')
print('-' * (77))

# Menghitung harga tertinggi dan terendah
harga_tertinggi = max(djual[2])
harga_terendah = min(djual[2])

# Mencari indeks item dengan harga tertinggi dan terendah
indeks_tertinggi = djual[2].index(harga_tertinggi)
indeks_terendah = djual[2].index(harga_terendah)

# Menampilkan harga tertinggi dan terendah beserta barangnya
print(f'Harga tertinggi adalah    : Rp{harga_tertinggi},- ({djual[1][indeks_tertinggi]} - {djual[0][indeks_tertinggi]})')
print(f'Harga terendah  adalah    : Rp{harga_terendah},- ({djual[1][indeks_terendah]} - {djual[0][indeks_terendah]})')

# Menambahkan informasi tambahan
print(f'Harga rata-rata pembelian : Rp ,-\n')
print('Parepare, 25 Oktober 2023'.center(77))
print('\n')
print('Gojo Satoru'.center(77))
print('------------'.center(77))
print('RESKY RAMADHANI'.center(77))
