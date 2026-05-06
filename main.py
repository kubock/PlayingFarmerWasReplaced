import Consts
import Initialize
import ReapSunflower
import PlantMethod
import PlantDefs
import CarePlants
import Plantdef_HELLOWORLD
import DroneControl

#clear()
#import Dinosour
i = 0
change_hat(Hats.Pumpkin_Hat)
#Initialize.Exec(0,0,1)

def PlantCactus():
	spawn_drone(DroneControl.PlantCactusDrone_1)
	spawn_drone(DroneControl.PlantCactusDrone_2)
	spawn_drone(DroneControl.PlantCactusDrone_3)
	spawn_drone(DroneControl.PlantCactusDrone_4)
	spawn_drone(DroneControl.PlantCactusDrone_5)
	wait_for(spawn_drone(DroneControl.CareCactusDrone))

def SunFlowerAsDrone():
	spawn_drone(DroneControl.SunflowerDrome_1)
	spawn_drone(DroneControl.SunflowerDrome_2)
	spawn_drone(DroneControl.SunflowerDrome_3)
	spawn_drone(DroneControl.SunflowerDrome_4)
	wait_for(spawn_drone(DroneControl.SunflowerDrome_5))
	
	
Initialize.MoveToPoint(0,0)
while True:
	spawn_drone(Initialize.WaterManage)
	SunFlowerAsDrone()
	
while True:
	if harvest():
		harvest()
	clear()
	spawn_drone(Initialize.WaterManage)
	wait_for(spawn_drone(PlantCactus))


#while True:
#	PlantMethod.PlantSomething2D(PlantDefs.Cactus1)
#	spawn_drone(CarePlants.CareCactus(PlantDefs.Cactus1))	
#	CarePlants.CareCactus(PlantDefs.Cactus1)


#	for i in PlantDefs.PunkinList:
#		PlantMethod.PlantSomething2D(i)	


#	for i in PlantDefs.CarrotList:
#		PlantMethod.PlantSomething2D(i)	

#	for i in PlantDefs.SunflowerList:
#		PlantMethod.PlantSomething2D(i)	
#	ReapSunflower.Exec(PlantDefs.SunflowerList)
		


#	PlantMethod.PlantSomething2D(PlantDefs.Pumpkin1)
#	PlantMethod.PlantSomething2D(PlantDefs.Pumpkin2)
#	PlantMethod.PlantSomething2D(PlantDefs.Carrot1)
#	PlantMethod.PlantSomething2D(PlantDefs.Carrot2)
#	PlantMethod.PlantSomething2D(PlantDefs.Sunflower1)
#
#	CarePlants.CarePumpkin(PlantDefs.Pumpkin1)
#	CarePlants.CarePumpkin(PlantDefs.Pumpkin2)
#