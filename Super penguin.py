# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print(penguin)

    def run(self):
        print ("run faster")


peggy = penguin()
peggy.WhoIsThis()
Peggy.swim()
Peggy.run()