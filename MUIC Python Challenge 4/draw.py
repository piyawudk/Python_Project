def triangle(k: int) -> None:
    if k > 1:
      star = "*"
      sharp = []
      for i in range(k-1):
          sharp+="#"

      while True:
          sharp_s = "".join(sharp)
          print(sharp_s+star+sharp_s)
          star +="**"
          if len(sharp) > 0 :
              sharp.remove("#")
          elif len(sharp) == 0 :
              break
    elif k == 1:
        print("*")
    else:
        print("")

def diamond(k: int) -> None:
    for i in range(k,0,-1):
        for j in range(i,0,-1):
            print("#",end="")
        for j in range(2*(k-i)+1):
            print("*",end="")
        for j in range(i,0,-1):
            print("#",end="")
        print()
    for i in range(k):
        for j in range(i+1):
            print("#", end="")
        for j in range(2*(k-i)-1):
            print("*", end="")
        for j in range(i+1):
            print("#", end="")
        print()

triangle(3)
print()
diamond(3)