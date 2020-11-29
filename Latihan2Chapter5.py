#Latihan2Chapter5
#2

a=int(input('Nilai Bahasa Indonesia :'))
b=int (input('Nilai Matematika:'))
c=int (input('Nilai IPA'))

print ('====================')

if(a<0 or a>100):
    print ('Maaf input ada yang tidak valid')
elif (b<0 or b>100):
     print ('Maaf input ada yang tidak valid')
elif (c<0 or c>100):
    print ('Maaf input ada yang tidak valid')

elif (a>60 and b>60 and c>70):
    print('Status kelulusan : LULUS')
else :
    print ('Status kelulusan :TIDAK LULUS')
