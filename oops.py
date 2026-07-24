#class student:
    # pass
# def student(name,age):
#     print(name)
#     print(age)
# student("alwin",20)
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s1=student("alwin",20)
# s2=student("mega",15)
# print(s1.name)
# print(s2.age)

#method overriding
# class animal:
#     def eat(self):
#         print("animal eats food")
# class tiger(animal):
#     def eat(self):
#         print("tiger eats food")
# class pig(animal):
#     def eat(self):
#         print("pig eats food")
# t1= tiger()
# t1.eat()
# t2= pig()
# t2.eat()
#method overloading
# class maths:
#     def add(self,a=7,b=2):
#         print(a+b)
# m1 = maths()
# m1.add()
# m1.add(5,6)
# a=input("enter value")
# b=input("enter value")
# print(a+b)
# a=int(input("enter value"))
# b=int(input("enter value"))
# print(a+b)

# class student():
#     def __init__(self):
#         self._name = "milesh"
# c1=student()
# print(c1.name)
#pritected
class worker:
    def __init__(self):
        self.__salary=60000

    def manage(self):
        print(self.__salary)
a1=worker()
a1.manage()
# class Bank:
#
#    def __init__(self):
#
#        self.__balance = 10000
#
#    def show_balance(self):
#
#        print("Balance =", self.__balance)
#
# b1 = Bank()
# b1.show_balance()
















