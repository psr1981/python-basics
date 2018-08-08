class Cup:
    def __init__(self, color):
        self._color = color    # protected variable
        self.__content = None  # private variable

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def getContent(self):
        return self.__content


redCup = Cup("red")
redCup.fill("tea")

print(redCup.getContent())

try:
    print (redCup.__content)
except:
    print ("__content can not be accessed from outside")


