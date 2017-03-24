import math


class HereditaryBaseNotation:
    def __init__(self, number, base):
        self._base = base
        self.Exponents = []
        self.Multiplier = 1
        while number >= base:
            e = math.floor(math.log(number, base))
            n = math.floor(base ** e)
            if len(self.Exponents) > 0 and self.Exponents[-1].Value == e:
                self.Exponents[-1].Multiplier += 1
            else:
                self.Exponents.append(HereditaryBaseNotation(e, base))
            number -= n
        self.ZeroPower = number

    @property
    def Value(self):
        ret = self.ZeroPower
        for e in self.Exponents:
            ret += e.Multiplier * (self.Base ** e.Value)
        return math.floor(ret)

    @property
    def Base(self):
        return self._base

    @Base.setter
    def Base(self, value):
        self._base = value
        for e in self.Exponents:
            e.Base = value

    def __str__(self):
        ret = ""
        for e in self.Exponents:
            ret += " + "
            if e.Multiplier > 1:
                ret += str(e.Multiplier) + " * "
            ret += str(self.Base)
            if e.Value > 1:
                ret += "^"
                if len(e.Exponents) > 1 or (len(e.Exponents) == 1 and e.ZeroPower > 0):
                    ret += "(" + str(e) + ")"
                else:
                    ret += str(e)
        if self.ZeroPower > 0:
            ret += " + " + str(self.ZeroPower)
        return ret[3:]


if __name__ == '__main__':
    num = 0
    iterations = 0
    while True:
        inp = input("Enter the number to compute a Goodstein Sequence [default 3]: ")
        if inp == "":
            num = 3
            break
        try:
            num = int(inp)
            if num < 0:
                continue
            break
        except (TypeError, ValueError):
            continue
    while True:
        inp = input("Enter the maximum iterations [default 10]: ")
        if inp == "":
            iterations = 10
            break
        try:
            iterations = int(inp)
            if iterations < 1:
                continue
            break
        except (TypeError, ValueError):
            continue
    print("\nComputing G(" + str(num) + ") up to " + str(iterations) + " iterations\n")
    it_max = iterations
    gs = HereditaryBaseNotation(num, 2)
    val = gs.Value
    while iterations > 0:
        print("base " + str(gs.Base) + ": " + str(gs) + " = " + str(val))
        gs.Base += 1
        val = gs.Value
        print("  " + str(gs) + " - 1 = " + str(val - 1))
        gs = HereditaryBaseNotation(val - 1, gs.Base)
        val = gs.Value
        iterations -= 1
        if val == 0:
            break
    if val == 0:
        print("\nReached 0 in " + str(it_max - iterations) + " iterations")
    else:
        print("\nReached maximum iterations (" + str(it_max) + ")")
