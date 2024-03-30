if __name__ == '__main__':
  ABC = [int(x) for x in input().split()]
  result: str = 'N'

  for i in range(len(ABC)):
    for j in range(i+1, len(ABC)):
      if ABC[i] == ABC[j] or ABC[i] + ABC[j] == sum(ABC) - ABC[i] - ABC[j]:
        result = 'S'
        break

  print(result)

