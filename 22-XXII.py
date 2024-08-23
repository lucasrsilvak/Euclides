import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class XXII(Scene):
    def construct(self):
        I_Y = -2.85
        I_X = 2.95
        IDotA, ILabelA = CreateDot(self, -5+I_X, 2+I_Y, 'A', LEFT, False)
        IDotA2, ILabelA2 = CreateDot(self, -2.5+I_X, 2+I_Y, '', RIGHT, False)
        ILineA = CreateLine(self, IDotA, IDotA2, False)

        IDotB, ILabelB = CreateDot(self, -5+I_X, 1.5+I_Y, 'B', LEFT, False)
        IDotB2, ILabelB2 = CreateDot(self, -3+I_X, 1.5+I_Y, '', RIGHT, False)
        ILineB = CreateLine(self, IDotB, IDotB2, False)

        IDotC, ILabelC = CreateDot(self, -5+I_X, 1+I_Y, 'C', LEFT, False)
        IDotC2, ILabelC2 = CreateDot(self, -3.5+I_X, 1+I_Y, '', RIGHT, False)
        ILineC = CreateLine(self, IDotC, IDotC2, False)

        Condition = VGroup(IDotA, IDotB, IDotC, ILabelA, ILabelB, ILabelC, ILineA, ILineB, ILineC, IDotA2, IDotB2, IDotC2)
        Condition.set_opacity(0)

        IDotF, ILabelF = CreateDot(self, 0.25, -2.25, 'F', DOWN, False)
        IDotG, ILabelG = CreateDot(self, 2.25, -2.25, 'G', DOWN, False)
        IDotK, ILabelK = CreateDot(self, 2.25, -0.75, 'K', UP, False)

        ILineFG = CreateLine(self, IDotF, IDotG, False)
        ILineFK = CreateLine(self, IDotF, IDotK, False)
        ILineKG = CreateLine(self, IDotK, IDotG, False)

        Success = VGroup(Condition, IDotF, IDotG, IDotK, ILabelF, ILabelG, ILabelK, ILineFG, ILineFK, ILineKG)
        Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema XXII", 
            ("De três retas, que são iguais as três retas dadas,\n"
             "construir um triângulo; e é preciso as duas, sendo.\n"
             "tomadas juntas de toda maneira, ser maiores do que\n"
             "do que o restante."),
            Condition, Success
        )

        DotA, LabelA = CreateDot(self, -5, 2, 'A', LEFT)
        DotA2, LabelA2 = CreateDot(self, -2.5, 2, '', RIGHT)
        LineA = CreateLine(self, DotA, DotA2)

        DotB, LabelB = CreateDot(self, -5, 1.5, 'B', LEFT)
        DotB2, LabelB2 = CreateDot(self, -3, 1.5, '', RIGHT)
        LineB = CreateLine(self, DotB, DotB2)

        DotC, LabelC = CreateDot(self, -5, 1, 'C', LEFT)
        DotC2, LabelC2 = CreateDot(self, -3.5, 1, '', RIGHT)
        LineC = CreateLine(self, DotC, DotC2)

        DotD, LabelD = CreateDot(self, -3.25, -1.25, 'D', LEFT)
        DotE, LabelE = CreateDot(self, 3.25, -1.25, 'E', RIGHT)
        LineDE = CreateLine(self, DotD, DotE)

        LineA = VGroup(LineA, DotA, DotA2)
        LineA2 = LineA.copy()
        LineB = VGroup(LineB, DotB, DotB2)
        LineB2 = LineB.copy()
        LineC = VGroup(LineC, DotC, DotC2)
        LineC2 = LineC.copy()

        MoveLineToDot(self, LineA2, DotA, DotD)

        DotF, LabelF = CreateDot(self, -0.75, -1.25, '', DOWN, False)
        LabelF = CreateLabel(self, -0.75, -1.25, 'F', DOWN)
        LineDF = CreateLine(self, DotD, DotF)

        MoveLineToDot(self, LineB2, DotB, DotF)

        DotG, LabelG = CreateDot(self, 1.25, -1.25, '', DOWN, False)
        LabelG = CreateLabel(self, 1.25, -1.25, 'G', DOWN)
        LineFG = CreateLine(self, DotF, DotG)

        MoveLineToDot(self, LineC2, DotC, DotG)

        DotH, LabelH = CreateDot(self, 2.75, -1.25, '', DOWN, False)
        LabelH = CreateLabel(self, 2.75, -1.25, 'H', DOWN_RIGHT)
        LineGH = CreateLine(self, DotG, DotH)

        CircleDKL = CreateCircleFromLine(self, DotF, DotD, LineDF)
        CircleLKH = CreateCircleFromLine(self, DotG, DotH, LineGH)

        DotK, LabelK = CreateDot(self, 1.25, 0.25, 'K', UP)

        LineFK = CreateLine(self, DotF, DotK)
        LineKG = CreateLine(self, DotK, DotG)
        TriangleFGK = VGroup(DotF, DotG, DotK, LabelF, LabelG, LabelK, LineFG, LineFK, LineKG)

        self.play(FadeOut(DotD, DotE, DotH, LabelD, LabelE, CircleDKL, CircleLKH, LineDE, LineA2, LineB2, LineC2, LineDF, LineGH, LabelH))

        LinesDesc = VGroup(LabelA, LineA, DotA, DotA2, LabelB, LineB, DotB, DotB2, LabelC, LineC, DotC, DotC2)
        self.play(LinesDesc.animate.shift(1.85*DOWN + 2.95*RIGHT), TriangleFGK.animate.shift(1.00*RIGHT))

        # FIM

        Quest = AddQuest(self, "Livro I - Problema XXII")
        Solution = AddSolution(self, [
            "Portanto, das três retas KF, FG, GK, que são iguais às três dadas A, B, C",
            "foi construído o triângulo KFG; o que era preciso fazer."
        ])

        self.wait(3)

        self.play(FadeOut(Solution, Quest, LinesDesc, TriangleFGK))

        self.wait(1)
