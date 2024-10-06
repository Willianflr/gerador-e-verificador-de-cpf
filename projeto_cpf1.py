# FUNÃO PARA VER SE O CPF É VÁLIDO

cpf_novo = list('Digite um cpf para fazer a validação: ')
cpf_novo_str = input(''.join(cpf_novo))
def validar_cpf():
    if len(cpf_novo) == 11:
        pri_num1 = int(cpf_novo[0]) * 10
        pri_num2 = int(cpf_novo[1]) * 9
        pri_num3 = int(cpf_novo[2]) * 8
        pri_num4 = int(cpf_novo[3]) * 7
        pri_num5 = int(cpf_novo[4]) * 6
        pri_num6 = int(cpf_novo[5]) * 5
        pri_num7 = int(cpf_novo[6]) * 4
        pri_num8 = int(cpf_novo[7]) * 3
        pri_num9 = int(cpf_novo[8]) * 2
         
        seg_pri_num1 = int(cpf_novo[0]) * 11
        seg_pri_num2 = int(cpf_novo[1]) * 10
        seg_pri_num3 = int(cpf_novo[2]) * 9
        seg_pri_num4 = int(cpf_novo[3]) * 8
        seg_pri_num5 = int(cpf_novo[4]) * 7
        seg_pri_num6 = int(cpf_novo[5]) * 6
        seg_pri_num7 = int(cpf_novo[6]) * 5
        seg_pri_num8 = int(cpf_novo[7]) * 4
        seg_pri_num9 = int(cpf_novo[8]) * 3
        seg_pri_num10 = int(cpf_novo[9]) * 2

        somar_valida = (pri_num1 +
                        pri_num2 +
                        pri_num3 +
                        pri_num4 +
                        pri_num5 +
                        pri_num6 +
                        pri_num7 +
                        pri_num8 +
                        pri_num9 )
        divisão_Soma =(somar_valida // 11)
        resto_divisão = (somar_valida - (11 * divisão_Soma))

        somar_valida_seg = (seg_pri_num1 +
                        seg_pri_num2 +
                        seg_pri_num3 +
                        seg_pri_num4 +
                        seg_pri_num5 +
                        seg_pri_num6 +
                        seg_pri_num7 +
                        seg_pri_num8 +
                        seg_pri_num9 )
        divisão_Soma_seg =(somar_valida_seg // 11)
        resto_divisão_seg = (somar_valida_seg - (11 * divisão_Soma_seg))

        digito_antepenultimo_cpf = int(cpf_novo[8])
        digito_penultimo_cpf = int(cpf_novo[9])
        digito_ultimo_cpf = int(cpf_novo[10])

        valor_1 = False
        valor_2 = False
        valor_3 = False
        valor_4 = False

        if(resto_divisão <= 1) and (digito_penultimo_cpf == 0):
            valor_1 = True

        elif(resto_divisão >= 2 and resto_divisão < 10) and (11 - resto_divisão == digito_penultimo_cpf):
            valor_2 = True

        elif(resto_divisão_seg <= 1 ) and (digito_ultimo_cpf == 0):
            valor_3 = True

        elif(resto_divisão_seg >= 2 and resto_divisão_seg < 10 )and (11 - resto_divisão_seg == digito_ultimo_cpf):
            valor_4 = True

        else: ()

        if (valor_1 == True or valor_2 == True) and (valor_3 == True or valor_4 == True):
            print(f'O cpf número: {cpf_novo_str} é válido! ')
        else:
            print(f'O cpf número:{cpf_novo_str} é inválido, tente novamente. ') 

            # ORIGEM DO CPF A QUAL ESTADO PERTENCE       

        if digito_antepenultimo_cpf == 1:
           print("Seu CPF é originário do estado do Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins")
        elif digito_antepenultimo_cpf == 2:
            print("Seu CPF é originário do estado do Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima")
        elif digito_antepenultimo_cpf == 3:
            print("Seu CPF é originário do estado do Ceará, Maranhão ou Piauí")
        elif digito_antepenultimo_cpf == 4:
            print("Seu CPF é originário do estado de Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas")
        elif digito_antepenultimo_cpf == 5:
            print("Seu CPF é originário do estado da Bahia; e Sergipe")
        elif digito_antepenultimo_cpf == 6:
            print("Seu CPF é originário de Minas Gerais")
        elif digito_antepenultimo_cpf == 7:
            print("Seu CPF é originário do estado do Rio de Janeiro ou Espírito Santo")
        elif digito_antepenultimo_cpf == 8:
            print("Seu CPF é originário do estado de São Paulo")
        elif digito_antepenultimo_cpf == 9:
            print("Seu CPF é originário do estado do Paraná ou Santa Catarina")
        else:
            print("Seu CPF é de origem do estado do Rio Grande do Sul")

    else: 
         print(f"O CPF número: {cpf_novo_str} é inválido, tente novamente.")

validar_cpf()