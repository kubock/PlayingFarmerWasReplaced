import Initialize
import Consts

# 2次元網羅的に植える
def PlantSomething2D(PlantDef):

	start_x = PlantDef[0][0]
	start_y = PlantDef[0][1]
	range_x = PlantDef[1][0]
	range_y = PlantDef[1][1]
	entity  = PlantDef[2]

	#「進む」方向の初期値は東と北
	x_direction_go = East
	y_direction_go = North

	#「戻る」方向の初期値は西と南
	x_direction_back = West
	y_direction_back = South

	# 開始位置に移動
	Initialize.MoveToPoint(start_x, start_y)
	for i in range(range_x):
		if i %2 == 0:
			# xが偶数の時はy軸は「進む」
			y_direction = y_direction_go
		else:
			# xが奇数の時はy軸は「戻る」
			y_direction = y_direction_back

		#植えて移動する
		for j in range(range_y -1):
			PlantSelector(entity)
			move(y_direction)

		# 植えて×軸に移動する
		PlantSelector (entity)
		move (x_direction_go)
	
# 植物に従って適切に植える
def PlantSelector(entity):

	ground_type = get_ground_type()

	#なにかあったらとりあえず収穫しとく
	if can_harvest() :
		harvest()

	# 木を植えたいときは特殊処理
	if entity == Entities.Tree:
		if ground_type == Ground.Soil:
			till()
		if (get_pos_x() + get_pos_y()) % 2 == 0:
			#x座標とy座標の合計が偶数の時に植えると市松模様になる
			plant(entity)
		return
		
	if entity == Entities.Bush or entity == Entities.Grass:
		# 茂みor草は耕さない
		if ground_type == Grounds.Soil:
			till()
	else:
		# 上記以外は耕す
		if ground_type != Grounds.Soil:
			till()
	plant(entity)
	