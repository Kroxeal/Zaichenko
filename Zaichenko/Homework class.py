# # 1
# class Summ:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def set_a(self, a):
#         self.a = a
#
#     def set_b(self, b):
#         self.b = b
#
#     def get_a(self):
#         return self.a
#
#     def get_b(self):
#         return self.b
#
#     def summ(self):
#         return self.a + self.b
#
#     def maxx(self):
#         if self.a > self.b:
#             return self.a
#         else:
#             return self.b
#
#
# obj = Summ(10, 20)
# print(obj.get_a())
# obj.set_a(100)
# print(obj.get_a())
# print(obj.maxx())
# =======================
# # 2
# class Counter:
#
#     def __init__(self, count=0, fromm=0, too=100):
#         self.count = count
#         self.fromm = fromm
#         self.too = too
#
#     def number_plus(self):
#         if self.count < self.too:
#             self.count += 1
#         else:
#             print("Out of range")
#
#     def number_minus(self):
#         if self.count > self.fromm:
#             self.count -= 1
#         else:
#             print("Out of range")
#
#     def get(self):
#         return self.count
#
#
# c = Counter(10, 1, 11)
# print(c.get())
# c.number_plus()
# print(c.get())
# c.number_plus()
# print(c.get())
# =======================
# # 3
# class Shop:
#
#     def __init__(self):
#         self.items = {}
#
#     def add_som(self, name: str, quantity: int):
#         self.items.update({name: quantity})
#
#     def del_som(self, name: str, quantity=0):
#         if quantity == 0:
#             self.items.pop(name)
#         elif self.items[name] <= quantity:
#             self.items.pop(name)
#         else:
#             self.items.update({name: self.items.get(name) - quantity})
#
#     def search(self, name: str):
#         return name, self.items.get(name)
#
#     def show_products(self):
#         return self.items
#
#
# sh = Shop()
# sh.add_som("Milk", 20)
# sh.add_som("Parrot", 49)
# sh.add_som("Bread", 45)
# print(sh.show_products())
# sh.del_som("Milk")
# print(sh.show_products())
# print(sh.search("Bread"))
# ==============================
# # 4
# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.money_in = 0
#
#     def can_add(self, monet):
#         if self.capacity - self.money_in >= monet:
#             return True
#         else:
#             return False
#
#     def add(self, monet):
#         if self.can_add(monet):
#             self.money_in += monet
#             return self.money_in
#         else:
#             return False
#
#
# mon = MoneyBox(9)
# print(mon.can_add(5))
# print(mon.add(10))
# =======================
# dop tasks
# # 1
# class Storage:
#
#     def __init__(self):
#         self.items = {}
#
#     def add_stor(self, name, quantity):
#         self.items.update({name: quantity})
#
#     def info_stor(self):
#         return self.items
#
#     def search(self, name, quantity):
#         if self.items.get(name):
#             if self.items.get(name) >= quantity:
#                 self.items.update({name: self.items.get(name) - quantity})
#                 print(f"It's ok. Your product - {name} is in the storage")
#                 return True
#             else:
#                 print(f"There's no enough - {name} in our storage, there's only {self.items.get(name)} pieces")
#                 return True
#         else:
#             print("There's no such a product - {name} in the storage")
#             return False
#
#
# class Expert(Storage):
#
#     def __init__(self):
#         super().__init__()
#         self.items_shop = {}
#
#     def add_exp(self, name, quantity):
#         self.items_shop.update({name: quantity})
#
#     def info_exp(self):
#         return self.items_shop
#
#     def search_shop(self, name, quantity):
#         if self.items_shop.get(name):
#             if self.items_shop.get(name) >= quantity:
#                 self.items_shop.update({name: self.items_shop.get(name) - quantity})
#                 print(f"Your product - {name} is in the shop")
#                 return True
#             else:
#                 print(f"There's no enough - {name} in our shop, there's only {self.items_shop.get(name)} pieces")
#                 return True
#         else:
#             return False
#
#
# class Client(Expert):
#
#     def make_request(self, name: str, quantity: int):
#         if self.search_shop(name, quantity):
#             return True
#         else:
#             print(f"We will search this product - {name} in our storage!......")
#             return self.search(name, quantity)
#
#
# vova = Client()
# st = Storage()
# ex = Expert()
# st.add_stor("Milk", 25)
# st.add_stor("Coffe", 5)
# st.add_stor("Bread", 150)
# ex.add_exp("Water", 30)
# ex.add_exp("Pepsi", 94)
# ex.add_exp("Cola", 111)
# print(st.info_stor())
# print(ex.info_exp())
# vova.make_request("Pepsi", 120)
# print(st.info_stor())
# print(ex.info_exp())
# vova.make_request("Bread", 160)
# print(vova.__dict__)
# print(st.__dict__)
# print(ex.__dict__)

# ===============================
# # 2 здесь реализация этой системы не очень!
# class Faculty:
#
#     def examination(self):
#         a = int(input("5 + 2 = "))
#         if a == 7:
#             self.mark = 10
#             return True
#         else:
#             self.mark = 2
#             return False
#
#
# class Entrant(Faculty):
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.mark = 0
#         self.status = "NO"
#
#     def make_request(self):
#         if self.examination():
#             print(f"Good! You - {self.name} {self.surname} are the student of our university!")
#             print(f"Your mark is {self.mark}")
#         else:
#             print("You loose this game....")
#
#
# vova = Entrant("Vova", "Pupkin")
# vova.make_request()
