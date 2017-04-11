from functools import reduce

class Evaluate:
    def average(self, scores):
        return reduce(lambda a, b: a + b, scores)/len(scores)

    def variance(self, scores, avrg):
        return reduce(lambda a, b: a + b, map(lambda s:(s-avrg)**2, scores))/len(scores)

if __name__ == "__main__":
    e = Evaluate()
    li = [100, 95, 90]