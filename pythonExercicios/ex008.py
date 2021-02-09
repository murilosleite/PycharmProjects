distM = int(input('Digite a distância em metro: '))
km = distM / 100
hm = distM / 100
dam = distM / 10
dm = distM * 10
cm = distM * 100
mm = distM * 1000
print('A medida de {} corresponde à: '.format(distM))
print('{} quilômetros (Km)'.format(km))
print('{} hectômetros (Hm)'.format(hm))
print('{} decâmetros (Dam)'.format(dam))
print('{} decimetros (dm)'.format(dm))
print('{} centímetros (cm)'.format(cm))
print('{} milímetros (mm)'.format(mm))