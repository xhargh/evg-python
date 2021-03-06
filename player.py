# Logic for controlling units

#  .  x  .
#  x  o  H
#  .  x  .

from game import Action, is_empty, Unit, GameState, build_distance_map
from random import randint

class Pt:
  x = 0
  y = 0
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def right(self):
    self.x = self.x + 1
  def left(self):
    self.x = self.x - 1
  def up(self):
    self.y = self.y - 1
  def down(self):
    self.y = self.y + 1
  def go(self, dir):
    if dir == 'up':
      self.up()
    elif dir == 'down':
      self.down()
    elif dir == 'right':
      self.right()
    elif dir == 'down':
      self.down()
  def __repr__(self):
      '''mostly for developers'''
      return f"({self.x}, {self.y})"

  def __str__(self):
      '''mostly for users'''
      return f"({self.x}, {self.y})"


def dist(u1, u2):
  return Pt(u2.x - u1.x, u2.y - u1.y)

def manhattan(pt):
  return abs(pt.x) + abs(pt.y)

def reverse(dir):
  if dir == 'left':
    return 'right'
  if dir == 'right':
    return 'left'
  if dir == 'up':
    return 'down'
  if dir == 'down':
    return 'up'

def directFromDist(pt):
  if randint(0, 3000) % 2 == 0:
    if pt.x <= -1:
      return 'left'
    elif pt.x >= 1:
      return 'right'
    elif pt.y <= -1 :
      return 'up'
    elif pt.y >= 1 :
      return 'down'
  else:
    if pt.y <= -1 :
      return 'up'
    elif pt.y >= 1 :
      return 'down'
    elif pt.x <= -1:
      return 'left'
    elif pt.x >= 1:
      return 'right'


def get_actions(state):
  currentPosition = [state.unit.x, state.unit.y]
  
  print(currentPosition)
  rnd = randint(0, 3)
  directions = ['left','right','up','down']
  #possibleNextPositions = 
  #print('floor = ', state.floor_map)
  #print('empty = ', state.empty_map)
  dirWalk = directions[rnd]
  dirAttack = 'left'
  foundFoe = False
  needToWalk = False
  manh = 1000

  # Idéer
  # - om man inte kan gå åt det hållet man vill, gå åt ett annat håll, ofta finns det ju två håll som är "rätt håll".
  # - låt alla units gå mot en och samma fiende och mosa denna.
  # -


  # Slå direkt
  for foe in state.foes:
    if (foe.health == 0):
      continue
    foeDist = dist(state.unit, foe)
    manh = manhattan(foeDist)

    #print('foe: ', foe.x, ' ', foe.y, ' (dist: ', foeDist,   ' manh: ', manh, ')')
    if (manh == 1):
      #print('found foe')
      dirAttack = directFromDist(foeDist)
      foundFoe = True
      break

  # First weakest non-dead enemy
  closestFoe = state.foes[0]
  minstrength = 1000
  for foe in state.foes:
    if (foe.health == 0):
      continue
    if foe.power+foe.health < minstrength:
      minstrength = foe.power+foe.health
      closestFoe = foe
      print('minstrength = ', minstrength)

  standStill = False
  attackThenWalk = False

  # Gå ett steg, slå sen
  if not foundFoe:
    print('go towards closeby')
    foeDist = dist(state.unit, closestFoe)
    dirWalk = directFromDist(foeDist)
    #if (manh == 1):
    #  foundFoe = True
    #if (manh == 2):
    #  standStill = True
    currentPt = Pt(state.unit.x, state.unit.y)
    currentPt.go(dirWalk)
    foeDist = dist(currentPt, foe)
    dirAttack = directFromDist(foeDist)
    needToWalk = True
  else:
    foeDist = dist(state.unit, closestFoe)
    dirWalk = directFromDist(foeDist)
    attackThenWalk = True

  # Move our weakest unit south east
  unitPowerList = []
  thereIsSomeoneWeaker = False
  for unit in state.units:
    unitPowerList.append((unit, unit.power+unit.health))
    #if (unit.health == 0):
    #  continue
    #if unit.power+unit.health > state.unit.power + state.unit.health:
    #  thereIsSomeoneWeaker = True
  
  sortedUnitPowerList = sorted(unitPowerList, key=lambda x: x[1])  
  weakestUnit = sortedUnitPowerList[0][0]
  secondWeakestUnit = sortedUnitPowerList[1][0]

  print('---', weakestUnit.id, state.unit.id)

    
  if state.unit.id == weakestUnit.id and weakestUnit.power+weakestUnit.health < secondWeakestUnit.power+secondWeakestUnit.health:
    print('reverse')
    dirWalk = reverse(dirWalk)


  moveAction = Action('move', dirWalk)
  attackAction =  Action('attack', dirAttack)

  if standStill:
    print("don't walk")
    actions = []
  elif (needToWalk and foundFoe):
    actions = [moveAction, attackAction]
  elif (attackThenWalk):
    actions = [attackAction, moveAction]
  elif (foundFoe):
    actions = [attackAction]
  else:
    actions = [moveAction]



  return actions

def get_player_info():
  print('get_player_info' )
  return {
    "id": "Rust",
    "name": "Rust"
  }

def game_end():
  pass