#Latihan1Chapter5
#4

a=int(input('Masukkan kode karyawan:'))
b=input('Masukkan nama karyawan:')
c=input('Masukkan golongan')

print('===================')

print ('STRUK RINCIAN GAJI KARYAWAN')

print ('-------------------')
print('NamaKaryawan:' ,b +'(Kode:'+str(a),),
print ('Golongan:' ',)')

print ('-------------------')

if (c == 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    JumlahPotongan = 2.5 / 100*10000000
    GajiBersih = 10000000 - JumlahPotongan
elif (c== 'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    JumlahPotongan = 2.0/ 100*850000
    GajiBersih = 850000 - JumlahPotongan
elif (c== 'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    JumlahPotongan = 1.5/ 100*7000000
    GajiBersih = 7000000 - JumlahPotongan
elif (c== 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JumlahPotongan = 1.0/ 100*5500000
    GajiBersih = 5500000 - JumlahPotongan

print ('GajiPokok : Rp' + str(GajiPokok))
print ('Potongan ('+str(Potongan)+'%):Rp'+str(JumlahPotongan))
print ('----------------------------------------')

print ('GajiBersih : Rp' + str (GajiBersih))
