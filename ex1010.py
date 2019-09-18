cod1, pecas1, valor_unit1 = input().split(' ') 
cod2, pecas2, valor_unit2 = input().split(' ') 

pecas_int1 = int(pecas1)
pecas_int2 = int(pecas2)

valor_unit1_float = float(valor_unit1)
valor_unit2_float = float(valor_unit2)

valor_a_pagar = pecas_int1*valor_unit1_float + pecas_int2*valor_unit2_float


print("VALOR A PAGAR: R$ {:.2f}".format(valor_a_pagar))
