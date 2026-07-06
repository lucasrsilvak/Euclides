import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class I3(Scene):
    def construct(self):
        I_Y = -1
        I_X = 2.95
        ICircleABC = CreateCircle(self, radius=1, color=WHITE, stroke=1, animate=False, y=I_Y)

        Condition = VGroup(ICircleABC)
        Condition.set_opacity(0)

        IDotF, ILabelF = CreateDot(self, 0, I_Y, 'F', RIGHT, False)

        Success = VGroup(Condition, IDotF, ILabelF)
        Success.set_opacity(0)

        Introduction(self,
            "Livro III - Problema I", 
            ("Achar o centro do círculo dado."),
            Condition, Success
        )

        Y = 0

        CircleABC = CreateCircle(self, radius=1, color=WHITE, stroke=1, animate=True)

        subtitle = Text("Escolha dois pontos A e B sobre o círculo e trace AB", font_size=20, color=WHITE)
        subtitle.move_to(UP*3)
        self.play(
            FadeIn(subtitle, shift=UP),
            run_time=3
        )

        DotA, LabelA = CreateDot(self, -math.sqrt(2)/2, Y - math.sqrt(2)/2, 'A', DOWN_LEFT)
        DotB, LabelB = CreateDot(self, math.sqrt(2)/2, Y - math.sqrt(2)/2, 'B', DOWN_RIGHT)
        self.wait(1)
        LineAB = CreateLine(self, DotA, DotB)
        self.wait(1)

        self.play(
            FadeOut(subtitle),
            run_time=3
        )

        subtitle = Text("Corte AB em duas retas iguais no ponto D e", font_size=20, color=WHITE)
        subtitle2 = Text("trace a CD perpendicular em ângulos retos com AB", font_size=20, color=WHITE)
        subtitle.move_to(UP*3)
        subtitle2.next_to(subtitle, DOWN, buff=0.1)
        self.play(
            FadeIn(subtitle, shift=UP),
            FadeIn(subtitle2, shift=UP),
            run_time=3
        )

        DotD, LabelD, DotExtra, LabelExtra, LineExtra = ProblemaX(self, DotA, DotB, ['', '', '', '', 'D'], [DOWN, RIGHT, LEFT, UP, UP_RIGHT], 0.7, False, Keep=True)

        DotC, LabelC = CreateDot(self, 0, Y + 1, 'C', UP)
        LineCD = CreateLine(self, DotD, DotC)
        self.play(FadeOut(DotExtra, LabelExtra, LineExtra))

        self.play(
            FadeOut(subtitle, subtitle2),
            run_time=3
        )
    
        subtitle = Text("Seja CD extendida até E", font_size=20, color=WHITE)
        subtitle.move_to(UP*3)
        self.play(
            FadeIn(subtitle, shift=UP),
            run_time=3
        )
        DotE, LabelE = CreateDot(self, 0, Y - 1, 'E', DOWN)
        LineDE = CreateLine(self, DotD, DotE)
        self.wait(1)
        LineCE = CreateLine(self, DotC, DotE, False)

        self.play(
            FadeOut(subtitle, DotA, LabelA, DotB, LabelB, LineAB, DotD, LabelD),
            run_time=3
        )
    
        subtitle = Text("Corte CE em duas retas iguais no ponto F", font_size=20, color=WHITE)
        subtitle.move_to(UP*3)
        self.play(
            FadeIn(subtitle, shift=UP),
            run_time=3
        )
        subtitle.z_index = 15

        DotF, LabelF, _, _, _ = ProblemaX(self, DotC, DotE, ['', '', '', '', 'F'], [DOWN, RIGHT, LEFT, UP, RIGHT], 0.625, True, False)
        self.play(
            FadeOut(subtitle),
            run_time=3
        )

        self.play(
            FadeOut(DotC, DotE, LabelC, LabelE, LineCD, LineCE, LineDE)
        )

        self.wait(2)

        Quest = AddQuest(self, "Livro I - Problema XXII")
        Solution = AddSolution(self, [
            "Portanto, foi encontrado o centro F do círculo ABC, o que era preciso fazer."
        ])

        self.wait(3)

        self.play(FadeOut(Solution, Quest, CircleABC, DotF, LabelF))

        self.wait(1)
