#Latihan2Chapter5
#6

print ('Hai...nama saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!')
ab=int(input('Tebakan Anda :'))
c=0
while True:
    if (ab<10):
        print('Hehehe...Bilangan anda terlalu kecil')
        ab=int(input('Tebakan Anda:'))
        c+=2
    elif(ab>10):
        print('Hehehe...Bilangan anda terlalu besar')
        ab=int(input('Tebakan Anda:'))
        c+=2
    elif(ab==10):
        print('yeee...Bilangan tebakan anda benar')
        score=100-c
        print('Score anda:'+str(score))
        break
