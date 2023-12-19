nama = 'REZKY RAMADHANI'
nim = '231031102'
prodi = 'SISTEM INFORMASI'
meet = 'praktikum d3'
email = 'Rezky6249@gmail.com'

print(len(nama))

ap = 31
print('-'.center(ap,'-'))

print(nama.center(ap))
print(nim.center(ap))
print('\n'*2)
print(meet.rjust(ap))
print(prodi.rjust(ap))
print(email.rjust(ap))

print('-'.center(ap,'-'))

paragraf = '''\tHalo, selamat datang perkenalkan nama
saya {} dengan NIM {} dari prodi
{}. Ini adalah file {}.'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)

# ---------------5++++++9-------------
x = int(input('Masukkan Nilai= '))
print(x)
#1. input nilai x
x = int(input('Masukkan Nilai= '))
#2. cek1 apakah x>5 True
cek1 = x>5
#3. cek2 apakah x<9 True
cek2 = x<9
#4. status = cek1 dan cek2
status = cek1 and cek2
#5. cetak status
print('Hasilnya adalah',status)
# ++++++++++5------9+++++++++++
# 1. input x
x = int(input('Masukkan Nilai ++5---9++= '))
# 2. cek1 apakah x<5
cek1 = x<5
# 3. cek2 apakah x>9 false
cek2 = x>9
# 4. status = cek1 or cek2 true
status = cek1 or cek2
# 5. cetak status
print('Hasilnya adalah',status)

# ++++++5------9++++++13------
# 1. input x
x = int(input('Masukkan Nilai ++5---9++13= '))
# 2. cek1 x<5
cek1 = x<5
# 3. cek2 x>9
cek2 = x>9
# 4. cek4 x<13
cek = x<13
# 5. status cek1 or cek2 or cek3
status = cek1 or cek2 and cek3
# 6. cek status
print('Hasilnya adalah',status)


# Tugas 1
# ----5++++9------13+++++16-----

# 1. Input nilai
x = int(input('Masukkan Nilai --5++9--13++16--= '))
# 2. Cek1 x>5
cek1 = x>5
# 3. Cek2 x<9
cek2 = x<9
# 4. cek3 x>13
cek3 = x>13
# 5. cek4 x<16
cek4 = x<16
# 6. status cek1 and cek2 or cek3 and cek4
status = cek1 and cek2 or cek3 and cek4
# 7. cetak status
print('Hasilnya adalah',status)

# Tugas 2
# ++++5----9++++13----16+++++

# 1. Input nilai
x = int(input('Masukkan Nilai ++5--9++13--16++= '))
# 2. Cek1 x<5
cek1 = x<5
# 3. Cek2 x>9
cek2 = x>9
# 4. cek3 x<13
cek3 = x<13
# 5. cek4 x>16
cek4 = x>16
# 6. status cek1 or cek2 and cek3 or cek4
status = cek1 or cek2 and cek3 or cek4
# 7. cetak status
print('Hasilnya adalah',status)

# Tugas 3
# ----5++++9------13+++++16-----20+++++24-----

# 1. Input nilai
x = int(input('Masukkan Nilai --5++9--13++16--20++24--= '))
# 2. Cek1 x>5
cek1 = x>5
# 3. Cek2 x<9
cek2 = x<9
# 4. cek3 x>13
cek3 = x>13
# 5. cek4 x<16
cek4 = x<16
# 6. cek5 x>20
cek5 = x>20
# 7. cek6 x<24
cek6 = x<24
# 8. status cek1 and cek2 or cek3 and cek4 or cek5 and cek6
status = cek1 and cek2 or cek3 and cek4 or cek5 and cek6
# 9. cetak status
print('Hasilnya adalah',status)

# Tugas 4
# ++++5----9++++++13-----16+++++20-----24+++++
# 1. Input nilai
x = int(input('Masukkan Nilai ++5--9++13--16++20--24++= '))
# 2. Cek1 x<5
cek1 = x<5
# 3. Cek2 x>9
cek2 = x>9
# 4. cek3 x<13
cek3 = x<13
# 5. cek4 x>16
cek4 = x>16
# 6. cek5 x<20
cek5 = x<20
# 7. cek6 x>24
cek6 = x>24
# 8. status cek1 or cek2 and cek3 or cek4 and cek5 or cek6 
status = cek1 or cek2 and cek3 or cek4 and cek5 or cek6
# 9. cetak status
print('Hasilnya adalah',status)

