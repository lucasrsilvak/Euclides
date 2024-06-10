import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class II(Scene):
    def construct(self):
        I_Y = -3.25 # Ajuda a Centralizar
        IDotA, ILabelA = CreateDot(self, -0.375, I_Y + -0.375*math.sqrt(3)/3, 'A', DOWN_LEFT, False)
        IDotB, ILabelB = CreateDot(self, 0, I_Y + 0, 'B', UP_RIGHT, False)
        IDotC, ILabelC = CreateDot(self, 0, I_Y + 1.25, 'C', UP, False)
        ILineBC        = CreateLine(self, IDotB, IDotC, False)
        
        Condition = VGroup(IDotA, ILabelA, IDotB, ILabelB, IDotC, ILabelC, ILineBC)
        Condition.set_opacity(0)

        IDotL, ILabelL = CreateDot(self, -0.375, I_Y + -0.375*math.sqrt(3)/3-1.25, 'L', DOWN_RIGHT, False)
        ILineAL = CreateLine(self, IDotA, IDotL, False)
        Success = VGroup(IDotL, ILabelL, ILineAL, Condition)
        Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema II", 
            "Pôr, no ponto dado, uma reta igual à reta dada.",
            Condition, Success
        )

        Y = 0.25 # ajuda muito na edição

        DotA, LabelA = CreateDot(self, -0.375, Y + -0.375*math.sqrt(3)/3, 'A', DOWN_LEFT)
        DotB, LabelB = CreateDot(self, 0, Y+0, 'B', UP_RIGHT)
        DotC, LabelC = CreateDot(self, 0, Y+1.5, 'C', UP)
        self.wait(1)
        LineBC = CreateLine(self, DotB, DotC)
        self.wait(1)

        DotD, LabelD, LineAB, LineBD, LineDA = ProblemaI(self, DotA, DotB, 'D', UP_LEFT)
        DotE, LabelE = CreateDot(self, -0.375, Y + -2.375, 'E', DOWN)
        DotF, LabelF = CreateDot(self, 2, Y + -2*math.sqrt(3)/3, 'F', DOWN)

        LineAE = CreateLine(self, DotA, DotE)
        LineBF = CreateLine(self, DotB, DotF)

        self.wait(1)

        CircleCGH = CreateCircleFromLine(self, DotB, DotC, LineBC)
        DotG, LabelG = CreateDot(self, 3*math.sqrt(3)/4, Y + -0.75, 'G', DOWN)
        LabelH = CreateLabel(self, -3*math.sqrt(3)/4, Y + 0.75, 'H', UP_LEFT)

        self.wait(1)

        LineFG = CreateLine(self, DotF, DotG, False)
        LineDG = CreateLine(self, DotD, DotG, False)
        self.remove(LineBF)
    
        CircleGKL = CreateCircleFromLine(self, DotD, DotG, LineDG)
        DotL, LabelL = CreateDot(self, -0.375, Y + math.sqrt(3)/8-math.sqrt(39+12*math.sqrt(3))/4, 'L', DOWN_RIGHT)
        LabelK = CreateLabel(self, -0.75-3*math.sqrt(3)/4, Y + 0.75+0.75*math.sqrt(3)/3, 'K', UP_LEFT)

        LineAL = CreateLine(self, DotA, DotL, False)

        self.wait(3)

        self.play(
            FadeOut(CircleCGH),
            FadeOut(CircleGKL),
            FadeOut(LineAE),
            FadeOut(LineAB),
            FadeOut(LineBF),
            FadeOut(LineBD),
            FadeOut(LineDA),
            FadeOut(LineDG),
            FadeOut(LineFG),
            FadeOut(DotD),
            FadeOut(DotE),
            FadeOut(DotF),
            FadeOut(DotG),
            FadeOut(LabelD),
            FadeOut(LabelE),
            FadeOut(LabelF),
            FadeOut(LabelG),
            FadeOut(LabelH),
            FadeOut(LabelK)
        )

        self.play(
            LabelA.animate.next_to(DotA, UP, buff=0.1),
            LabelB.animate.next_to(DotB, DOWN, buff=0.1),
            LabelL.animate.next_to(DotL, DOWN, buff=0.1),
            run_time=0.5,
            rate_func=smooth
        )

        FirstLine   = VGroup(DotB, DotC, LineBC, LabelB, LabelC)
        SecondLine  = VGroup(DotA, DotL, LineAL, LabelA, LabelL)

        # Generate targets for animation
        FirstLine.generate_target()
        SecondLine.generate_target()

        current_y_center_FirstLine = FirstLine.get_center()[1]
        current_y_center_SecondLine = SecondLine.get_center()[1]
        
        shift_y_FirstLine = -current_y_center_FirstLine  # This makes the y-coordinate zero
        shift_y_SecondLine = -current_y_center_SecondLine  # This makes the y-coordinate zero
        
        FirstLine.target.shift(UP * shift_y_FirstLine)
        SecondLine.target.shift(UP * shift_y_SecondLine)

        self.play(
            MoveToTarget(FirstLine),
            MoveToTarget(SecondLine),
            run_time=2
        )
        
        self.wait(3)
        
        self.play(
            FirstLine.animate.shift(DOWN * shift_y_FirstLine),
            SecondLine.animate.shift(DOWN * shift_y_SecondLine),
            run_time=2
        )

        self.wait(1)

        Quest = AddQuest(self, "Livro I - Problema II")
        Solution = AddSolution(self, [
            "No ponto dado A, foi posta a reta AL",
            "igual a reta dada BC, o que era preciso fazer."
        ])

        self.wait(5)

        self.play(FadeOut(Solution), FadeOut(Quest), FadeOut(FirstLine), FadeOut(SecondLine))
        self.wait(1)
