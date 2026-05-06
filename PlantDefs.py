import Consts
# 植物を植える定義
# 1つ目：開始位置　2つ目：X,Yのサイズ　3つ目：植えるもの

Pumpkin1 = ((0,0),(10,10),Entities.Pumpkin)
Pumpkin2 = ((0,11),(10,10),Entities.Pumpkin)
Pumpkin3 = ((0,22),(10,10),Entities.Pumpkin)
PunkinList=[Pumpkin1,Pumpkin2,Pumpkin3]

Carrot1 =((0,10),(10,1),Entities.Carrot) 
Carrot2 =((0,21),(10,1),Entities.Carrot) 
CarrotV1 =((10,0),(1,Consts.ground_range),Entities.Carrot) 
CarrotList=[Carrot1,Carrot2,CarrotV1]

Sunflower1 =((0,0),(1,8),Entities.Sunflower)
Sunflower2 =((1,0),(1,8),Entities.Sunflower)
Sunflower3 =((2,0),(1,8),Entities.Sunflower)
Sunflower4 =((3,0),(1,8),Entities.Sunflower)
Sunflower5 =((4,0),(1,8),Entities.Sunflower)
Sunflower6 =((5,0),(1,8),Entities.Sunflower)
Sunflower7 =((6,0),(1,8),Entities.Sunflower)
Sunflower8 =((7,0),(1,8),Entities.Sunflower)
	
SunflowerList = [Sunflower1,Sunflower2,Sunflower3,Sunflower4,Sunflower5,Sunflower6,Sunflower7,Sunflower8]

Cactus1 =((0,0),(3,15),Entities.Cactus)
Cactus2 =((3,0),(3,15),Entities.Cactus)
Cactus3 =((6,0),(3,15),Entities.Cactus)
Cactus4 =((9,0),(3,15),Entities.Cactus)
Cactus5 =((12,0),(3,15),Entities.Cactus)

Cactus_Merge =((0,0),(15,15),Entities.Cactus)
CactusList = [Cactus1,Cactus2,Cactus3,Cactus4,Cactus5]