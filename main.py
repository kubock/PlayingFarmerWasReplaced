import Consts
import Initialize
import ReapSunflower
import PlantMethod
import CarePlants
import PlantDefs
#import Dinosour
i = 0
change_hat(Hats.Pumpkin_Hat)
Initialize.Exec(0,0,1)

while True:

	PlantMethod.PlantSomething2D(PlantDefs.Pumpkin1)
	PlantMethod.PlantSomething2D(PlantDefs.Pumpkin2)
	PlantMethod.PlantSomething2D(PlantDefs.Pumpkin3)
	PlantMethod.PlantSomething2D(PlantDefs.Carrot1)
	PlantMethod.PlantSomething2D(PlantDefs.Carrot2)
	PlantMethod.PlantSomething2D(PlantDefs.Sunflower1)

	CarePlants.CarePumpkin(PlantDefs.Pumpkin1)
	CarePlants.CarePumpkin(PlantDefs.Pumpkin2)
	CarePlants.CarePumpkin(PlantDefs.Pumpkin3)

	ReapSunflower.Exec()
