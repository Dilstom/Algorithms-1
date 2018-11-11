#!/usr/bin/python

import sys


#  climbing_stairs(n):
#   if n < 0:
#     return 0
#   elif n == 0:
#     return 1
#   else:
#     return climbing_stair

def climbing_stairs(n, cache=None):
  # what happens when n == 0?
  if n == 0:
    return 1
  elif n < 0:
    return 0
  # check if the cache has our answer
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      # initialize a cache. 'n+1' to include 'n' 
      cache = {i: 0 for i in range(n+1)}
      # this gives us a dictionary with keys from 0 to n and all the values = 0 
      # we can also use a list:
      # cache = [0 for i in range(n+1)]
      # make use of the array indexes  
      # now, populate the cache: 
    cache[n] = climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache) 
    return cache[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')