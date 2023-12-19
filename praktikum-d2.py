print('praktikum-d2 \n\n')
print('==========ini AND==========')
a = True
b = False
hasil = a and a
print('Nilai',a,'and',a,'adalah',hasil)
a = True
b = False
hasil = a and b
print('Nilai',a,'and',b,'adalah',hasil)
a = True
b = False
hasil = b and a
print('Nilai',b,'and',a,'adalah',hasil)
a = True
b = False
hasil = b and b
print('Nilai',b,'and',b,'adalah',hasil)

print('\n==========ini or==========')
hasil = a and a
print('Nilai',a,'and',a,'adalah',hasil)
a = True
b = False
hasil = a and b
print('Nilai',a,'and',b,'adalah',hasil)
a = True
b = False
hasil = b and a
print('Nilai',b,'and',a,'adalah',hasil)
a = True
b = False
hasil = b and b
print('Nilai',b,'and',b,'adalah',hasil)

print('\n==========ini not==========')
hasil = not a
print('hasil not',a,'adalah',hasil)
hasil = not b
print('hasil not',b,'adalah',hasil)

print('\n==========ini xor==========')
hasil = a ^ a
print('Nilai',a,'xor',a,'adalah',hasil)
hasil = a ^ b
print('Nilai',a,'xor',b,'adalah',hasil)
hasil = b ^ a
print('Nilai',b,'xor',a,'adalah',hasil)
hasil = b ^ b
print('Nilai',b,'xor',b,'adalah',hasil)


print('==========ini nand==========')
hasil = not (a and a)
print('Nilai',a,'nand',a,'adalah',hasil)
hasil = not (a and b)
print('Nilai',a,'nand',b,'adalah',hasil)
hasil = not (b and a)
print('Nilai',b,'nand',a,'adalah',hasil)
hasil = not (b and b)
print('Nilai',b,'nand',b,'adalah',hasil)

print('==========ini nor==========')
hasil = not (a and a)
print('Nilai',a,'nor',a,'adalah',hasil)
hasil = not (a and b)
print('Nilai',a,'nor',b,'adalah',hasil)
hasil = not (b and a)
print('Nilai',b,'nor',a,'adalah',hasil)
hasil = not (b and b)
print('Nilai',b,'nor',b,'adalah',hasil)


print('\n==========ini nxor==========')
hasil = a ^ a
print('Nilai',a,'nxor',a,'adalah',not hasil)
hasil = a ^ b
print('Nilai',a,'nxor',b,'adalah',not hasil)
hasil = b ^ a
print('Nilai',b,'nxor',a,'adalah',not hasil)
hasil = b ^ b
print('Nilai',b,'nxor',b,'adalah',not hasil)

print('============IS')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

print('============IS NOT')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

print('\n============in')
nama = 'Bacharuddin Jusuf Habibie'
test = 'rud'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))


test = 'Bach'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))


print('\n============ not in')
#Tugas buat nama menjadi nama lengkap masing-masing

print('\n============in')
data = ['Institut',
        'Teknologi',
        'Bacharuddin',
        'Jusuf',
        'Habibie',]
print('Data adalah',data)
test1 = 'Habibie'
test2 = 'Parepare'
test3 = 'Kampus'
test4 = 'Institut'

cek = test1 in data
print(test1,'terdapat di data adalah'+str(cek))

cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 in data
print(test4,'terdapat di data adalah '+str(cek))

print('\n============ not in')
#Tugas dengan cara yang sama buat operasiuntuk not in

#INI OPERATOR BITWSE
a = 26 
b = 10
b+= 2005
print('\n=============== AND')
print('Nilai',a,'dalam biner=     ',format(a,'08b'))
print('Nilai',b,'dalam biner=     ',format(b, '08b'))

print('============================= AND')
c = a & b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))


print('\n=============== not In')
# tugas buat nama menjadi nama lengkap masing masing
nama = 'Resky Ramadhani'

test = 'rud'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'bach'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'ib'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

print('\n=============== not In')
# tugas dengan cara yang sama buat operator untuk not in
data = ['Resky',
        'Ramadhani']
print('Data adalah',data)
test1 = 'Resky Ramahani'
test2 = 'Resky'
test3 = 'Ramadhani'
test4 = 'Resky Ramadhani'

cek = test1 not in data
print(test1,'tidak terdapat di data adalah '+str(cek))
cek = test2 not in data
print(test2,'tidak terdapat di data adalah '+str(cek))
cek = test3 not in data
print(test3,'tidak terdapat di data adalah '+str(cek))
cek = test4 not in data
print(test4,'tidak terdapat di data adalah '+str(cek))

print('\n=============== XOR')
#tugas untuk operator XOR, c = a ^ b
a = 26
b = 10
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- XOR')
c = a ^ b
print('Nilai',a,'^',b,'biner adalah',format(c,'08b'))

print('\n=============== not')
#tugas untuk operator not, c = ~a
a = 26
b = 10
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- not')
c = ~a
print('Nilai',~a,'biner adalah',format(c,'08b'))

print('\n=============== not')
#tugas untuk operator not, c = ~b
a = 26
b = 10
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- not')
c = ~b
print('Nilai',~b,'biner adalah',format(c,'08b'))

print('\n=============== geser kanan')
#tugas untuk operator geser kanan, c = a >> 2
a = 26
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('--------------------------------------------- geser kanan')
c = a >> 2
print('Nilai',(a) >> 2,'biner adalah',format(c,'08b'))

print('\n=============== geser kiri')
#tugas untuk operator geser kiri, c = a << 2
a = 26
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('--------------------------------------------- geser kiri')
c = a >> 2
print('Nilai',(a) << 2,'biner adalah',format(c,'08b'))

print('\n=============== not and')
#tugas untuk operator not and, c = ~(a & b)
a = 26
b = 10
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- not and')
c = ~(a & b)
print('Nilai',~(a & b),'biner adalah',format(c,'08b'))

print('\n=============== not or')
#tugas untuk operator not or, c = ~(a | b)
a = 26
b = 10
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- not or')
c = ~(a | b)
print('Nilai',~(a | b),'biner adalah',format(c,'08b'))

print('\n=============== not xor')
#tugas untuk operator not xor, c = ~(a ^ b)
a = 26
b = 10
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- not xor')
c = ~(a ^ b)
print('Nilai',~(a ^ b),'biner adalah',format(c,'08b'))

print('\n=============== not geser kanan')
#tugas untuk operator not geser kanan, c = ~(a >> 2)
a = 26
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('--------------------------------------------- not geser kanan')
c = ~(a >> 2)
print('Nilai',~((a) >> 2),'biner adalah',format(c,'08b'))

print('\n=============== not geser kiri')
#tugas untuk operator not geser kanan, c = ~(a << 2)
a = 26
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('--------------------------------------------- not geser kanan')
c = ~(a << 2)
print('Nilai',~((a) << 2),'biner adalah',format(c,'08b'))
      
