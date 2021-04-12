def checkMagazine(magazine, note):
  magazine = magazine.split(' ')
  note = note.split(' ')

  for cn in note:
    steps = 0
    for index, cm in enumerate(magazine):
      if cn == cm:
        magazine[index] = None
        break

      if steps == len(magazine) - 1:
        print('No')
        return

      steps += 1

  print('Yes')

print(checkMagazine('apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg', 'elo lxkvg bg mwz clm w')) # no
# print(checkMagazine('o l x imjaw bee khmla v o v o imjaw l khmla imjaw x', 'imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o')) # no
# print(checkMagazine('give me one grand today night', 'give one grand today')) # yes
# print(checkMagazine('two times three is not four', 'two times two is four')) # no
# checkMagazine('None me one grand today night', 'give one grand today')

# - pelo que eu entendi, a ordem das palavras das duas frases precisam
# estar na mesma ordem, o que facilita um pouco
# - parece que o jeito mais simples termina num O(m+n)
# - posso percorrer a nota, e pra cada palavra eu faço uma varredura
# na string da revista, se achar a palavra eu vou pra próxima e
# mantenho o track de onde parei na string da revista
# - vou precisar de um contador pra manter o track de onde parei
# na string da revista
# - não estão ordenadas não
# - não consegui pensar em como resolver isso sem ser em O(n*m)

