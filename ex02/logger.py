import time
import getpass
from random import randint

fd = open("./machine.log", "w+")


def log(func):
    def wrap(*args):
        time1 = time.time()
        ret = func(*args)
        time2 = time.time()

        username = getpass.getuser()
        timer = (time2-time1) * 1000
        measure = "ms"
        if timer >= 1000:
            measure = "s"
            timer = timer / 1000
        fd = open("./machine.log", "a")
        fd.write(
            '({})Running: {:15} [ exec-time = {:5.3f} {:2} ]\n'
            .format(username, func.__name__, timer, measure))

        return ret
    return wrap


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
        machine.make_coffee()
        machine.add_water(70)
    fd.close()
