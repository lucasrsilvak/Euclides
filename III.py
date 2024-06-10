import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class III(Scene):
    def construct(self):
        I_Y = -3.75
        IDotA, ILabelA = CreateDot(self, -1, 0+I_Y, 'A', LEFT, False)
        IDotB, ILabelB = CreateDot(self, 1, 0+I_Y, 'B', RIGHT, False)
        ILineAB = CreateLine(self, IDotA, IDotB, False)

        IDotC, ILabelC = CreateDot(self, -0.5, 1.25+I_Y, '', LEFT, False)
        IDotC_, LabelC_ = CreateDot(self, 0.5, 1.25+I_Y, '', RIGHT, False)
        ILabelC = CreateLabel(self, 0, 3.25 + I_Y, 'C', UP, False)
        ILineC = CreateLine(self, IDotC, IDotC_, False)

        Condition = VGroup(IDotA, ILabelA, IDotB, ILabelB, ILineAB, IDotC, ILabelC, IDotC_, ILineC)
        Condition.set_opacity(0)

        IDotC, ILabelC = CreateDot(self, -0.5, 1.25+I_Y, '', LEFT, False)
        IDotC_, ILabelC_ = CreateDot(self, 0.5, 1.25+I_Y, '', RIGHT, False)
        ILabelC = CreateLabel(self, 0, 3.25+I_Y, 'C', UP, False)
        ILineC = CreateLine(self, IDotC, IDotC_, False)
        
        IDotA, ILabelA = CreateDot(self, -0.5, 0+I_Y, 'A', LEFT, False)
        IDotE, ILabelE = CreateDot(self, 0.5, 0+I_Y, 'E', RIGHT, False)
        ILineAE = CreateLine(self, IDotA, IDotE, False)

        Success = VGroup(IDotC, ILabelC, IDotC_, ILineC, IDotA, ILabelA, IDotE, ILabelE, ILineAE)
        Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema III", 
            "Dadas duas retas desiguais, subtrair da maior uma reta igual à menor.",
            Condition, Success
        )

        Y = -0.25

        DotA, LabelA = CreateDot(self, -0.5, 0+Y, 'A', DOWN)
        DotB, LabelB = CreateDot(self, 1.5, 0+Y, 'B', DOWN)
        LineAB = CreateLine(self, DotA, DotB)
        
        DotC, LabelC = CreateDot(self, -0.5, 1.25+Y, '', LEFT)
        LabelC = CreateLabel(self, -0.125, 1.25+Y, 'C', UP)
        DotC_, LabelC_ = CreateDot(self, 0.25, 1.25+Y, '', RIGHT)
        
        LineC = CreateLine(self, DotC, DotC_)
        
        DotD, LabelD, LineAD = ProblemaII(self, DotA, DotC, DotC_, LineC,
            ['G','H','J', 'K', 'D'], [RIGHT, LEFT, LEFT, UP, DOWN], True
        )

        self.wait(1)

        CircleDEF = CreateCircleFromLine(self, DotA, DotD, LineAD)
        DotE, LabelE = CreateDot(self, 0.25, 0+Y, 'E', UP_RIGHT)
        LabelF = CreateLabel(self, -0.5 + 0.75*math.sqrt(1)/2, Y-0.75*math.sqrt(3)/2, 'F', DOWN)
        LineAE = CreateLine(self, DotA, DotE, False)

        self.wait(2)

        self.play(FadeOut(CircleDEF), FadeOut(LabelF), FadeOut(DotD), FadeOut(LabelD), FadeOut(LineAD))

        self.play(
            LabelA.animate.next_to(DotA, LEFT, buff=0.1),
            LabelB.animate.next_to(DotB, RIGHT, buff=0.1),
            LabelE.animate.next_to(DotE, UP, buff=0.1),
            run_time=0.5,
            rate_func=smooth
        )

        self.wait(0.5)
        
        FirstLine = VGroup(LabelC, DotC, DotC_, LineC)
        SecondLine = VGroup(DotA, DotB, DotE, LineAB, LineAE, LabelA, LabelB, LabelE)

        y_shift_for_FirstLine = (ORIGIN)[1] - FirstLine.get_center()[1] + 0.04
        y_shift_for_SecondLine = (ORIGIN)[1] - SecondLine.get_center()[1]

        self.play(
            FirstLine.animate.shift(UP * y_shift_for_FirstLine),
            SecondLine.animate.shift(UP * y_shift_for_SecondLine)
        )

        self.play(FadeOut(LineAB), FadeOut(DotB), FadeOut(LabelB), LabelE.animate.next_to(DotE, RIGHT, buff=0.1), run_time=0.5)
        SecondLine.remove(LineAB, DotB, LabelB)

        shift_for_FirstLine = ORIGIN + UP * 1 - FirstLine.get_center()
        shift_for_SecondLine = ORIGIN + DOWN * 1 - SecondLine.get_center()

        # Animate the shift
        self.play(
            FirstLine.animate.shift(shift_for_FirstLine),
            SecondLine.animate.shift(shift_for_SecondLine)
        )

        self.play(
            FirstLine.animate.move_to(ORIGIN + UP * 1),
            SecondLine.animate.next_to(FirstLine, DOWN, buff=1)
        )

        self.wait(0.5)

        self.play(
            FirstLine.animate.move_to(ORIGIN + UP * 1.5),
            SecondLine.animate.move_to(ORIGIN + DOWN * 1.5),
            FirstLine.animate.scale(2),
            SecondLine.animate.scale(2)
        )


        Quest = AddQuest(self, "Livro I - Problema III")
        Solution = AddSolution(self, [
            "Dadas as duas retas limitada AB, C, foi subtraída da",
            "maior AB, a AE igual à menor C; o que era preciso fazer."
        ])

        self.wait(3)

        self.play(FadeOut(Solution), FadeOut(Quest), FadeOut(FirstLine), FadeOut(SecondLine))
        self.wait(1)