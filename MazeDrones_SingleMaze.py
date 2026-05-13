import Initialize
import Maze
import Consts
import PlantMethod
import PlantDefs
import CarePlants


def drone1():
	Initialize.MoveToPoint(4,4)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()

def drone2():
	Initialize.MoveToPoint(4,12)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()
	
	
def drone3():
	Initialize.MoveToPoint(4,20)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()
	
def drone4():
	Initialize.MoveToPoint(4,28)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()
	
def drone5():
	Initialize.MoveToPoint(12,4)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()

def drone6():
	Initialize.MoveToPoint(12,12)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()
	
	
def drone7():
	Initialize.MoveToPoint(12,20)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()
	
def drone8():
	Initialize.MoveToPoint(12,28)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()
	
def drone9():
	Initialize.MoveToPoint(20,4)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()

def drone10():
	Initialize.MoveToPoint(20,12)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()
	
	
def drone11():
	Initialize.MoveToPoint(20,20)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()
	
def drone12():
	Initialize.MoveToPoint(20,28)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()

def drone13():
	Initialize.MoveToPoint(28,4)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()

def drone14():
	Initialize.MoveToPoint(28,12)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()
	
	
def drone15():
	Initialize.MoveToPoint(28,20)
	while True:
		if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			break
	Maze.MainLoop()
	
def drone16():
	Initialize.MoveToPoint(28,28)
	for i in range(2):
		do_a_flip()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance,Consts.Weird_Substance_num)
	Maze.MainLoop()

clear()
spawn_drone(drone1)
spawn_drone(drone2)
spawn_drone(drone3)
spawn_drone(drone4)
spawn_drone(drone5)
spawn_drone(drone6)
spawn_drone(drone7)
spawn_drone(drone8)
spawn_drone(drone9)
spawn_drone(drone10)
spawn_drone(drone11)
spawn_drone(drone12)
spawn_drone(drone13)
spawn_drone(drone14)
spawn_drone(drone15)
spawn_drone(drone16)