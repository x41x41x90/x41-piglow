#!/usr/bin/env python
from piglow import PiGlow
import random
i = 0
j = 1
k = 2
piglow = PiGlow()
piglow.all(0)
goingUp = 1


while True:
	if goingUp == 1:
		piglow.colour(j, i)
		i+=1
	else:
		piglow.colour(j, i)
		i-=1

	if i == 256:
		goingUp = 0
	if i == -1:
		goingUp = 1
		
		j = random.randint(1,6)
