import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class I(Scene):
    def construct(self):
        I_Y = -4 # Ajuda a centralizar a imagem
        IDotA, ILabelA = CreateDot(self, -1, 0 + I_Y, 'A', DOWN_LEFT, False)
        IDotB, ILabelB = CreateDot(self, 1, 0 + I_Y, 'B', DOWN_RIGHT, False)
        ILineAB = CreateLine(self, IDotA, IDotB, False)
        Condition = VGroup(IDotA, ILabelA, IDotB, ILabelB, ILineAB)
        Condition.set_opacity(0)

        IDotC, ILabelC = CreateDot(self, 0, math.sqrt(3) + I_Y, 'C', DOWN_RIGHT, False)
        ILineBC = CreateLine(self, IDotB, IDotC, False)
        ILineCA = CreateLine(self, IDotC, IDotA, False)
        ITriangleABC = AssembleTriangle(self, ILineAB, ILineBC, ILineCA)
        ITriangleABC = AddTicksToTriangle(self, ITriangleABC, False)
        
        Success = VGroup(ITriangleABC, Condition)
        Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema I", 
            "Construir um triângulo equilátero sobre a reta limitada dada.",
            Condition, Success
        )

        DotA, LabelA = CreateDot(self, -1, 0, 'A', DOWN_LEFT)
        DotB, LabelB = CreateDot(self, 1, 0, 'B', DOWN_RIGHT)
        self.wait(1)
        LineAB = CreateLine(self, DotA, DotB)
        self.wait(1)
        CircleACD = CreateCircleFromLine(self, DotA, DotB, LineAB)

        LabelD = CreateLabel(self, -3, 0, 'D', RIGHT)
        CircleBCE = CreateCircleFromLine(self, DotB, DotA, LineAB)
        LabelE = CreateLabel(self, 3, 0, 'E', LEFT)

        DotC, LabelC = CreateDot(self, 0, math.sqrt(3), 'C', UP)
        LineBC = CreateLine(self, DotB, DotC)
        LineCA = CreateLine(self, DotC, DotA)
        self.wait(2)

        TriangleABC = AssembleTriangle(self, LineAB, LineBC, LineCA)
        TriangleCenter = np.array([0, np.sqrt(3)/3, 0])

        self.play(FadeOut(CircleACD), FadeOut(CircleBCE), FadeOut(LabelD), FadeOut(LabelE))
        self.wait(1)

        self.play(Rotate(TriangleABC, angle=2*PI/3, about_point=TriangleCenter, run_time=2))
        self.wait(0.5)
        self.play(Rotate(TriangleABC, angle=2*PI/3, about_point=TriangleCenter, run_time=2))
        self.wait(0.5)

        TriangleABC = AddTicksToTriangle(self, TriangleABC)
        TriangleABC = VGroup(TriangleABC, DotA, DotB, LabelA, LabelB)
        self.wait(1)

        self.play(FadeOut(DotC), FadeOut(LabelC))

        self.play(TriangleABC.animate.move_to(ORIGIN))
        self.wait(0.5)

        self.play(TriangleABC.animate.scale(1.5))

        self.wait(1)

        Quest = AddQuest(self, "Livro I - Problema I")
        Solution = AddSolution(self, [
            "Sobre a reta limitada dada AB, foi construído",
            "um triângulo equilátero, o que era preciso fazer."
        ])

        self.wait(3)

        self.play(FadeOut(Solution), FadeOut(Quest), FadeOut(TriangleABC))

        self.wait(1)
