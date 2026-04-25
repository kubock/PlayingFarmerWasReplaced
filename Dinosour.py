import Initialize
import Consts
def Shorted_Distance():
	next_x = measure()[0]
	next_y = measure()[1]
	
	current_x = get_pos_x()
	current_y = get_pos_y()
	
	if next_x > current_x:
		direction_x = East
	else:
		direction_x = West
	
	if next_y > current_y:
		direction_y = North
	else:
		direction_y = South
	
	while (get_pos_x() !=next_x):
		if move(direction_x) == False:
			change_hat(Hats.Dinosaur_Hat)
			return		

	while(get_pos_y() !=next_y):
		if move(direction_y) == False:
			change_hat(Hats.Dinosaur_Hat)
			return

def WalkOnePass():
	for i in range(Consts.ground_range):
	
		if i == 0:
			direction_y = North
			range_y = Consts.ground_range -1
		elif i == Consts.ground_range - 1:
			direction_y = South
			range_y = Consts.ground_range -1
		elif i % 2 == 0:
			direction_y = North
			range_y = Consts.ground_range - 2
		else:
			direction_y = South
			range_y = Consts.ground_range - 2
		
		for j in range(range_y):
			if not move(direction_y):
				change_hat(Hats.Dinosaur_Hat)
				move(direction_y)
		if i < Consts.ground_range -1:
			if not move(East):
				change_hat(Hats.Dinosaur_Hat)
				move(East)
	
	for i in range(Consts.ground_range - 1):
		if not move(West):
			change_hat(Hats.Dinosaur_Hat)
			move(West)

Initialize.MoveToPoint(0,0)
change_hat(Hats.Dinosaur_Hat)
while True:
	WalkOnePass()