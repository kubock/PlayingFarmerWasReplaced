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
	return (neighborhood, distance)

# 宝箱を手に入れつつマッピングを成長させる
def GetTreasureAndGrowMapping(mapinfo_dict):

	new_mapinfo_dict = mapinfo_dict
	current_treasure = measure()

	# 今の座標を取得
	current_x = get_pos_x ( )
	current_y = get_pos_y ( )
	current_position = (current_x, current_y)
	current_mapinfo = new_mapinfo_dict[current_position]

	# 宝箱を見つけるまでループ
	while True:

		new_treasure = measure()
		if new_treasure != current_treasure:
			# 宝箱の場所が変わった ⇒ 宝箱を見つけた ⇒ ループを抜ける
			break

		# 宝箱取得
		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance,Consts.Weird_Substance_num)
			break
		go_another_flag = False
		first_Flag = False 
		# 周囲の行ったことのないところに行ってみる。行ったことのないところがなければ1マス戻る
		neighbor_list = current_mapinfo[0]
		for next_position in neighbor_list:
			#移動できないところは無視
			if next_position == (-1,-1):
				continue
			
			# 自身の周囲の行ったことのないところに行ってみる
			if not next_position in new_mapinfo_dict:
				# 移動先で状態を取得、mapinfo_dictを育てて for ループを抜ける
				Initialize.MoveToPoint(next_position[0],next_position[1])
				current_mapinfo = GetMappingAttribute(current_mapinfo[1] + 1)
				new_mapinfo_dict[next_position] = (current_mapinfo[0], current_mapinfo[1])
				go_another_flag = True
				break
			# 戻ることを仮定して1つ前の座標を取得
			elif new_mapinfo_dict[next_position][1] < current_mapinfo[1]:
				back_position = next_position
				
			# 始点に戻ってしまっていたらそれ用の対応を行う
			elif current_mapinfo[1] == 0:
				first_Flag = True
				
		if first_Flag:
			#first_Flagがtrue ⇒ 始点でループしている ⇒ 別の場所に行く
			new_mapinfo_dict = GoToNeverBeenPoint(new_mapinfo_dict)
			current_x = get_pos_x ( )
			current_y = get_pos_y ( )
			current_position = (current_x, current_y)
			current_mapinfo = new_mapinfo_dict[current_position]
			
			continue
		
		if not go_another_flag:
			# go_another_flagがfalse ⇒ 全部行ったことある ⇒ 1マス戻って位置情報を取得
			Initialize.MoveToPoint(back_position[0],back_position[1])
			current_mapinfo = new_mapinfo_dict[back_position]

			# mapinfo_dictの情報を更新
			current_mapinfo_update = GetMappingAttribute(current_mapinfo[1])
			new_mapinfo_dict[back_position] = (current_mapinfo_update[0], current_mapinfo_update[1])
			current_mapinfo = new_mapinfo_dict[back_position]

			current_position = back_position

	# 宝箱が見つかったら終わり。育てたmapinfo_dictを戻す
	return new_mapinfo_dict

# ルートを構築して宝箱をGetする
def CreateRouteAndGetTreasure(mapinfo_dict):

	# 宝箱から始点までのルートを計算
	treasure_position = measure()
	route_to_treasure = CalcRouteToFirstPoint(treasure_position, mapinfo_dict)

	# 現在の場所から始点までのルートを計算
	current_position = (get_pos_x(), get_pos_y ( ) )
	route_to_current = CalcRouteToFirstPoint(current_position, mapinfo_dict)
	
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

	new_mapinfo_dict = mapinfo_dict
	# 目的の場所まで移動
	for position in merge_route:
		Initialize.MoveToPoint(position[0],position[1])
		
		# mapinfo_dictの情報を更新
		current_mapinfo = new_mapinfo_dict[position]
		current_mapinfo_update = GetMappingAttribute(current_mapinfo[1])
		new_mapinfo_dict[position] = (current_mapinfo_update[0], current_mapinfo_update[1])
		new_treasure = measure()
		if new_treasure != treasure_position:
			# 宝箱の場所が変わった ⇒ 宝箱を見つけた ⇒ ループを抜ける
			return new_mapinfo_dict

	# 宝箱を開ける
	# 宝箱取得
	if get_entity_type() == Entities.Treasure:
		use_item(Items.Weird_Substance,Consts.Weird_Substance_num)
	
	return new_mapinfo_dict


# 特定のポイントから始点までのルートを計算する
def CalcRouteToFirstPoint(position, mapinfo_dict):

	# 指定された場所の位置情報を取得
	current_mapinfo = mapinfo_dict[position]

	# 計算用変数の準備·初期化
	distance = current_mapinfo[1]
	route_list = [position]

	# 終点につくまで
	while distance > 0:
		for neighbor_position in current_mapinfo[0]:
			# 移動できないところと行ったこと無いところは無視
			if neighbor_position == (-1,-1) or not neighbor_position in mapinfo_dict:
				continue

			next_mapinfo = mapinfo_dict[neighbor_position]
			# 今より最も距離の小さいところを取得
			if next_mapinfo[1] <= distance:
				next_position = neighbor_position
				distance = current_mapinfo[1]
		
		# ルートリストに追加
		route_list.append(next_position)
		current_mapinfo = mapinfo_dict[next_position]

	return route_list

# 宝箱を取得する
def GetTreasure(mapinfo_dict):

	new_mapinfo_dict = mapinfo_dict
	treasure_position = measure()

	if not treasure_position in mapinfo_dict:
		# 宝箱の場所にまだ行ったことがなけれ虱潰しで検索しつつmapinfo_dictを育てる
		new_mapinfo_dict = GetTreasureAndGrowMapping(mapinfo_dict)
	else:
		# 宝箱の場所に行ったことがあればルートを構築して宝箱をGetする
		new_mapinfo_dict = CreateRouteAndGetTreasure(mapinfo_dict)
	return new_mapinfo_dict

# mapign_dictを育てるために、行ったことのないところを探して行ってみる
# 例えば、(0,0)まで戻ってしまってループにハマった場合に実行する
def GoToNeverBeenPoint(mapinfo_dict):
	
	#初期値はmapinfo_dictのキーの中に最初に登録された値
	next_position = list(mapinfo_dict)[0]	

	# mapinfo_dictの１つ目の要素は周囲の移動可能な座標リストである。
	# その中で更にmapinfo_dictにないものが到達可能かつまだ行ったことがない場所になる。
	for key in mapinfo_dict:
		neighbor_list = mapinfo_dict[key][0]
		for neighbor in neighbor_list:
			if neighbor in mapinfo_dict or neighbor == (-1,-1):
				continue
			else:
				# 行ったことのない座標があればそこに行ってみる
				next_position = key
				break
	
	# ルートを構築
	route_list = CalcRouteToFirstPoint(next_position, mapinfo_dict)
	
	# ルートを逆さにして、目的の場所まで移動
	reverse_route_list = []
	for position in route_list:
		reverse_route_list.insert(0,position)

	new_mapinfo_dict = mapinfo_dict
	for position in reverse_route_list:
		Initialize.MoveToPoint(position[0],position[1])
		
		# mapinfo_dictの情報を更新
		current_mapinfo = new_mapinfo_dict[position]
		current_mapinfo_update = GetMappingAttribute(current_mapinfo[1])
		new_mapinfo_dict[position] = (current_mapinfo_update[0], current_mapinfo_update[1])
	
	return new_mapinfo_dict

def MainLoop():

	# 初期位置での位置情報取得
	first_mapinfo = GetMappingAttribute(0)
	mapinfo_dict = {(get_pos_x(),get_pos_y()):(first_mapinfo)}
	i = 0
	while i <= 300:
		i = i + 1
		GetTreasure(mapinfo_dict)
		
	if get_entity_type() == Entities.Treasure:
		harvest()
