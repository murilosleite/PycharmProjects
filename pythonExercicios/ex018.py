from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COSENO de {:.2f}'.format(angulo, coseno))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))
