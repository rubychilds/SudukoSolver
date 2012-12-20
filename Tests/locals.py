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


class locals:
    StartTopLeft = 1 # starting in the top left corner is allowed
    StartTopRight = 1 << 1
    StartBottomLeft = 1 << 2
    StartBottomRight = 1 << 3
    StartAny = StartTopLeft | StartTopRight | StartBottomLeft | StartBottomRight

    EndTopLeft = 1 << 4
    EndTopRight = 1 << 5
    EndBottomLeft = 1 << 6
    EndBottomRight = 1 << 7
    EndAny = EndTopLeft | EndTopRight | EndBottomLeft | EndBottomRight
    Any = StartAny | EndAny

    capitals = [
        ["A", Path(zip([0, 5, 10], [10, 0, 10])), StartBottomLeft | EndBottomRight],
        ["B", Path(zip([0, 0, 0, 3, 3, 0], [0, 10, 7, 7, 10, 10])), StartTopLeft | EndBottomLeft],
        ["C", Path(zip([10, 0, 0, 10], [0, 0, 10, 10])), StartTopRight | EndBottomRight],
        ["D", Path(zip([0, 0, 10, 10, 0], [10, 0, 0, 10, 10])), StartBottomLeft | EndBottomLeft],
        ["E", Path(zip([10, 0, 0, 3, 0, 0, 10], [0, 0, 5, 5, 5, 10, 10])), StartTopRight | EndBottomRight],
        ["F", Path(zip([10, 0, 0], [0, 0, 10])), StartTopRight | EndBottomLeft],
        ["G", Path(zip([10, 0, 0, 10, 10, 5], [0, 0, 10, 10, 5, 5])), StartTopRight | EndAny],
        ["H", Path(zip([0, 0, 0, 3, 3], [0, 10, 7, 7, 10])), StartTopLeft | EndBottomRight],
        ["I", Path(zip([5, 5], [0, 10])), StartTopLeft | EndBottomLeft],
        ["J", Path(zip([10, 10, 0], [0, 10, 10])), StartTopRight | EndBottomLeft | EndTopLeft],
        ["K", Path(zip([10, 0, 0, 10], [0, 10, 0, 10])), StartTopRight | EndBottomRight],
        ["L", Path(zip([0, 0, 10], [0, 10, 10])), StartTopLeft | EndBottomRight],
        ["M", Path(zip([0, 0, 5, 10, 10], [10, 0, 5, 0, 10])), StartBottomLeft | EndBottomRight],
        ["N", Path(zip([0, 0, 10, 10], [10, 0, 10, 0])), StartBottomLeft | EndTopRight],
        ["O", Path(zip([5, 0, 0, 10, 10, 5], [0, 0, 10, 10, 0, 0])), StartTopLeft | StartTopRight | EndTopLeft | EndTopRight],
        ["P", Path(zip([0, 0, 0, 10, 10, 0], [0, 10, 0, 0, 5, 5])), StartBottomLeft | EndAny],
        ["P2", Path(zip([0, 0, 10, 10, 0], [10, 0, 0, 5, 5])), StartBottomLeft | EndAny],
        ["Q", Path(zip([4, 0, 0, 4, 4], [0, 0, 4, 4, 7])), None],
        ["R", Path(zip([0, 0, 0, 10, 10, 0, 10], [0, 10, 0, 0, 5, 5, 10])), StartBottomLeft | EndAny],
        ["R2", Path(zip([0, 0, 10, 10, 0, 10], [10, 0, 0, 5, 5, 10])), StartBottomLeft | EndBottomRight],
        ["S", Path(zip([10, 0, 0, 10, 10, 0], [0, 2, 4, 6, 8, 10])), StartTopRight | EndBottomLeft],
        ["T", Path(zip([0, 8, 8], [0, 0, 10])), StartTopLeft | EndBottomRight],
        ["U", Path(zip([0, 5, 10], [0, 10, 0])), StartTopLeft | EndTopRight],
        ["U2", Path(zip([0, 0, 10, 10], [0, 10, 10, 0])), StartTopLeft | EndTopRight],
        ["V", Path(zip([10, 5, 0], [0, 10, 0])), StartTopLeft | EndTopRight],
        ["V2", Path(zip([0, 3, 6, 10], [0, 10, 0, 0])), StartTopLeft | EndTopRight],
        ["W", Path(zip([0, 0, 5, 10, 10], [0, 10, 5, 10, 0])), StartTopLeft | EndTopRight],
        ["X", Path(zip([0, 10, 10, 0], [10, 0, 10, 0])), StartBottomLeft | EndTopLeft],
        ["Y", Path(zip([0, 0, 5, 5, 5, 5, 5, 10], [0, 5, 5, 0, 5, 10, 5, 5])), StartTopLeft | EndAny],
        ["Z", Path(zip([0, 10, 0, 10], [0, 0, 10, 10])), StartTopLeft | EndBottomRight],
    ]

class OneStrokeGestureException(Exception):
    pass

class OneStrokeGesture:

    paths = []

    def __init__(self, strokes=locals.capitals):
        self.strokes = strokes
        self.path = None
        self.down = False

    def PenDown(self, pos):
        self.path = Path()
        self.path.AddPoint(pos)
        self.down = True

    def PenTo(self, pos):
        self.path.AddPoint(pos)

    def PenUp(self, pos):
        self.down = False
        if len(self.path) > 1:
            self.path.AddPoint(pos)
            return self.FindBestMatch()

    def Learn(self, id, points):
        self.strokes += [[id, Path(points), locals.Any]]

    def FindGesture(self, points):
        self.path = Path(points)
        return self.FindBestMatch()

    def FindBestMatch(self):
        if self.path.points[0] != self.path.points[1]:
            self.path.Normalize()
            minDist = 100
            minStroke = [None, None, None]
            results = [(s[0], self.path.DistancePath(s[1])) for s in self.strokes if self.path.MatchConstraint(s[2])]
            results.sort(lambda a,b: cmp(a[1], b[1]))
            return results
        else:
            raise OneStrokeGestureException("Paths are different lengths")
