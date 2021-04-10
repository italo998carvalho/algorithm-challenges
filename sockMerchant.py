def sockMerchant(n, ar):
  pairs = 0
  socks = {}
  
  for sock in ar: # O(n)
    if sock in socks: # O(1)
      pairs += 1
      socks.pop(sock, None) # O(1)
    else:
      socks[sock] = True

  return pairs

print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))

# - aparentemente não vai ter jeito de fugir de O(n)
# - da pra ir iterando no array e pra cada par novo, salva num dicionario,
# se fechar o par, tira do dicionario
# - poderia usar o has_key pra ver se a chave já existe, se existir eu fecho um par
# e se não existir eu salvo no dicionario, mas o has_key é O(n) no pior caso, o que
# faria o algoritmo ficar O(n²)
# - essa questão diz que o operador in em dicionarios é O(1):
# https://stackoverflow.com/questions/17539367/python-dictionary-keys-in-complexity

