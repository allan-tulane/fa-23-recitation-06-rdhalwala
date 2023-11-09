def fib_recursive(n, counts):
  """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """
  counts[n] += 1
  ###TODO
  #base case
  if n <= 1:
    return n
  else:
    #Recursive
    return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)


def fib_top_down(n, fibs):
  ###TODO
  if fibs[n] != -1:
    return fibs[n]
  elif n <= 1:
    fibs[n] = n
  else:
    fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)
  return fibs[n]


def fib_bottom_up(n):
  ###TODO
  ran = range(2, n + 1)
  result = 0
  x = 0
  y = 1
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    for i in ran:
      result = x + y
      x = y
      y = result
    return result
