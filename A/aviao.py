
def aviao(input_list) -> int:
  H: int = input_list[0]
  K: int = input_list[1]
  V: int = input_list[2]
  S: int = input_list[3]

  traveledDistance: int = 0

  while H > 0:
    V += S
    V -= max(1, V // 10)

    if V >= K:
      H += 1
    
    if V > 0 and V < K:
      H -= 1
      if H == 0: V = 0
    
    if V <= 0:
      H = 0
      V = 0

    traveledDistance += V

    if S > 0:
      S -= 1
  
  return traveledDistance

if __name__ == "__main__":
  input_list = [int(x) for x in input().split()]
    
  print(aviao(input_list))