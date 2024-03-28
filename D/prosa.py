def prosa(string) -> int:
    letras_unicas = set()

    for caractere in string.lower():
        if caractere in 'abcdefghijklmnopqrstuvwxyz':
            letras_unicas.add(caractere)

    return len(letras_unicas)

N: int = int(input())

while N > 0:
  N -= 1

  frase = input()
  letras_alfabeto: int = prosa(frase)

  if(letras_alfabeto == 26):
    print("boa informacao")
  elif(letras_alfabeto >= 13):
    print("media informacao")
  else:
    print("pouca informacao")