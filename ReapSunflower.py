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

	yet_grow = True
	while yet_grow:
		yet_grow = False
		# 開始位置に移動
		Initialize.MoveToPoint(sart_x, sart_y)
		for i in range(x_size):
			for j in range(y_size-1):
				
				if i % 2 == 0:					
					# 偶数行は北に移動
					direction_y = North
				else: 			
					# 奇数行は南に移動
					direction_y = South
				current_num = measure()
				if current_num >= target_num:
					if can_harvest():
						harvest()
					else:
						# 指定の花びらだけど収穫できない⇒育ち切ってない判定
						yet_grow = True
				# 次の位置に移動
				move(direction_y)
			# 行の最後まで来たら東に移動
			if current_num >= target_num:
				if can_harvest():
					harvest()
				else:
					# 指定の花びらだけど収穫できない⇒育ち切ってない判定
					yet_grow = True
			move(East)				
	# 最後まで回ったらtrue
	return True