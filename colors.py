class Color:

    def __init__(self):
        self.lst = [[0, 255, 255], [255, 0, 0], [0, 255, 0], [127, 0, 255], [0, 0, 0]]

    def getList(self):
        return self.lst

    def check(self, r, g, b):

        proche = None
        for value in self.getList():
            
            if proche == None:
                proche = value

            else:

                valeur_proche = [abs(proche[0] - r), abs(proche[1] - g), abs(proche[2] - b)]
                valeur_essaie = [abs(value[0] - r), abs(value[1] - g), abs(value[2] - b)]

                if valeur_proche > valeur_essaie:
                    proche = value

        return proche