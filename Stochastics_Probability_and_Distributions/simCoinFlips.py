import random
from flippingCoins import coinFlip,flipSim

#print('10 trials of 10 flips each')
#print(flipSim(10,10))

#print('10 trials of 100 flips each')
#print(flipSim(100,10))

print('10 trials of 1000 flips each')
print(0.5-flipSim(1000,10))


print('10 trials of 50000 flips each')
print(0.5-flipSim(50000,10))


print('10 trials of 100000 flips each')
print(0.5-flipSim(100000,10))


print('10 trials of 500000 flips each')
print(0.5-flipSim(500000,10))


print('10 trials of 1000000 flips each')
print(0.5-flipSim(1000000,10))

print('now the other way. 1000 trials of 10 flips each.')
print(0.5-flipSim(10,1000))

print('50000 trials of 10 flips each')
print(0.5-flipSim(10,50000))

print('100000 trials of 10 flips each')
print(0.5-flipSim(10,100000))

print('500000 trials of 10 flips each')
print(0.5-flipSim(10,500000))

print('1000000 trials of 10 flips each')
print(0.5-flipSim(10,1000000))
