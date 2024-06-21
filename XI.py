import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class XI(Scene):
    def construct(self):
        I_Y = -1.25
        IDotA, ILabelA = CreateDot(self, -1, 0+I_Y, 'A', LEFT, False)
        IDotB, ILabelB = CreateDot(self, 1, 0+I_Y, 'B', RIGHT, False)

        ILineAB = CreateLine(self, IDotA, IDotB, False)
        IDotC, ILabelC = CreateDot(self, 0, 0+I_Y, 'C', DOWN, False)

        Condition = VGroup(IDotA, IDotB, IDotC, ILabelA, ILabelB, ILabelC, ILineAB)
        
        Condition.set_opacity(0)

        IDotF, ILabelF = CreateDot(self, 0, 1+I_Y, 'F', UP, False)
        ILineFC = CreateLine(self, IDotF, IDotC, False)

        Success = VGroup(Condition, IDotF, ILabelF, ILineFC)
        Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema XI", 
            ("Traçar uma linha reta em ângulos retos com\n"
             "a reta dada a partir do ponto dado sobre ela."),
            Condition, Success
        )

        DotA, LabelA = CreateDot(self, -2, 0, 'A', LEFT)
        DotB, LabelB = CreateDot(self, 2, 0, 'B', RIGHT)

        LineAB = CreateLine(self, DotA, DotB)

        DotC, LabelC = CreateDot(self, 0, 0, 'C', DOWN)

        LineCB = CreateLine(self, DotC, DotB, False)

        self.wait(2)

        DotD, LabelD = CreateDot(self, -0.6, 0, 'D', DOWN_LEFT)
        LineDC = CreateLine(self, DotD, DotC, False)

        DotE, LabelE, _, _ = Intercept(self, DotC, DotD, LineDC, LineCB, ['E'], [DOWN_RIGHT])
        DotF, LabelF, LineDE, LineEF, LineFD = ProblemaI(self, DotD, DotE, 'F', UP)

        LineFC = CreateLine(self, DotF, DotC)

        self.wait(1)

        self.play(FadeOut(DotD, DotE, LabelD, LabelE, LineDE, LineEF, LineFD))

        Quest = AddQuest(self, "Livro I - Problema XI")
        Solution = AddSolution(self, [
            "Portanto, foi traçada a linha reta CF em ângulos retos com a reta dada AB",
            "a partir do ponto dado C sobre ela; o que era preciso fazer."
        ])

        self.wait(3)

        self.play(FadeOut(Solution, Quest, DotA, DotB, DotC, DotF, LabelA, LabelB, LabelC, LabelF, LineAB, LineCB, LineDC, LineFC))

        self.wait(1)