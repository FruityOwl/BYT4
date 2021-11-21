"""import random

global healthPoint
healthPoint = 20
global ExpPoints
ExpPoints = 0


class AbstractHandler(object):

    def __init__(self, nxt):
        self._nxt = nxt

    def handle(self, request):
        handled = self.processRequest(request)

        if not handled:
            self._nxt.handle(request)

    def processRequest(self, request):
        raise NotImplementedError('')


class DamageHandler(AbstractHandler):

    def processRequest(self, request):
        global healthPoint
        if request.find('Damage') > -1:
            print("This is DamageHandler")
            dmg = random.randrange(1, 8)
            healthPoint -= dmg
            print(dmg)
            if healthPoint > 0:
                print(healthPoint)
            else:
                print("You are dead")
            return True


class HealHandler(AbstractHandler):

    def processRequest(self, request):
        global healthPoint
        if request.find('Heal') > -1:
            print("This is HealHandler")
            heal = random.randrange(1, 8)
            if 0 < healthPoint < 20:
                healthPoint += heal
                print('Heal =', heal)
                print(healthPoint)
            elif healthPoint == 20:
                print("You are feeling healthy")
            else:
                print("Sorry, you can't heal cold corpse")

            return True


class AbilityHandler(AbstractHandler):

    def processRequest(self, request):
        if request.find('Ability') > -1:
            print("This is AbilityHandler")
            ability = random.randrange(1, 20)
            if ability >= 10:
                print("Success:", ability)
            else:
                print("Failure:", ability)
            return True


class ExpHandler(AbstractHandler):

    def processRequest(self, request):
        global ExpPoints
        if request.find('Exp') > -1:
            print("This is ExpHandler")
            ExpPoints += int(request[3:len(request)])
            print(ExpPoints)
            return True


class DefaultHandler(AbstractHandler):

    def processRequest(self, request):
        print("There is no such operation")
        return True


class User:

    def __init__(self):
        initial = None

        self.handler = DamageHandler(HealHandler(AbilityHandler(ExpHandler(DefaultHandler(initial)))))

    def agent(self, request):
        self.handler.handle(request)


if __name__ == "__main__":
    user = User()
    string = ''

    while string != "exit":
        print("Write equation: ")
        string = input()
        user.agent(string)
"""