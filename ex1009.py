nome = input()
salary = float(input())
total_of_vendas = float(input())
comissao = 0.15*total_of_vendas
total = salary + comissao

print("TOTAL = R$ {:.2f}".format(total))
