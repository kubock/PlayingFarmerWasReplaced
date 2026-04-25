import Initialize
import Consts

def Exec():
	entity = get_companion()[0]
	point_x =get_companion()[1][0]
	point_y =get_companion()[1][1]
	
	Initialize.MoveToPoint(point_x,point_y)
	while True:
		use_item(Items.Water)
		if can_harvest():
			harvest()
			break
		if get_entity_type() == None:
			break
			
	if entity == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()
	elif get_ground_type() == Grounds.Soil:
		till()
	
	plant(entity)	
	
	while num_items(Items.Power) < Consts.power_threshold:
		ReapSunflower.Exec()
		change_hat(Hats.Pumpkin_Hat)

#Initialize.Exec(0,0,Consts.ground_range)
while True:
	Exec()