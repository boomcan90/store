"""Customer dummy data."""
# id, email, m_credit_no, phone_no, address, password=None"""10 fake people."""

from store.customer.models import Customer
# id, email, m_credit_no, phone_no, address, password=None
c1 = Customer('cid1', 'cid1@email.com', '1234531', '987654321', '1, coolstreet', 'abcd', active=True)
# id, email, m_credit_no, phone_no, address, password=None
c2 = Customer('cid2', 'cid2@email.com', '1234532', '987654322', '2, coolstreet', 'abcd', active=True)
# id, email, m_credit_no, phone_no, address, password=None
c3 = Customer('cid3', 'cid3@email.com', '1234533', '987654323', '3, coolstreet', 'abcd', active=True)
# id, email, m_credit_no, phone_no, address, password=None
c4 = Customer('cid4', 'cid4@email.com', '1234534', '987654324', '4, coolstreet', 'abcd', active=True)
# id, email, m_credit_no, phone_no, address, password=None
c5 = Customer('cid5', 'cid5@email.com', '1234535', '987654325', '5, coolstreet', 'abcd', active=True)
# id, email, m_credit_no, phone_no, address, password=None
c6 = Customer('cid6', 'cid6@email.com', '1234536', '987654326', '6, coolstreet', 'abcd', active=True)
# id, email, m_credit_no, phone_no, address, password=None
c7 = Customer('cid7', 'cid7@email.com', '1234537', '987654327', '7, coolstreet', 'abcd', active=True)
# id, email, m_credit_no, phone_no, address, password=None
c8 = Customer('cid8', 'cid8@email.com', '1234538', '987654328', '8, coolstreet', 'abcd', active=True)
# id, email, m_credit_no, phone_no, address, password=None
c9 = Customer('cid9', 'cid9@email.com', '1234539', '987654329', '9, coolstreet', 'abcd', active=True)
# id, email, m_credit_no, phone_no, address, password=None
c10 = Customer('cid10', 'cid10@email.com', '1234540', '987654330', '10, coolstreet', 'abcd', active=True)

sample_list = []
sample_list.append(c1)
sample_list.append(c2)
sample_list.append(c3)
sample_list.append(c4)
sample_list.append(c5)
sample_list.append(c6)
sample_list.append(c7)
sample_list.append(c8)
sample_list.append(c9)
sample_list.append(c10)
