class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def test(self):
        print("The values are {} and {}".format(self.x, self.y) ,end=" ")
        #print(f"The values are {self.x} and {self.y}", end=" ")

p = Point(3,5)
p.test()