from math import sqrt

class Path:
    def __init__(self, points=[]):
        self.lens = []
        self.points = []
        self.normalized = False

        [self.AddPoint(p) for p in points]

        if len(self.points):
            self.Normalize()

    def __len__(self):
        return len(self.points)

    def AddPoint(self, point):
        self.points.append(point)

        if len(self.lens):
            l = self.Distance(self.points[-2], self.points[-1])
            self.lens.append(self.lens[-1] + l)
        else:
            self.lens.append(0)

    def Distance(self, a, b):
        return sqrt(sum([pow(a[i] - b[i], 2) for i in range(len(a))]))

    def DistancePath(self, path):
        if len(self) == len(path):
            return sum(self.Distance(self.points[i], path.points[i]) for i in range(len(self)))

    def Interpolate(self, array, index, ratio):
        return float(array[index]) + float(array[index + 1] - array[index]) * ratio

    def Normalize(self):
        if not self.normalized:
            self.normalized = True

            normLen = 10
            newPoints = []
            len = self.lens[-1]

            mx_min = min([x for x, y in self.points])
            mx_max = max([x for x, y in self.points])
            my_min = min([y for x, y in self.points])
            my_max = max([y for x, y in self.points])
            mx_diff = mx_max - mx_min
            my_diff = my_max - my_min

            if my_diff == 0:
                proportion = 10000000000000.0
            else:
                proportion = abs(float(mx_max - mx_min) / float(my_max - my_min))

            curIndex = 0
            for i in range(normLen):
                targetLen = i * len / normLen;

                while (self.lens[curIndex+1] < targetLen):
                    curIndex += 1

                ratio = (targetLen - self.lens[curIndex]) / (self.lens[curIndex + 1] - self.lens[curIndex])
                x = self.Interpolate([px for px, py in self.points], curIndex, ratio)
                y = self.Interpolate([py for px, py in self.points], curIndex, ratio)

                if (proportion < 0.2):
                    newPoints.append((0, (y - my_min) / (my_diff)))
                elif (proportion > 5):
                    newPoints.append(((x - mx_min) / (mx_diff), 0))
                else:
                    newPoints.append(((x - mx_min) / (mx_diff), (y - my_min) / my_diff))

            self.points = newPoints

    def PosValue(self, x, y):
        if (x < 0.5 and y < 0.5):
            return locals.StartTopLeft
        if (x >= 0.5 and y < 0.5):
            return locals.StartTopRight
        if (x < 0.5 and y >= 0.5):
            return locals.StartBottomLeft
        if (x >= 0.5 and y >= 0.5):
            return locals.StartBottomRight

    def MatchConstraint(self, c):
        if not c:
            return True
        if not self.normalized:
            return False

        startValue = self.PosValue(self.points[0][0], self.points[0][1])
        endValue = self.PosValue(self.points[-1][0], self.points[-1][1]) << 4

        return ((startValue | endValue) & (~c)) == 0