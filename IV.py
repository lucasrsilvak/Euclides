import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class IV(Scene):
    def construct(self):
        I_Y = -2
        IDotA, ILabelA = CreateDot(self, -1.5, 1 + I_Y, 'A', UP, False)
        IDotA_, ILabelA_ = CreateDot(self, -1.5, 1 + I_Y, '', UP, False)
        IDotB, ILabelB = CreateDot(self, -2.5, -1 + I_Y, 'B', LEFT, False)
        IDotC, ILabelC = CreateDot(self, -0.5, -1 + I_Y, 'C', RIGHT, False)
        ILineAB = CreateLine(self, IDotA, IDotB, False)
        ILineBC = CreateLine(self, IDotB, IDotC, False)
        ILineCA = CreateLine(self, IDotC, IDotA_, False)
        IAngleBAC = CreateAngle(self, IDotA, ILineAB, ILineCA, False)

        IDotD, ILabelD = CreateDot(self, 1.5, 1 + I_Y, 'D', UP, False)
        IDotE, ILabelE = CreateDot(self, 0.5, -1 + I_Y, 'E', LEFT, False)
        IDotF, ILabelF = CreateDot(self, 2.5, -1 + I_Y, 'F', RIGHT, False)

        ILineDE = CreateLine(self, IDotD, IDotE, False)
        ILineEF = CreateLine(self, IDotE, IDotF, False)
        ILineFD = CreateLine(self, IDotF, IDotD, False)
        IAngleDEF = CreateAngle(self, IDotD, ILineDE, ILineFD, False)

        ITickAB = CreateLineTick(self, ILineAB, 1, False)
        ITickDE = CreateLineTick(self, ILineDE, 1, False)

        ITickCA = CreateLineTick(self, ILineCA, 2, False)
        ITickFD = CreateLineTick(self, ILineFD, 2, False)

        Condition = VGroup(IDotA, ILabelA, IDotB, ILabelB, IDotC, ILabelC, ILineAB, ILineBC, ILineCA,
                           IDotD, ILabelD, IDotE, ILabelE, IDotF, ILabelF, ILineDE, ILineEF, ILineFD,
                           IAngleBAC, IAngleDEF, ITickAB, ITickDE, ITickCA, ITickFD)
        
        #Condition.set_opacity(0)

        ILabelEq = CreateLabel(self, 0, 0 + I_Y, '≡', DOWN*0, False, 40)
        
        Success = VGroup(ILabelEq, Condition)
        #Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema IV", 
            "Caso dois triângulos tenham os dois lados iguais aos dois lados, cada um a cada um,\n e tenham o ângulo contido pelas retas iguais igual ao ângulo,\n também terão a base igual a base, e o triângulo será igual ao triângulo,\n e os ângulos restantes serão iguais aos ângulos restantes,\n cada um a cada um, sob os quais se estendem os lados iguais.",
            Condition, Success
        )

        DotA, LabelA = CreateDot(self, -1.5, 1, 'A', UP)
        DotA_, LabelA_ = CreateDot(self, -1.5, 1, '', UP, False)
        DotB, LabelB = CreateDot(self, -2.5, -1, 'B', UP_LEFT)
        DotC, LabelC = CreateDot(self, -0.5, -1, 'C', UP_RIGHT)
        self.wait(1)
        LineAB = CreateLine(self, DotA, DotB)
        LineBC = CreateLine(self, DotB, DotC)
        LineCA = CreateLine(self, DotC, DotA_)
        self.wait(1)
        AngleBAC = CreateAngle(self, DotA, LineAB, LineCA)

        DotD, LabelD = CreateDot(self, 1.5, 1, 'D', DOWN)
        DotE, LabelE = CreateDot(self, 0.5, -1, 'E', DOWN_LEFT)
        DotF, LabelF = CreateDot(self, 2.5, -1, 'F', DOWN_RIGHT)

        self.wait(1)
        LineDE = CreateLine(self, DotD, DotE)
        LineEF = CreateLine(self, DotE, DotF)
        LineFD = CreateLine(self, DotF, DotD)
        AngleDEF = CreateAngle(self, DotD, LineDE, LineFD)
        self.wait(1)

        TickAB = CreateLineTick(self, LineAB)
        TickDE = CreateLineTick(self, LineDE)

        TickCA = CreateLineTick(self, LineCA, 2)
        TickFD = CreateLineTick(self, LineFD, 2)

        self.play(FadeOut(AngleDEF), FadeOut(LineDE), FadeOut(LineBC), FadeOut(LineEF), FadeOut(LineFD), FadeOut(TickAB), FadeOut(TickAB), FadeOut(TickAB), FadeOut(TickAB), FadeOut(TickDE), FadeOut(TickCA), FadeOut(TickFD))

        self.wait(3)

        TriangleABC = VGroup(DotA, DotB, LabelA, LabelB, LineAB, DotC, DotA_, LabelC, LineCA, AngleBAC)

        
        MoveLine(self, TriangleABC, DotD, DotE)

        self.play(
            LabelA.animate.next_to(DotA, LEFT, buff=0.1),
            LabelD.animate.next_to(DotA, RIGHT, buff=0.1),
        )

        LineEF = CreateLine(self, DotE, DotF)

        self.wait(1)

        Triangle = VGroup(TriangleABC, DotD, DotE, DotF, LabelD, LabelE, LabelF, LineEF)

        MoveToOrigin(self, Triangle)

        self.wait(2)

        Quest = AddQuest(self, "Livro I - Problema IV")
        Solution = AddSolution(self, [
            "Portanto, caso dois triângulos tenham dois lados iguais e o ângulo contido pelas retas",
            "iguais igual, também serão iguais as bases e os triângulos, o que era preciso provar."
        ])

        self.wait(3)

        self.play(FadeOut(Solution), FadeOut(Quest), FadeOut(Triangle))

        self.wait(1)
