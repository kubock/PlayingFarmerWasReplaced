import Consts
def Exec(start_x,start_y,ground_range):
	change_hat(Hats.Pumpkin_Hat)
	do_a_flip()
	MoveToPoint(start_x,start_y)
	for i in range(ground_range):
		for i in range(ground_range):
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Soil:
				till()
			move(North)		
		for i in range(ground_range):
			move(South)
		move(East)
	for i in range(ground_range):
		move(West)

# 指定したポイントへ移動する
def MoveToPoint(target_x,target_y):
	# 現在の位置
	cur_x = get_pos_x()
	cur_y = get_pos_y()
	
	# 目的地までの距離を測定
	obverse_dx = (target_x - cur_x) % Consts.ground_range
	obverse_dy = (target_y - cur_y) % Consts.ground_range
	
	# 1巡させた場合の距離
	reverse_dx = Consts.ground_range - obverse_dx
	reverse_dy = Consts.ground_range - obverse_dy
	
	# X軸の距離と方向を決める
	if obverse_dx < reverse_dx:
		range_x = obverse_dx
		direction_x = East
	else:
		range_x = reverse_dx
		direction_x = West

	# Y軸の距離と方向を決める
	if obverse_dy < reverse_dy:
		range_y = obverse_dy
		direction_y = North
	else:
		range_y = reverse_dy
		direction_y = South
	
	# 移動する
	for i in range(range_x):
		move(direction_x)
	for i in range(range_y):
		move(direction_y)

def WaterManage():
	MoveToPoint(0,0)
	if get_water() < Consts.water_threshold and num_items(Items.Water) > Consts.water_number_th:
		for i in range(Consts.ground_range):
			for i in range(Consts.ground_range):
				while get_water() < 1:
					use_item(Items.Water)
				move(North)
			move(East)
