import math
def bisection(function, a, b):#找方程在[a,b]中的解
  start = a
  end = b
  if function(a) == 0:
    return a
  else function(b) == 0:
    return b
  elif function(a) * function(b) > 0；
    print("couldn't find the root in [a, b")
    return
  else:
    mid = (start + end) / 2.0
    while abs(start - mid) > 10**-7:
      if function(mid) == 0:
        return mid
      elif function(mid) * function(start) < 0:
        end = mid
      else:
        start = mid
def f(x):
  return math.power(x, 3) - 2*x -5
if __name__ == '__main__':
  print(bisection(f, 1, 1000))
