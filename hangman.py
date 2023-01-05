import random

vidas = 6

words = ['jirafa', 'carroceria', 'estetoscopio', 'vainilla', 'arcoiris', 'leñador']

word = ''
def play():
  global vidas
  global word 
  word = random.choice(words)
  while vidas > 0:
    print(drawWord())
    letter = input('Remaining lives: ' + str(vidas) + ' Guest a letter: ')
    positions = getAllPositions(word, letter)
    if len(positions) == 0:
      vidas = vidas - 1

def getAllPositions(word, letter):
  positions = []
  i = 0
  for pos in word:
    if letter == pos:
      positions.append(i)
    i = i + 1
  return positions

def drawWord():
  line = ''
  
  for pos in words:
    line = line + '_'
  return line

def main():
  inp = 'y'
  while inp == 'y':
    inp = input('Do you want to play?: ')
    if inp=='y':
      play()
    else:
      print('chau')

main()