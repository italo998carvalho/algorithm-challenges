def is_anagram(test, original):
  if len(test) != len(original):
    return False

  test = test.lower()
  original = original.lower()

  for i in test:
    for j in original:


# - se não é case sensitive a primeira coisa que eu penso é converter tudo pra maiusculo ou
# minusculo, mas por ser linear talvez tenha jeito melhor de fazer a comparação depois
# - o reverse padrão em python é em O(n) e parece que não da pra fugir disso
# - a primeira ideia é converter as duas string
# - é o mesmo problema do ransomNote, duas strings onde você precisa chegar o conteúdo de uma
# dentro da outra, não pensei em como resolver sem ser em O(n*m)

# - penso que pra resolver o problema do anagrama da pra fazer um O(nm) onde cada iteração
# de n procura pelo caractere em m, se encontrar seta como nulo e roda dnv
# - se toda a string ficar nula ta resolvido
