if __name__ == '__main__':
  A, B, C, D = map(int, input().split())

  current: int = 0
  while True:
    current += 1
    if current % A == 0 and current % B != 0 and C % current == 0 and D % current != 0:
      break
  
  print(current)