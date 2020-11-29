#Latihan2Chapter5
#5

print ('Hai...nama saya Mr.Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!')
ab=int(input('Tebakan Anda :'))
while True:
    if (ab<10):
        print('Hehehe...Bilangan anda terlalu kecil')
        ab=int(input('Tebakan Anda:'))
    elif(ab>10):
        print('Hehehe...Bilangan anda terlalu besar')
        ab=int(input('Tebakan Anda:'))
    elif(ab==10):
        print('yeee...Bilangan tebakan anda benar')
        break
               
