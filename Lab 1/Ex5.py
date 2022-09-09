import itertools


# (a)
poker_5 = list(itertools.combinations(['♠1','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K',
                                      '♣1','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K',
                                      '♦1','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K',
                                      '♥1','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K'], 5))
print(poker_5)
print(poker_5.__len__())

# (b)
dict_values ={'♠1':1,'♠2':2,'♠3':3,'♠4':4,'♠5':5,'♠6':6,'♠7':7,'♠8':8,'♠9':9,'♠10':10,'♠J':11,'♠Q':12,'♠K':13,
              '♣1':1,'♣2':2,'♣3':3,'♣4':4,'♣5':5,'♣6':6,'♣7':7,'♣8':8,'♣9':9,'♣10':10,'♣J':11,'♣Q':12,'♣K':13,
              '♦1':1,'♦2':2,'♦3':3,'♦4':4,'♦5':5,'♦6':6,'♦7':7,'♦8':8,'♦9':9,'♦10':10,'♦J':11,'♦Q':12,'♦K':13,
              '♥1':1,'♥2':2,'♥3':3,'♥4':4,'♥5':5,'♥6':6,'♥7':7,'♥8':8,'♥9':9,'♥10':10,'♥J':11,'♥Q':12,'♥K':13}
def get_value(card):
  return dict_values[card]
def check_poker(array):
  value_array = list(map(get_value, array))
  set_value_array = set(value_array)
  # dk can 3 the khac nhau set()==3 va 1 th 1 the co so luong ==3
  if len(set_value_array) == 3 and any(value_array.count(i) == 3 for i in set_value_array):
    return True
  return False
# check_poker(poker_5[0])
# print(poker_5[0])
three_of_a_kind = []
for i in poker_5:
  check_poker(i) and three_of_a_kind.append(i)
len_three_of_a_kind= len(three_of_a_kind)


print(three_of_a_kind)
print(len_three_of_a_kind)