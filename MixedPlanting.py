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
		
def Exec_drone():
	while True:
		Exec()
			
clear()

spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)
spawn_drone(Exec_drone)