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

def directFromDist(pt):
  if pt.x <= -1:
    return 'left'
  elif pt.x >= 1:
    return 'right'
  elif pt.y <= -1 :
    return 'up'
  elif pt.y >= 1 :
    return 'down'

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

  # Slå direkt
  for foe in state.foes:
    if (foe.health == 0):
      continue
    foeDist = dist(state.unit, foe)
    manh = manhattan(foeDist)
    print('foe: ', foe.x, ' ', foe.y, ' (dist: ', foeDist,   ' manh: ', manh, ')')
    if (manh == 1):
      print('found foe')
      dirAttack = directFromDist(foeDist)
      foundFoe = True
      break

  # Gå ett steg, slå sen
  if not foundFoe:
    for foe in state.foes:
      if (foe.health == 0):
        continue
      foeDist = dist(state.unit, foe)
      manh = manhattan(foeDist)
      print('foe: ', foe.x, ' ', foe.y, ' (dist: ', foeDist,   ' manh: ', manh, ')')
      if (manh == 2):
        print('found foe closeby')
        dirWalk = directFromDist(foeDist)
        foundFoe = True
        currentPt = Pt(state.unit.x, state.unit.y)
        currentPt.go(dirWalk)
        foeDist = dist(currentPt, foe)
        dirAttack = directFromDist(foeDist)
        needToWalk = True
        break

  moveAction = Action('move', dirWalk)
  attackAction =  Action('attack', dirAttack)

  if (needToWalk):
    actions = [moveAction, attackAction]
  elif (foundFoe):
    actions = [attackAction]
  else:
    actions = [moveAction]

  return actions

def get_player_info():
  print('get_player_info asf' )
  return {
    "id": "Rust",
    "name": "Rust"
  }

def game_end():
  pass