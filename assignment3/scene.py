from assignment3.parser import Parser


class Scene:

    def __init__(self, file_list):
        self.parser = Parser()
        self.files = file_list
        self.object_list = []

    def init(self):
        for file in self.files:
            obj = self.parser.read_object(file)
            self.object_list.append(obj)

    def render(self):
        for obj in self.object_list:
            obj.draw()

    def key_pressed(self, key):
        if key == "left":
            for obj in self.object_list:
                obj.operation.rotate_y(-2.0)
        elif key == "right":
            for obj in self.object_list:
                obj.operation.rotate_y(2.0)