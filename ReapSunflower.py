import Initialize
import Consts
def Exec(SunfloweList):
	max = 0
	Initialize.MoveToPoint(0,0)

	# 15から0まで-1しながら二次元的に収穫
	target_num = 15
	while target_num >= 7:
	# 行単位でループ
		for i in SunfloweList:
			# 指定のエリア単位で収穫
			ReapAsArea(i,target_num)
		target_num = target_num - 1
			
# 指定されたひまわりのエリアを収穫
def ReapAsArea(SunfloweArea, target_num):

	sart_x = SunfloweArea[0][0]
	sart_y = SunfloweArea[0][1]
	x_size = SunfloweArea[1][0]
	y_size = SunfloweArea[1][1]

	reap_result = 'YetGrow'
	while reap_result == 'YetGrow':
		yet_grow = False
		# 開始位置に移動
		Initialize.MoveToPoint(sart_x, sart_y)
		current_num = 0
		for i in range(x_size):
			for j in range(y_size-1):
				
				if i % 2 == 0:					
					# 偶数行は北に移動
					direction_y = North
				else: 			
					# 奇数行は南に移動
					direction_y = South
				
				# 収穫判断して次の位置に移動
				reap_result = JudgeThrowOrReap(target_num)
				move(direction_y)

			# 行の最後まで来たら収穫判断して東に移動
			reap_result = JudgeThrowOrReap(target_num)
			move(East)

	# 最後まで回ったらtrue
	return True

def JudgeThrowOrReap(target_num):
	current_num = measure()
	if get_entity_type() != Entities.Sunflower:
		return 'Throw'

	if current_num >= target_num:
		if can_harvest():
			harvest()
			return 'Reap'
		else:
			# 指定の花びらだけど収穫できない⇒育ち切ってない判定
			return 'YetGrow'