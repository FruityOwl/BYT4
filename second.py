import random

global healthPoint
healthPoint = 20
global ExpPoints
ExpPoints = 0
global AbilityModifier
AbilityModifier = 1


class AbstractHandler(object):

    def __init__(self, nxt):
        self._nxt = nxt

    def handle(self, request):
        handled = self.processRequest(request)

        if not handled:
            self._nxt.handle(request)

        return handled

    def processRequest(self, request):
        raise NotImplementedError('')


class DamageHandler(AbstractHandler):

    def processRequest(self, request):
        global healthPoint
        if request.find('Damage') > -1:
            dmg = random.randrange(1, 8)
            healthPoint -= dmg
            print("Damage:", dmg)
            if healthPoint > 0:
                print("Health Points:", healthPoint)
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
                print('Heal: ', heal)
                print(healthPoint)
            elif healthPoint == 20:
                print("You are feeling healthy")
            else:
                print("Sorry, you can't heal cold corpse")

            return True


class AbilityHandler(AbstractHandler):

    def processRequest(self, request):
        if request.find('Ability') > -1:
            ability = random.randrange(1, 20) + AbilityModifier
            if ability >= 10:
                print("Success:", ability)
                return True
            else:
                print("Failure:", ability)
                return False


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


class System(object):
    def Send(self, answer):
        text1 = "You are leaving tavern behind, and realising that it's way too cold to be outside for the whole night."
        text2 = "You are entering tavern. As you continue moving to the bartender. Awful smell continue to fill your " \
                "nose." \
                "You trying to stop vomiting reflex."

        if answer == "1":
            if AbilityHandler.processRequest(AbilityHandler, "Ability"):
                print(text1, "But your strong body could handle this, so you are only feeling little sick.")
            else:
                print(text1, "Maybe you should stay in tavern, because now you are have some physical ant mental "
                             "issues, as you are feeling homeless.")
                user.agent("Damage")

        elif answer == "2":
            if AbilityHandler.processRequest(AbilityHandler, "Ability"):
                print(text2, "\nThat was close. Now you fully have the honor to be here, everyone in the tavern think "
                             "the same and cheering you up with beer mugs filled to the brim.")
            else:
                print(text2, "\nOops, that was huge. Everyone laughing at you. Feeling of embarrassment is starting "
                             "to approach heavily, when you realise they already cheering you up. It's pretty common "
                             "in here.")
        else:
            print("There is no such answer. Please choose wisely..."
                  "\nWhat are you going to do?")
            txt = input()
            self.Send(txt)


class User(System):
    def Send(self, answer):
        super(User, self).Send(answer)

    def __init__(self):
        initial = None

        self.handler = DamageHandler(HealHandler(AbilityHandler(ExpHandler(DefaultHandler(initial)))))

    def agent(self, request):
        self.handler.handle(request)


if __name__ == "__main__":
    user = User()
    string = ''

    print("You are entering small old tavern. If you had another choice you would pick it, but today it is your one "
          "and only option.\nAs your enter it different noises struck your ears and the smell... please don't make me "
          "describe it.\nWhat are you going to do?"
          "\n1. No, it's way too bad. Turn around and leave."
          "\n2. It's only for today.(Ability Check: Trying not to vomit)")

    answer = input()
    user.Send(answer)
