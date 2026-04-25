import Initialize
import Consts
def Exec():
	max = 0
	Initialize.MoveToPoint(0,0)
	SunflowerCols_List=[]
	# ヒマワリの列を取得
	for i in range(Consts.ground_range):
		if get_entity_type()==Entities.Sunflower:
			SunflowerCols_List.append(i)
		move(East)
	
	# 15から0まで-1しながら二次元的に収穫
	target_num = 15
	while target_num >= 7:
	# 行単位でループ
		for i in SunflowerCols_List:
			# 列単位で収穫
			ReapAsCol(i, 0, target_num, Consts.ground_range)
		target_num = target_num - 1
			
# 指定された列の指定された花びらのヒマワリを収穫する。ヒマワリか否かの判定はしない
def ReapAsCol(x, y, target_num, ground_range):
	yet_grow = True
	while yet_grow:
		yet_grow = False
		# 開始位置に移動
		Initialize.MoveToPoint(x, y)
		for i in range(ground_range):
			current_num = measure()
			if current_num == target_num:
				if can_harvest() :
					harvest()
				else:
					# 指定の花びらだけど収穫できない⇒育ち切ってない判定
					yet_grow = True
					break
			move(North)
	# 最後まで回ったらtrue
	return True