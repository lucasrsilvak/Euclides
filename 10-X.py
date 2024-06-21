import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class X(Scene):
    def construct(self):
        I_Y = -1.25
        IDotA, ILabelA = CreateDot(self, -1, 0+I_Y, 'A', LEFT, False)
        IDotB, ILabelB = CreateDot(self, 1, 0+I_Y, 'B', RIGHT, False)

        ILineAB = CreateLine(self, IDotA, IDotB, False)

        Condition = VGroup(IDotA, IDotB, ILabelA, ILabelB, ILineAB)
        
        Condition.set_opacity(0)

        IDotD, ILabelD = CreateDot(self, 0, 0+I_Y, 'D', DOWN, False)

        Success = VGroup(Condition, IDotD, ILabelD)
        Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema X", 
            ("Cortar em duas a reta limitada dada."),
            Condition, Success
        )

        DotA, LabelA = CreateDot(self, -1, 0, 'A', LEFT)
        DotB, LabelB = CreateDot(self, 1, 0, 'B', RIGHT)

        LineAB = CreateLine(self, DotA, DotB)

        self.wait(1)

        DotC, LabelC, LineAB2, LineBC, LineCA = ProblemaI(self, DotA, DotB, 'C', UP)
        AngleBAC, DotF, LabelF, LineFA = ProblemaIX(self, DotC, DotA, DotB, LineCA, LineBC)

        DotD, LabelD = CreateDot(self, 0, 0, 'D', DOWN)

        self.play(FadeOut(AngleBAC, DotC, DotF, LabelC, LabelF, LineBC, LineCA, LineFA))


        Quest = AddQuest(self, "Livro I - Problema X")
        Solution = AddSolution(self, [
            "Portanto, a reta limitada dada AB",
            "foi cortada em duas no D; o que era preciso fazer."
        ])

        self.wait(3)

        self.play(FadeOut(Solution, Quest, DotA, DotB, DotD, LabelA, LabelB, LabelD, LineAB, LineAB2))

        self.wait(1)
