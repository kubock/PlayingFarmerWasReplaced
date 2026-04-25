import Initialize
import Consts
def CarePumpkin(plantdef):
	# 位置とサイズを取得

	start_x = plantdef[0][0]
	start_y = plantdef[0][1]
	pumpkin_size = plantdef[1][0]
	
	# 開始位置に移動
	Initialize.MoveToPoint(start_x, start_y)

	#「進む」方向の初期値は東と北
	x_direction_go = East
	y_direction_go = North

	#「戻る」方向の初期値は西と南
	x_direction_back = West
	y_direction_back = South
	
	need_care = False
	need_care_list = []
	# 走査してケアが必要なかぼちゃをリストに取得
	for i in range(pumpkin_size):
		if i % 2 == 0:
			# xが偶数の時はy軸を「進む」
			y_direction = y_direction_go
		else:
			# xが奇数の時はy軸を「戻る」
			y_direction = y_direction_back

		# 走査してY軸方向を移動
		for j in range(pumpkin_size -1) :
			if not can_harvest():
				point = get_pos_x(), get_pos_y()
				need_care_list.append(point)
				
				need_care = True
			move(y_direction)
		
		# 走査してX軸方向を移動
		if not can_harvest ():
			need_care_list.append((get_pos_x(),get_pos_y ()))
			need_care = True
		move(x_direction_go)

	# いらないなら終わり
	if not need_care:
		return

	#一つずつケアしていく
	for point in need_care_list:
		Initialize.MoveToPoint(point[0], point[1])
		cared_flag = True
		# ケア完了までやる
		while cared_flag:
			cared_flag = CareUnitPumpkin()

def CareUnitPumpkin() :

	cared_flag = False

	if not can_harvest():
		cared_flag = True
	
	if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None :
		plant(Entities.Pumpkin)
		use_item(Items.Water)
	
	return cared_flag