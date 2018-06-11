#Add sample comments
def coins1(cents):
  count = 0
  for c in range(cents, -1, -25):
    count += coins1_pnd(c)
  return count

def coins1_pnd(cents):
  count = 0
  for c in range(cents, -1, -10):
    count += (c / 5) + 1
  return count

def coins2(cents):
  n = cents / 5
  return int(n*n*n/60.0 + n*n*9/40.0 + n*53/60.0 + 301/240.0)

