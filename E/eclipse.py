if __name__ == "__main__":
  Ds, Ys = map(int, input().split())
  Dm, Ym = map(int, input().split())

  temp = {"s": Ys - Ds, "m": Ym - Dm}

  count = 0
  while temp["s"] != temp["m"]:
    temp["s"] -= 1
    if temp["s"] <= 0: temp["s"] = Ys
    temp["m"] -= 1
    if temp["m"] <= 0: temp["m"] = Ym
    count += 1

  print(count + temp["s"])