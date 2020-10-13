Size = 3
board = []
n = 1
length = 1
inv = []
for i in range(Size):
  s = ""
  s = s + "  "*(Size-i-1)
  for j in range(length):
    s=s+str(n)+" "
    board.append(n)
    inv.append((4*2**i-4)-(n-1))
    n+=1
  length+=2
  print(s)

def draw():
  n = 0
  length = 1

  for i in range(Size):
    s = ""
    s = s + "  "*(Size-i-1)
    for j in range(length):
      s=s+str(board[n])+" "
      n+=1
    length+=2
    print(s)
#+ pointing right
#- pointing left
#1: Leftmost Diagonal
#2: Rightmost Diagonal
#3: Horizontal
def move(dir, place):
  global board
  neg = -1
  if dir<0:
    neg = +1
    dir = dir*-1
  places = []
  if dir == 1:
    places.append(place**2 + 2*place)
    for i in range(Size-1-place):
      places.append(((Size-i-1-place)+place)**2+2*place)
      places.append(((Size-i-1-place)+place)**2+2*place + 1)
  elif dir == 2:
    places.append(inv[place**2 + 2*place])
    for i in range(Size-1-place):
      places.append(inv[((Size-i-1-place)+place)**2+2*place])
      places.append(inv[((Size-i-1-place)+place)**2+2*place + 1])
  elif dir == 3:
    for i in range(3*place):
      places.append(place**2+i)
  print(places)
  values=[]
  for i in range(len(places)):
    values.append(board[places[(i+neg)%len(places)]])
  for i in range(len(places)):
    board[places[i]] = values[i]
  draw() 
