"""OrderConsistsOf dummy data."""
# consists_order_id, consists_isbn13, consists_qty

from store.orders.models import OrderConsistsOf

oco1 = OrderConsistsOf('oid_1', '9780439139595', 3)
oco2 = OrderConsistsOf('oid_2', '9780345803498', 5)
oco3 = OrderConsistsOf('oid_3', '9780345803498', 1)
oco4 = OrderConsistsOf('oid_4', '9780345803481', 2)
oco5 = OrderConsistsOf('oid_5', '9780545139700', 5)
oco6 = OrderConsistsOf('oid_6', '9780439358071', 4)
oco7 = OrderConsistsOf('oid_7', '9780439139595', 5)
oco8 = OrderConsistsOf('oid_8', '9780439784542', 3)
oco9 = OrderConsistsOf('oid_9', '9780439784542', 5)
oco10 = OrderConsistsOf('oid_10', '9780439784542', 15)

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
