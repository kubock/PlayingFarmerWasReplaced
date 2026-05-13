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

def CareUnitPumpkin():
	cared_flag = False
	if not can_harvest():
		cared_flag = True
	if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None :
		plant(Entities.Pumpkin)
		use_item(Items.Water)
	return cared_flag

def CareCactus(plantdef):
	
	# 位置とサイズを取得
	start_x = plantdef[0][0]
	start_y = plantdef[0][1]
	cactus_size_x = plantdef[1][0]
	cactus_size_y = plantdef[1][1]

	#「進む」方向の初期値は東と北
	x_direction_go = East
	y_direction_go = North

	#「戻る」方向の初期値は西と南
	x_direction_back = West
	y_direction_back = South
	
	sorted_flag = True
	while sorted_flag:
		# 開始位置に移動
		Initialize.MoveToPoint(start_x, start_y)
		sorted_flag = False
		# 平面でサボテンをソート
		for i in range(cactus_size_x):
			if i % 2 == 0:
				# xが偶数の時はy軸を「進む」
				y_direction = y_direction_go
			else:
				# xが奇数の時はy軸を「戻る」
				y_direction = y_direction_back

			# ソートしてY軸方向を移動
			for j in range(cactus_size_y -1) :
				sorted_flag = SortCactus(sorted_flag)
				move(y_direction)
			
			# 走査してX軸方向を移動
			sorted_flag = SortCactus(sorted_flag)
			move(x_direction_go)

# 今いる位置を基準としたサボテンのソート
def SortCactus(sorted_flag):
	
	# 周囲の数値を取得
	current_num = measure()
	position_x = get_pos_x()
	position_y = get_pos_y()
	 
	current_num = measure()		
	north_num = measure(North)
	east_num = measure(East)
	
	# 周囲の数値と比較してソート
	if current_num != None:
		if position_y < Consts.ground_range - 1:
			#北と東を大きくなるようにソート
			if north_num != None and current_num > north_num:
				swap(North)
				current_num = north_num
				sorted_flag = True
		
		if position_x < Consts.ground_range - 1:
			if east_num != None and current_num > east_num:
				swap(East)
				current_num = east_num
				sorted_flag = True
		
	return sorted_flag

def GrowPlants(start_x, start_y, size_x, size_y, fertilizer_flag):
	#「進む」方向の初期値は東と北
	x_direction_go = East
	y_direction_go = North

	#「戻る」方向の初期値は西と南
	x_direction_back = West
	y_direction_back = South
	
	sorted_flag = True
	while sorted_flag:
		# 開始位置に移動
		Initialize.MoveToPoint(start_x, start_y)
		sorted_flag = False
		# 平面でサボテンをソート
		for i in range(size_x):
			if i % 2 == 0:
				# xが偶数の時はy軸を「進む」
				y_direction = y_direction_go
			else:
				# xが奇数の時はy軸を「戻る」
				y_direction = y_direction_back

			# 水やりしてY軸方向を移動
			for j in range(size_y -1) :
				use_item(Items.Water)
				if fertilizer_flag:
					use_item(Items.Fertilizer)
				move(y_direction)
			
			# 水やりしてX軸方向を移動
			use_item(Items.Water)
			if fertilizer_flag:
				use_item(Items.Fertilizer)
			move(x_direction_go)
