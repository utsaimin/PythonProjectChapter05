#Latihan1Chapter5
#5

a=int(input('Masukkan Kode karyawan:'))
b=input('Masukkan nama karyawan:')
c=input ('Masukkan golongan:')
d=input('Masukkan status (1:Menikah,2:Belum):')
if (d=='1'):
    JumlahAnak int (input('Masukkan Jumlah Anak:'))
    TunjanganMenikah =10/100
    TunjanganAnak =5/100
    StatusMenikah = 'Sudah Menikah'
else:
    JumlahAnak = 0
    TunjanganMenikah = 0
    TunjanganAnak = 0
    StatusMenikah = 'Belum Menikah'

print ('====================')

print ('STRUK RINCIAN GAJI KARYAWAN')

print ('--------------------')

print('NamaKaryawan:' ,b + ' (Kode:'+str(a),')')
print ('Golongan:',c)
print ('StatusMenikah:',d)
print ('JumlahAnak:',JumlahAnak)

print ('--------------------')

if (c== 'A'):
    GajiPokok = 10000000
    Potongan = 2.5
    JumlahTunjanganMenikah = 10000000 + TunjanganMenikah
    JumlahTunjanganAnak = 10000000 +  TunjanganAnak
    GajiKotor = 10000000 + TunjanganMenikah + TunjanganAnak
    JumlahPotongan = 2.5 /100 *GajiKotor
    GajiBersih = GajiKotor-JumlahPotongan

elif (c== 'B'):
    GajiPokok = 8500000
    Potongan = 2.0
    JumlahTunjanganMenikah = 8500000 + TunjanganMenikah
    JumlahTunjanganAnak = 8500000 +  TunjanganAnak
    GajiKotor = 8500000 + TunjanganMenikah + TunjanganAnak
    JumlahPotongan = 2.0 /100 *GajiKotor
    GajiBersih = GajiKotor-JumlahPotongan

elif (c== 'C'):
    GajiPokok = 7000000
    Potongan = 1.5
    JumlahTunjanganMenikah = 7000000+ TunjanganMenikah
    JumlahTunjanganAnak = 7000000 +  TunjanganAnak
    GajiKotor = 7000000 + TunjanganMenikah + TunjanganAnak
    JumlahPotongan = 1.5 /100 *GajiKotor
    GajiBersih = GajiKotor-JumlahPotongan

elif (c== 'D'):
    GajiPokok = 5500000
    Potongan = 1.0
    JumlahTunjanganMenikah = 5500000+ TunjanganMenikah
    JumlahTunjanganAnak = 5500000 +  TunjanganAnak
    GajiKotor = 5500000 + TunjanganMenikah + TunjanganAnak
    JumlahPotongan = 1.0 /100 *GajiKotor
    GajiBersih = GajiKotor-JumlahPotongan

print ('GajiPokok:Rp'+str(GajiPokok))
print ('TunjanganMenikah :Rp' +str (JumlahTunjanganMenikah))
print ('TunjanganAnak : Rp' + str (JumlahTunjanganAnak))

print ('----------------------------------------')

print ('GajiKotor : Rp' + str (GajiKotor))
print ('Potongan('+str(Potongan)+%):Rp'+str (JumlahPotongan))

print ('----------------------------------------')

print ('GajiBersih : Rp'+str(GajiBesih))

