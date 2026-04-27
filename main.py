import Consts
import Initialize
import ReapSunflower
import PlantMethod
import CarePlants
import PlantDefs
import Plantdef_HELLOWORLD


clear()
#import Dinosour
i = 0
change_hat(Hats.Pumpkin_Hat)
#Initialize.Exec(0,0,1)

while True:
	PlantMethod.PlantSomething2D(PlantDefs.Cactus1)
	spawn_drone(CarePlants.CareCactus(PlantDefs.Cactus1))


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