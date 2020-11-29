#Latihan2Chapter5
#3

a=int(input('Nilai Bahasa Indonesia:'))
b= int(input('Matematika:'))
c=int(input('IPA'))

print ('====================')

if (a<0 or a>100):
    print ('Maaf input ada yang tidak valid')
elif (b<0 or b>100):
     print ('Maaf input ada yang tidak valid')
elif (c<0 or c>100):
    print ('Maaf input ada yang tidak valid')

elif (a>60 and b>70 and c>60):
    print ('Status kelulusan : LULUS')
else :
    print ('Status kelulusan : TIDAK LULUS')
    print ('Sebab:')
    if(a<60):
        print('-Nilai Bahasa Indonesia kurang dari 60')
    if (b<70):
        print('-Nilai Matematika kurang dari 70')
    if (c<60):
        print('-Nilai IPA kurang dari 60')
