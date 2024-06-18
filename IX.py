import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class IX(Scene):
    def construct(self):
        I_Y = -1.25
        IDotA, ILabelA = CreateDot(self, 0, 1+I_Y, 'A', UP, False)
        IDotB, ILabelB = CreateDot(self, -0.5, -1+I_Y, 'B', DOWN_LEFT, False)
        IDotC, ILabelC = CreateDot(self, 0.5, -1+I_Y, 'C', DOWN_RIGHT, False)

        ILineAB = CreateLine(self, IDotA, IDotB, False)
        ILineCA = CreateLine(self, IDotC, IDotA, False)
        IAngleBAC = CreateAngle(self, IDotA, ILineAB, ILineCA, False, RED, 0.4)

        Condition = VGroup(IDotA, IDotB, IDotC, ILabelA, ILabelB, ILabelC, ILineAB, ILineCA, IAngleBAC)
        
        Condition.set_opacity(0)

        IDotF, ILabelF = CreateDot(self, 0, -0.75+I_Y, 'F', DOWN, False)
        ILineFA = CreateLine(self, IDotF, IDotA, False)

        Success = VGroup(Condition, IDotF, ILabelF, ILineFA)
        Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema IX", 
            ("Cortar em dois o ângulo retílineo dado."),
            Condition, Success
        )

        DotA, LabelA = CreateDot(self, 0, 1, 'A', UP)
        DotB, LabelB = CreateDot(self, -0.5, -1, 'B', DOWN_LEFT)
        DotC, LabelC = CreateDot(self, 0.5, -1, 'C', DOWN_RIGHT)

        self.wait(1)

        LineAB = CreateLine(self, DotA, DotB)
        LineAC = CreateLine(self, DotA, DotC)
        LineCA = CreateLine(self, DotC, DotA, False)

        self.wait(1)

        AngleBAC = CreateAngle(self, DotA, LineAB, LineCA, True, RED, 0.4)

        DotD, LabelD = CreateDot(self, -0.3125, -0.25, 'D', LEFT)
        LineAD = CreateLine(self, DotA, DotD, False)

        CircleADH = CreateCircleFromLine(self, DotA, DotD, LineAD, True)
        DotE, LabelE = CreateDot(self, 0.3125, -0.25, 'E', RIGHT)

        self.play(FadeOut(CircleADH))

        DotF, LabelF, LineDE, LineEF, LineFD = ProblemaI(self, DotD, DotE, 'F', DOWN, True)

        LineFA = CreateLine(self, DotF, DotA)

        self.play(FadeOut(DotD, DotE, LabelD, LabelE, LineDE, LineEF, LineFD))

        Quest = AddQuest(self, "Livro I - Problema IX")
        Solution = AddSolution(self, [
            "Portanto, o ângulo retilíneo dado, o sob BAC, foi cortado em dois",
            "pela reta AF; o que era preciso fazer."
        ])

        self.wait(3)

        self.play(FadeOut(Solution, Quest, DotA, DotB, DotC, DotF, LabelA, LabelB, LabelC, LabelF, LineAB, LineAC, LineAD, LineCA, LineFA, AngleBAC))

        self.wait(1)