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


def dist(u1, u2):
  return Pt(u2.x - u1.x, u2.y - u1.y)

def manhattan(pt):
  return abs(pt.x) + abs(pt.y)

def directFromDist(pt):
  if pt.x == -1 and pt.y == 0:
    return 'left'
  if pt.x == 1 and pt.y == 0:
    return 'right'
  if pt.x == 0 and pt.y == -1 :
    return 'up'
  if pt.x == 0 and pt.y == 1 :
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
      
    
  #for friend in state.units:
  #  print('friend: ', friend.x, ' ', friend.y, ' (dist: ', dist(state.unit, friend))

  moveAction = Action('move', dirWalk)
  attackAction =  Action('attack', dirAttack)



  if (foundFoe):
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