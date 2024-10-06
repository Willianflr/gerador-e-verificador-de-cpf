import random
import time
import re
import sys

for _ in range(77):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regeressivo_1 = 10 
    print(nove_digitos)
    time.sleep(0.5)
    resultado_digit_1 = 0
    for digito in nove_digitos:
        resultado_digit_1 += int(digito) * contador_regeressivo_1
        contador_regeressivo_1 -= 1
    digito_1 = (resultado_digit_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    
    dez_digitos = nove_digitos + str(digito_1)
    
    
    contador_regeressivo_2 = 11
    
    resultado_digit_2 = 0
    for digito in dez_digitos:
        resultado_digit_2 += int(digito) * contador_regeressivo_2
        contador_regeressivo_2 -= 1 
    digito2 = (resultado_digit_2 * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0
    
    cpf_gerado_pelo_calculo = (f'{nove_digitos}{digito_1}{digito2}')
    
else:
    print('cpf inválido')
