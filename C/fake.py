if __name__ == '__main__':
  N, V = map(int, input().split())
  AB = [tuple(map(int, input().split())) for _ in range(N)]

  count: int = 0
  tempo_total: int = 0
  while True:
    visitas = sum((count - a) // b + 1 for a, b in AB)
    
    if visitas >= V:
      tempo_total = visitas
      break

    count += 1

  print(count)
