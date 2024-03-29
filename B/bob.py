if __name__ == "__main__":  
  #campeonato_stream: str = "BBAAABABBAAABB"
  #campeonato_stream: str = "AABBBAAB"
  campeonato_stream: str = str(input())

  partidas: dict[str, int] = {
    "A": 0,
    "B": 0
  }

  K_partidas: list[int] = []

  for current_ganhador in campeonato_stream:
    partidas[current_ganhador] += 1
    if partidas["A"] > partidas["B"]: 
      if partidas["A"] not in K_partidas and partidas["A"] > 1: 
        K_partidas.append(partidas["A"])

  print(len(K_partidas))
  print(*K_partidas, sep=" ")
