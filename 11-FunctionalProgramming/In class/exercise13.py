def bottle_fill(limit):
    def check(ml):
        if limit == 500:
            if 0.98*limit <= ml <= 1.02*limit:
                return True
            else:
                return False
        elif limit == 1000:
            if 0.97*limit <= ml <= 1.03*limit:
                return True
            else:
                return False
        elif limit == 1500:
            if 0.95*limit <= ml <= 1.05*limit:
                return True
            else:
                return False
        else:
            return "Input proper limit"
    return check

bottle05 = bottle_fill(500)
bottle1 = bottle_fill(1000)
bottle15 = bottle_fill(1500)
bottleasdddd = bottle_fill(1)

print(bottle05(507))
print(bottle05(489))
print(bottle1(984))
print(bottle1(1032))
print(bottle15(1578))
print(bottle15(1430))
print(bottleasdddd(1234))