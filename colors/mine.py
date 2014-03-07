#!/usr/bin/env python
from piglow import PiGlow
import time
import random
i = 0
j = 1
k = 2
piglow = PiGlow()
piglow.all(0)
goingUp = 1


while True:
	time.sleep(.03)
	if goingUp == 1:
		piglow.colour(j, i)
		i+=5
	else:
		piglow.colour(j, i)
		i-=5

	if i == 255:
		goingUp = 0
	if i == 0:
		piglow.colour(j, i)
		goingUp = 1
		
		j = random.randint(1,6)
