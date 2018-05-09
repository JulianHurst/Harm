from .writer import HarmWriter

class HarmReader:
    base = ["c", "d", "e", "f", "g", "a", "b"]
    mods = ["b", "#"]

    def __init__(self, filename):
        self.writer = HarmWriter(filename)

    def read(self, filename):
        print("reading")
        with open(filename) as f:
            data = f.read()

        self.writer.writeTitle(filename)
        lines = data.split("\n")
        print(lines)
        struct = False
        for line in lines:
            if not line == '':
                if line == "[STRUCT]":
                   struct = True 
                   self.writer.writeStructTitle()
                elif not struct:
                    split_data = line.split(" ")
                    label = split_data[0]
                    chords = split_data[1:]
                    self.writer.write(label, chords)
                    self.writer.nextLine(1)
                else:
                    split_data = line.strip().split(" ")
                    print(split_data)
                    label = split_data[0]
                    if len(split_data) == 1:
                        iterations = '1'
                    else:
                        iterations = split_data[1]
                    self.writer.writeStruct(label, iterations)
                    self.writer.nextLine(0.5)
        self.writer.save()
