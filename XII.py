import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class XII(Scene):
    def construct(self):
        I_Y = -1.25
        IDotA, ILabelA = CreateDot(self, -1, 0+I_Y, 'A', LEFT, False)
        IDotB, ILabelB = CreateDot(self, 1, 0+I_Y, 'B', RIGHT, False)

        ILineAB = CreateLine(self, IDotA, IDotB, False)
        IDotC, ILabelC = CreateDot(self, 0, 0.5+I_Y, 'C', UP, False)

        Condition = VGroup(IDotA, IDotB, IDotC, ILabelA, ILabelB, ILabelC, ILineAB)
        
        Condition.set_opacity(0)

        IDotH, ILabelH = CreateDot(self, 0, 0+I_Y, 'H', DOWN, False)
        ILineHC = CreateLine(self, IDotH, IDotC, False)

        Success = VGroup(Condition, IDotH, ILabelH, ILineHC)
        Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema XII", 
            ("Traçar uma reta perpendicular à reta ilimitada dada,\n"
             "a partir do ponto dado que não está sobre ela."),
            Condition, Success
        )

        DotA, LabelA = CreateDot(self, -2, 0, 'A', LEFT)
        DotB, LabelB = CreateDot(self, 2, 0, 'B', RIGHT)

        LineAB = CreateLine(self, DotA, DotB)

        DotC, LabelC = CreateDot(self, 0, 0.75, 'C', UP)

        self.wait(1)

        DotD, LabelD = CreateDot(self, 0.25, -0.25, 'D', DOWN_RIGHT)

        LineCD = CreateLine(self, DotC, DotD)

        DotE, LabelE, DotF, LabelF = Intercept(self, DotC, DotD, LineCD, LineAB, ['E', 'F'], [DOWN_RIGHT, DOWN_LEFT], True)

        self.play(FadeOut(DotD, LabelD, LineCD))

        DotH, LabelH = ProblemaX(self, DotE, DotF, ['J', 'K', 'L', 'M', 'H'], [DOWN, RIGHT, LEFT, UP, DOWN], 0.625, True)
        LineCH = CreateLine(self, DotC, DotH)

        self.play(FadeOut(DotE, DotF, LabelE, LabelF))

        Quest = AddQuest(self, "Livro I - Problema XII")
        Solution = AddSolution(self, [
            "Portanto, foi traçada a perpendicular CH à reta ilimitada dada AB, a",
            "partir do ponto dado C, que não está sobre ela; o que era preciso fazer."
        ])

        self.wait(3)

        self.play(FadeOut(Solution, Quest, DotA, DotB, DotC, DotH, LabelA, LabelB, LabelC, LabelH, LineAB, LineCH))

        self.wait(1)