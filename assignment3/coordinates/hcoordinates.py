class HCoordinates:

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return 'HCoordinates(' + self.x + ', ' + str(self.y) + ', ' + str(self.z) + ', ' + str(self.w) + ')'
