def twoStrings(s1, s2): # O(nm)
  for c in s1:
    if c in s2:
      return 'YES'
  return 'NO'

# - preciso pensar numa lógica pra extrair todas as substrings possíveis de s1
# - checar se uma string é substring da outra é nativo do python (pesquisar complexidade)
# - não preciso checar todas as possíveis substrings, pois não existe nenhum caso onde
# uma substring de 1 caracter não contém, mas de 2 contém, sendo assim, uma busca linear resolve
