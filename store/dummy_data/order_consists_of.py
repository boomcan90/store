# consists_order_id, consists_isbn13, consists_qty

from store.orders.models import Order_Consists_Of

oco1 = Order_Consists_Of('oid_1', '9780439139595', 3)
oco2 = Order_Consists_Of('oid_2', '9780345803498', 5)
oco3 = Order_Consists_Of('oid_3', '9780345803498', 1)
oco4 = Order_Consists_Of('oid_4', '9780345803481', 2)
oco5 = Order_Consists_Of('oid_5', '9780545139700', 5)
oco6 = Order_Consists_Of('oid_6', '9780439358071', 4)
oco7 = Order_Consists_Of('oid_7', '9780439139595', 5)
oco8 = Order_Consists_Of('oid_8', '9780439784542', 3)
oco9 = Order_Consists_Of('oid_9', '9780439784542', 5)
oco10 = Order_Consists_Of('oid_10', '9780439784542', 15)

sample_list = []
sample_list.append(oco1)
sample_list.append(oco2)
sample_list.append(oco3)
sample_list.append(oco4)
sample_list.append(oco5)
sample_list.append(oco6)
sample_list.append(oco7)
sample_list.append(oco8)
sample_list.append(oco9)
sample_list.append(oco10)
