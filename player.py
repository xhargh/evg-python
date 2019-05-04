# Logic for controlling units

#  .  x  .
#  x  o  H
#  .  x  .

from game import Action, is_empty, Unit, GameState, build_distance_map
from random import randint

def dist(u1, u2):
  return [u2.x - u1.x, u2.y - u1.y]

def manhattan(vec):
  return abs(vec[0]) + abs(vec[1])

def directFromDist(vec):
  if vec[0] == -1 and vec[1] == 0:
    return 'left'
  if vec[0] == 1 and vec[1] == 0:
    return 'right'
  if vec[0] == 0 and vec[1] == -1 :
    return 'up'
  if vec[0] == 0 and vec[1] == 1 :
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