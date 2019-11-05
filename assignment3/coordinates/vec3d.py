class Vec3d:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 0

    def __str__(self):
        return 'Vec3d(' + self.x + ', ' + str(self.y) + ', ' + str(self.z) + ')'
