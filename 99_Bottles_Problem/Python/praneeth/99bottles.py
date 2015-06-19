__author__ = 'praneeth'
x = 99
  for i in range(99):
    w = 'Take one down and pass it around, '+str((x-(i+1)))+' bottle of beer on the wall.'
    y = str((x-i))+' bottles of beer on the wall, '+str((x-i))+' bottles of beer'
    z = 'Go to the Store and buy some more, '+str(x)+' bottle of beer on the wall.'
    if i == (x-1):
        print(y + '\n' + z)
    else:
        print(y + '\n' + w)
    i += 1
