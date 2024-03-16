def main():
  numero = input('Digite um número de dois dígitos: ')
  numeros_separados = [int(i) for i in str(numero)]

  numeros_soma = numeros_separados[0] + numeros_separados[1]
  numeros_sub = numeros_separados[0] - numeros_separados[1]
  numeros_multi = numeros_separados[0] * numeros_separados[1]
  numeros_divi = numeros_separados[0] / numeros_separados[1]

  print(numeros_soma, numeros_sub, numeros_multi, int(numeros_divi))

main()
