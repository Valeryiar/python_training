from model.group import Group
import random
import string

constant = [
    Group (name="name1", header="header1", footer = "footer1")
]

def random_string(prefix, maxlen):
    symbols = string.digits+""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] #+ [
  #  Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
  #  for i in range(3)
#]