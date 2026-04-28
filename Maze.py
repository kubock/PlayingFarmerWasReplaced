import Initialize
import Consts

# マップ内の各点についてその属性(以下項目)を返す関数
# 座標、どこから来たか、始点からの距離
def GetMappingAttribute(distance):

# 今の座標を取得
	current_x = get_pos_x ( )
	current_y = get_pos_y ( )
	position = (current_x, current_y)

	# 移動可能な隣人リストを取得
	# 例えば(0,0)にいるならnorth_neighber=(0,1),south_neighbor=(-1,-1)…等
	north_neighbor = (-1,-1)
	east_neighbor = (-1,-1)
	south_neighbor = (-1,-1)
	west_neighbor = (-1,-1)

	if can_move(North):
		north_neighbor = (current_x, current_y + 1)
	if can_move (East):
		east_neighbor = (current_x + 1,current_y)
	if can_move(South):
		south_neighbor = (current_x, current_y - 1)
	if can_move (West):
		west_neighbor = (current_x - 1,current_y)

	neighborhood = [north_neighbor, east_neighbor , south_neighbor, west_neighbor]

	# 上記取得した情報をタプルにして返す
	# 始点からの距離は呼び出し元の方で制御しているため引数を利用
	return (position, neighborhood, distance)

# 特定の座標に行ったことがあるか(mapping_listに格納済みか)判断
def IsExistsInMappingList(position, mapping_list):
	for map_position in mapping_list:
		if position == map_position[0]:
			return map_position
	return False

# 宝箱を手に入れつつマッピングを成長させる
def GetTreasureAndGrowMapping(mapping_list):

	new_mapping_list = mapping_list

	# 今の座標を取得
	current_x = get_pos_x ( )
	current_y = get_pos_y ( )
	position = (current_x, current_y)

	current_mapping = IsExistsInMappingList (position,new_mapping_list)

	# 宝箱を見つけるまでループ
	while True:
		# 宝箱取得
		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance,Consts.Weird_Substance_num)
			break
		back_flag = True

		
	
		# 周囲の行ったことのないところに行ってみる。行ったことのないところがなければ1マス戻る
		for next_position in current_mapping[1]:
			#移動できないところは無視
			if next_position == (-1,-1):
				continue

			next_mapping = IsExistsInMappingList(next_position, new_mapping_list)

			# 自身の周囲の行ったことのないところに行ってみる
			if not next_mapping:
				# 移動先で状態を取得、mapping_listを育てて for ループを抜ける
				Initialize.MoveToPoint(next_position[0],next_position[1])
				current_mapping = GetMappingAttribute(current_mapping[2] + 1)
				new_mapping_list.append(current_mapping)
				back_flag = False
				break
			# 戻ることを仮定して1つ前の座標を取得
			elif next_mapping[2] < current_mapping[2]:
				back_position = next_position
		
		if back_flag:
			# ループを抜けた⇒ 全部行ったことある⇒1マス戻って位置情報を取得
			Initialize.MoveToPoint(back_position[0],back_position[1])
			current_mapping = IsExistsInMappingList(back_position, new_mapping_list)
	
	# 宝箱が見つかったら終わり。育てたmapping_listを戻す
	return new_mapping_list

# ルートを構築して宝箱をGetする
def CreateRouteAndGetTreasure(mapping_list):
	# 宝箱から始点までのルートを計算
	treasure_position = measure()
	route_to_treasure = CalcRouteToFirstPoint(treasure_position, mapping_list)

	# 現在の場所から始点までのルートを計算
	current_position = (get_pos_x(), get_pos_y ( ) )
	route_to_current = CalcRouteToFirstPoint(current_position, mapping_list)
	
	# ルートが交わるか調査しつつルートを合体
	cross_position = (0,0)
	merge_route = []
	for position in route_to_current:
		merge_route.append(position)
		# 交わる点を調査
		if position in route_to_treasure:
			cross_position = position
			break

	# 交わる点で切れるように宝箱までの距離を取得
	# 現在位置から交点まで+交点から宝箱まで(宝箱から交点までの逆さ)=ルート
	insert_point = len(merge_route)
	for position in route_to_treasure:
		merge_route.insert(insert_point,position)
		# 交わる点で終わり
		if position == cross_position:
			break

	# 目的の場所まで移動
	for position in merge_route:
		Initialize.MoveToPoint(position[0],position[1])

	# 宝箱を開ける
	# 宝箱取得
	if get_entity_type() == Entities.Treasure:
		use_item(Items.Weird_Substance,Consts.Weird_Substance_num)
		return True
	return False


# 特定のポイントから始点までのルートを計算する
def CalcRouteToFirstPoint(position, mapping_list):

	# 指定された場所の位置情報を取得
	current_mapping = IsExistsInMappingList (position, mapping_list)

	# 計算用変数の準備·初期化
	distance = current_mapping[2]
	route_list = [position]

	# 終点につくまで
	while distance > 0:
		for neighbor_position in current_mapping[1]:
			if neighbor_position == (-1,-1):
				continue
			next_mapping = IsExistsInMappingList(neighbor_position, mapping_list)
			# 今より距離の小さいところをリストに追加
			if next_mapping[2] < distance:
				# ルートリストに追加
				route_list.append(next_mapping[0])
				# 位置情報を更新
				current_mapping = next_mapping
				# 距離を更新
				distance = current_mapping[2]
				break

	return route_list

# 宝箱を取得する
def GetTreasure(mapping_list):

	new_mapping_list = mapping_list
	treasure_position = measure( )

	if not IsExistsInMappingList(treasure_position, mapping_list):
		# 宝箱の場所にまだ行ったことがなければ右手法で検索しつつmapping_listを育てる
		new_mapping_list = GetTreasureAndGrowMapping(mapping_list)
	else:
		# 宝箱の場所に行ったことがあればルートを構築して宝箱をGetする
		CreateRouteAndGetTreasure(mapping_list)

	return new_mapping_list

def MainLoop():

	# 初期位置での位置情報取得
	first_mapping = GetMappingAttribute(0)
	mapping_list = [first_mapping]

	while True:
		GetTreasure(mapping_list)

clear()
Initialize.MoveToPoint(0,0)
plant(Entities.Bush)
use_item(Items.Weird_Substance,Consts.Weird_Substance_num)

MainLoop()