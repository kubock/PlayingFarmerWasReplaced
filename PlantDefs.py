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

Sunflower1 =((11,0),(5,5),Entities.Sunflower)

SunflowerList = [Sunflower1]

Cactus1 =((0,0),(10,10),Entities.Cactus)
CactusList = [Cactus1]