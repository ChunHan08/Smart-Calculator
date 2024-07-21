response=['welcome to smart calculator', 'my name is calc', 'thanks for using me!', 'sorry, thi is beyond my abilities']

def add(x,y):
  return x+y

def sub(x,y):
  return x-y

def mul(x,y):
  return x*y

def div(x,y):
  return x/y

def mod(x,y):
  return x%y

def lcm(x,y):
  L=x if x>y else y
  while L<=x*y:
    if L%x==0 and L%y==0:
      return L
    L+=1
def hcf(x,y):
  H=x if x<y else y
  while H>=1:
    if x%H==0 and y%H==0:
      return H
    H-=1

def extract_from_text(text):
  l=[]

for t in text.split(' '):
  try: 
    l.append(float(t))
  except ValueError:
    pass
  return l


operations = {
  'ADD':add,
  'PLUS': add,
  'SUM': add,
  'ADDITION': add,
  'SUB': sub,
  'SUBTRACT': sub,
  'MINUS': sub,
  'DIFFERENCE': sub,
  'LCM': lcm,
  'HCF': hcf,
  'PRODUCT': mul,
  'MULTIPLY': mul,
  'MULTIPLICATION': mul,
  'DIVISION': div,
  'MOD': mod,
  'REMAINDER': mod,
  'MODULUS': mod,
}

commands = {
  'NAME': myname,
  'EXIT': end,
  'END': end,
  'CLOSE': end,
} 

def myname():
  print(response[1])
def end():
  print(response[2])
  input('press enter key to exit')
  exit()

print(response[0])
print(response[1])

while True:
  text=input('enter your queries:')
  for word in text.split(' '):
    if word.upper() in operations.keys():
      try:
        l = extract_from_text(text)
        r = operations[word.upper()](l[0],l[1])
        print(r)
      except:
        print('something went wrong and i couldnt parse your input, plz enter again!!! sorry, invalid input')
      finally:
        break 
    elif word.upper() in commands.keys():
      commands[word.upper()]()
      break
    else:
      print(response[3])