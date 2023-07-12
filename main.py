def is_jagged(lst):
  len_lst = len(lst)
  if len_lst <= 1:
    return False

  len_first_row = len(lst[0])

  for i in range(1, len_lst):
    if len_first_row != len(lst[i]):
      return True

  return False

l = [[1,2,3], [4,5,6,7], [8,9,0]]
print(is_jagged(l)) # True

l = [[1,2,3], [4,5,6], [7,8,9]]
print(is_jagged(l)) # False

l = [[1,2,3]]
print(is_jagged(l)) # False

l = []
print(is_jagged(l)) # False