#In honour of Halloween, this code prints any phrase with every second letter changing from black to orange!!!
orange = "\033[33m"
black = "\033[30m"
phrase = str(input())
for i in range(len(phrase)):
  if i % 2 == 0:
    print(black + phrase[i], end="")
  else:
    print(orange + phrase[i], end="")