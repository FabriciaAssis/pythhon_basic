def init():
  num = input('Digite um número de dois dígitos: ')
  num_separete = [int(i) for i in str(num)]

  num_add = num_separete[0] + num_separete[1]
  num_sub = num_separete[0] - num_separete[1]
  num_multi = num_separete[0] * num_separete[1]
  num_divi = num_separete[0] / num_separete[1]

  print(num_add, num_sub, num_multi, int(num_divi))

init()
