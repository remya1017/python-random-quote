import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  while True:
    quotes = f.readline()
    if not quotes:
      break
    print(quotes)
  f.close()

  #last = 13
  #rnd = random.randint(0, last)
  print(quotes)

if __name__== "__main__":
  primary()
