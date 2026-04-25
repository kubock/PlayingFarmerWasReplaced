import Initialize
Initialize.MoveToPoint(0,0)
harvest()

if get_entity_type() != Grounds.Soil:
	till()

plant(Entities.Bush)

use_item(Items.Weird_Substance,64)
harvest()