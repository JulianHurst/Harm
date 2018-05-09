from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class HarmWriter:
    line_width = 20
    line_spacing = 50
    word_spacing = 50
    width, height = A4
    marginw = 20
    marginh = 20

    def __init__(self, filename):
        self.c = canvas.Canvas(filename)
        self.c.setFont("Helvetica", 15)
        self.line = 1
        self.word = 1
        self.bar = 1

    def writeTitle(self, title):
        self.c.setFont("Helvetica", 30)
        self.c.drawString(self.width / 2 - len(title) * 8, self.height - self.marginh * 2, title)
        self.line += 0.5


    def write(self, label, chords):
        label = label.strip() 
        self.c.setFont("Helvetica", 20)
        self.drawS(label)
        self.c.setFont("Helvetica", 15)
        self.word = 1
        self.line += 0.5
        for chord in chords:
            word_increment = 1
            chord = chord.strip()
            if chord == "|":
                self.bar += 1
                word_increment = 0.5
            #if self.bar == 6:
            #    self.word = 1
            #    self.line += 1
            #    self.bar = 1
            if self.word * self.word_spacing > self.width - self.marginw:
                self.word = 1
                self.line += 1
                self.bar = 1
            self.drawS(chord)
            self.word += word_increment

    def writeStructTitle(self):
        self.drawS("Structure : ")
        self.nextLine(0.5)
        self.word_spacing = 50

    def writeStruct(self, label, iterations):
        self.drawS(label)
        self.word += 0.5
        if iterations != '1':
            self.drawS("X" + iterations)

    def save(self):
        self.c.showPage()
        self.c.save()

    def drawS(self, string):
        self.c.drawString(self.word * self.word_spacing, self.height - self.line * self.line_spacing - self.marginh, string)

    def nextLine(self, increment):
        self.line += increment
        self.word = 1
        self.bar = 1
