import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class V(Scene):
    def construct(self):
        I_Y = -4
        IDotA, ILabelA = CreateDot(self, -1, 0+I_Y, 'A', DOWN_LEFT, False)
        IDotB, ILabelB = CreateDot(self, 1, 0+I_Y, 'B', DOWN_RIGHT, False)
        ILineAB = CreateLine(self, IDotA, IDotB, False)
        Condition = VGroup(IDotA, ILabelA, IDotB, ILabelB, ILineAB)
        #Condition.set_opacity(0)

        IDotC, ILabelC = CreateDot(self, 0, math.sqrt(3)+I_Y, 'C', DOWN_RIGHT, False)
        ILineBC = CreateLine(self, IDotB, IDotC, False)
        ILineCA = CreateLine(self, IDotC, IDotA, False)
        ITriangleABC = AssembleTriangle(self, ILineAB, ILineBC, ILineCA)
        ITriangleABC = AddTicksToTriangle(self, ITriangleABC, False)
        
        Success = VGroup(ITriangleABC, Condition)
        #Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema I", 
            "Construir um triângulo equilátero sobre a reta limitada dada.",
            Condition, Success
        )

        DotA, LabelA = CreateDot(self, 0, 1, 'A', UP)
        LabelA2 = CreateLabel(self, 0, 1, 'A', UP, False)
        DotB, LabelB = CreateDot(self, -0.375, 0, 'B', LEFT)
        DotC, LabelC = CreateDot(self, 0.375, 0, 'C', RIGHT)

        LineBA = CreateLine(self, DotB, DotA)
        LineBC = CreateLine(self, DotB, DotC)
        LineCA = CreateLine(self, DotC, DotA)

        DotD, LabelD = CreateDot(self, -0.75, -1, 'D', DOWN)
        DotE, LabelE = CreateDot(self, 0.75, -1, 'E', DOWN)

        LineBD = CreateLine(self, DotB, DotD)
        LineCE = CreateLine(self, DotC, DotE)

        self.wait(2)

        DotF, LabelF = CreateDot(self, -0.46875, -0.25, 'F', LEFT)
        LineAD = CreateLine(self, DotA, DotD, False)
        LineAF = CreateLine(self, DotA, DotF, False)
        LineAE = CreateLine(self, DotA, DotE, False)

        DotG, LabelG, LineDG = ProblemaII(self, DotA, DotF, DotA, LineAF,
            ['','','', '', 'G'], [RIGHT, LEFT, LEFT, UP, DOWN], True
        )

        RotateLine(self, LineDG, LineAE, DotG, LabelG)
        self.play(LabelG.animate.next_to(DotG, RIGHT, buff=0.1))

        self.wait(2) 

        LineAG = CreateLine(self, DotA, DotG, False)

        LineGB = CreateLine(self, DotG, DotB)
        LineFC = CreateLine(self, DotF, DotC)

        LineGB2 = CreateLine(self, DotG, DotB, False)
        LineFC2 = CreateLine(self, DotF, DotC, False)

        TriangleAFC = AssembleTriangle(self, LineAF, LineFC, LineCA)
        TriangleAFC = VGroup(TriangleAFC, LabelA, LabelF, LabelC)
        TriangleAGB = AssembleTriangle(self, LineAG, LineGB, LineBA)
        TriangleAGB = VGroup(TriangleAGB, LabelA2, LabelG, LabelB)

        self.play(TriangleAFC.animate.move_to(ORIGIN + 2*LEFT),
                  TriangleAGB.animate.move_to(ORIGIN + 2*RIGHT))


        Quest = AddQuest(self, "Livro I - Problema I")
        Solution = AddSolution(self, [
            "Sobre a reta limitada dada AB, foi construído",
            "um triângulo equilátero, o que era preciso fazer."
        ])

        self.wait(3)

        self.play(FadeOut(Solution), FadeOut(Quest))

        self.wait(1)
