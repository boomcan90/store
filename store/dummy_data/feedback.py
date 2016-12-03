"""Feedback dummy data."""

from store.feedback.models import Feedback

fb1 = Feedback("cid1", "9780439139595", 5, short_text="Goblet of fire is very firey!")
fb2 = Feedback("cid2", "9780439139595", 1, short_text="Goblet of fire is too hot! I got burnt ):")
fb3 = Feedback("cid3", "9780439139595", 4, short_text="Dragons! How to train a dragon!?")

sample_list = []
sample_list.append(fb1)
sample_list.append(fb2)
sample_list.append(fb3)