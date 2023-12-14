c=0
ok=0
def ura(a):
  a=int(a)
  global c
  global ok
  def okey(a):
    global ok
    if ((a%10) != 0):
      ok+=1
      return okey(a//10)
    else:
      return ok
  b=0
  if b < okey(a):
    a=str(a)
    c1=a[b]
    c+=int(c1)
    b+=1
    return ura(a)
  else:
    return c
print(ura(int(input())))
print('hfgf')