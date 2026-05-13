import Consts
import PlantMethod
import PlantDefs
import CarePlants

def SunflowerDrome_1():
	use_item(Items.Water)
	use_item(Items.Fertilizer)
	PlantMethod.PlantSomething2D(PlantDefs.Sunflower1)
def SunflowerDrome_2():
	use_item(Items.Water)
	use_item(Items.Fertilizer)
	PlantMethod.PlantSomething2D(PlantDefs.Sunflower2)
def SunflowerDrome_3():
	use_item(Items.Water)
	use_item(Items.Fertilizer)
	PlantMethod.PlantSomething2D(PlantDefs.Sunflower3)
def SunflowerDrome_4():
	use_item(Items.Water)
	use_item(Items.Fertilizer)
	PlantMethod.PlantSomething2D(PlantDefs.Sunflower4)
def SunflowerDrome_5():
	use_item(Items.Water)
	use_item(Items.Fertilizer)
	PlantMethod.PlantSomething2D(PlantDefs.Sunflower5)
def SunflowerDrome_6():
	use_item(Items.Water)
	use_item(Items.Fertilizer)
	PlantMethod.PlantSomething2D(PlantDefs.Sunflower6)
def SunflowerDrome_7():
	use_item(Items.Water)
	use_item(Items.Fertilizer)
	PlantMethod.PlantSomething2D(PlantDefs.Sunflower7)
def SunflowerDrome_8():
	use_item(Items.Water)
	use_item(Items.Fertilizer)
	PlantMethod.PlantSomething2D(PlantDefs.Sunflower8)
	
def PlantCactusDrone_1():
	PlantMethod.PlantSomething2D(PlantDefs.Cactus1)
	while True:
		CarePlants.CareCactus(PlantDefs.Cactus1)
def PlantCactusDrone_2():
	PlantMethod.PlantSomething2D(PlantDefs.Cactus2)
	while True:
		CarePlants.CareCactus(PlantDefs.Cactus2)
def PlantCactusDrone_3():
	PlantMethod.PlantSomething2D(PlantDefs.Cactus3)
	while True:
		CarePlants.CareCactus(PlantDefs.Cactus3)
def PlantCactusDrone_4():
	PlantMethod.PlantSomething2D(PlantDefs.Cactus4)
	while True:
		CarePlants.CareCactus(PlantDefs.Cactus4)
def PlantCactusDrone_5():
	PlantMethod.PlantSomething2D(PlantDefs.Cactus5)
	while True:
		CarePlants.CareCactus(PlantDefs.Cactus5)
def CareCactusDrone():
	CarePlants.CareCactus(PlantDefs.Cactus_Merge)
