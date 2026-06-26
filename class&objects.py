class student:
    name = "Dhanusya"
s = student()
print(s.name)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check(self):
        if self.age >= 18:
            print(self.name, "is Eligible to Vote")
        else:
            print(self.name, "is Not Eligible to Vote")

p = Person("Allie", 21)
p.check()

class MovieTicket:
    def __init__(self, movie, tickets):
        self.movie = movie
        self.tickets = tickets

    def bill(self):
        amount = self.tickets * 200
        print("Movie:", self.movie)
        print("Total Amount:", amount)

m = MovieTicket("Leo", 3)
m.bill()