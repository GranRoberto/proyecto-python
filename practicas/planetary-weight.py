# Write code below 💖

dp = int(input('Insert the number of your destination planet between 1 and 7: '))
ew = float(input('Insert your weight: '))
rg = 0

if dp == 1:
  rg = 0.38
  print(f'Your weight in Mercury is {ew * rg}')
elif dp == 2:
  rg = 0.91
  print(f'Your weight in Venus is {ew * rg}')
elif dp == 3:
  rg = 0.38
  print(f'Your weight in Mars is {ew * rg}')
elif dp == 4:
  rg = 2.53
  print(f'Your weight in Jupiter is {ew * rg}')
elif dp == 5:
  rg = 1.07
  print(f'Your weight in Saturn is {ew * rg}')
elif dp == 6:
  rg = 0.89
  print(f'Your weight in Uranus is {ew * rg}')
elif dp == 7:
  rg = 1.14
  print(f'Your weight in Neptune is {ew * rg}')
else:
  print('Invalid planet number')