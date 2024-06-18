import logging
import math
from manim import *
from utils import *
logging.basicConfig(level=logging.DEBUG)

class V(Scene):
    def construct(self):
        I_Y = -1.5
        IDotA, ILabelA = CreateDot(self, 0, I_Y+1, 'A', UP, False)
        IDotB, ILabelB = CreateDot(self, -0.375, I_Y+0, 'B', LEFT, False)
        IDotC, ILabelC = CreateDot(self, 0.375, I_Y+0, 'C', RIGHT, False)

        ILineAB = CreateLine(self, IDotA, IDotB, False)
        ILineBC = CreateLine(self, IDotB, IDotC, False)
        ILineCA = CreateLine(self, IDotC, IDotA, False)

        IDotD, ILabelD = CreateDot(self, -0.75, I_Y+-1, 'D', DOWN, False)
        IDotE, ILabelE = CreateDot(self, 0.75, I_Y+-1, 'E', DOWN, False)

        ILineDB = CreateLine(self, IDotD, IDotB, False)
        ILineCE = CreateLine(self, IDotC, IDotE, False)

        ITicksAB = CreateLineTick(self, ILineAB, 1, False)
        ITicksCA = CreateLineTick(self, ILineCA, 1, False)

        Condition = VGroup(IDotA, IDotB, IDotC, IDotD, IDotE,
                           ILabelA, ILabelB, ILabelC, ILabelD, ILabelE,
                           ILineAB, ILineBC, ILineCA, ILineDB, ILineCE,
                           ITicksAB, ITicksCA)
        
        Condition.set_opacity(0)

        IAngleABC = CreateAngle(self, IDotB, ILineBC, ILineAB, False, TEAL, 0.2)
        IAngleBCA = CreateAngle(self, IDotC, ILineCA, ILineBC, False, TEAL, 0.2)
        IAngleGCB = CreateAngle(self, IDotC, ILineCE, ILineBC, False, YELLOW, 0.15, True)
        IAngleCBF = CreateAngle(self, IDotB, ILineBC, ILineDB, False, YELLOW, 0.15)
        
        Success = VGroup(IAngleABC, IAngleBCA, IAngleGCB, IAngleCBF, Condition)
        Success.set_opacity(0)

        Introduction(self,
            "Livro I - Problema V", 
            ("Os ângulos junto à base dos triângulos isósceles são iguais entre si, e, tendo sido\n"
            "prolongadas ainda mais as retas iguais, os ângulos sob a base serão iguais entre si."),
            
            Condition, Success
        )

        DotA, LabelA = CreateDot(self, 0, 1, 'A', UP)
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

        DotF, LabelF = CreateDot(self, -0.5, -1/3, 'F', LEFT)
        LineAD = CreateLine(self, DotA, DotD, False)
        LineFA = CreateLine(self, DotF, DotA, False)
        LineAE = CreateLine(self, DotA, DotE, False)

        DotG, LabelG, LineDG = ProblemaII(self, DotA, DotF, DotA, LineFA,
            ['','','', '', 'G'], [RIGHT, LEFT, LEFT, UP, DOWN], True
        )

        RotateLine(self, LineDG, LineAE, DotG, LabelG)
        self.play(LabelG.animate.next_to(DotG, RIGHT, buff=0.1))

        self.wait(2) 

        LineAG = CreateLine(self, DotA, DotG, False)

        LineGB = CreateLine(self, DotG, DotB)
        LineFC = CreateLine(self, DotF, DotC)

        LineAC = CreateLine(self, DotA, DotC, False)
        AngleBAC = CreateAngle(self, DotA, LineAC, LineBA, True, RED, 0.2)

        self.wait(1)

        AngleFAC = CreateAngle(self, DotA, LineAC, LineBA, False, RED, 0.2)
        AngleBAG = CreateAngle(self, DotA, LineAC, LineBA, False, RED, 0.2)

        DotA1 = DotA.copy()
        DotA2 = DotA.copy()
        DotB1 = DotB.copy()
        DotC1 = DotC.copy()
        DotF1 = DotF.copy()
        DotG1 = DotG.copy()

        LabelA1 = LabelA.copy()
        LabelA2 = LabelA.copy()
        LabelB1 = LabelB.copy()
        LabelF1 = LabelF.copy()
        LabelC1 = LabelC.copy()
        LabelG1 = LabelG.copy()

        LineGB1 = LineGB.copy()
        LineCF = CreateLine(self, DotC, DotF, False)

        TriangleAFC = VGroup(LineFA, LineFC, LineCA, LabelA1, LabelF1, LabelC1, DotA1, DotF1, DotC1, AngleFAC)
        TriangleAGB = VGroup(LineAG, LineGB1, LineBA, LabelA2, LabelG1, LabelB1, DotA2, DotB1, DotG1, AngleBAG)

        self.play(TriangleAFC.animate.shift(1.5*LEFT),
                  TriangleAGB.animate.shift(1.5*RIGHT))
        
        self.play(FadeOut(DotA, LabelA, DotB, LabelB, DotC, LabelC, DotD, LabelD, DotE, LabelE, DotF, LabelF, DotG, LabelG,
                          LineGB, LineCF, LineAD, LineBC, LineBD, LineAE, LineCE, LineDG, LineAC, AngleBAC))
        
        TicksAB = CreateLineTick(self, LineBA, 1)
        TicksCA = CreateLineTick(self, LineCA, 1)
        TicksFA = CreateLineTick(self, LineFA, 2)
        TicksAG = CreateLineTick(self, LineAG, 2)

        self.wait(1)

        LabelEq = CreateLabel(self, 0, 0, '≡', DOWN*0, True, 40)

        AngleAFC = CreateAngle(self, DotF1, LineFA, LineCF, True, BLUE, 0.15)
        AngleBGA = CreateAngle(self, DotG1, LineGB, LineAG, True, BLUE, 0.15)

        AngleACF = CreateAngle(self, DotC1, LineCA, LineFC, True, GREEN, 0.2, True)
        AngleABG = CreateAngle(self, DotB1, LineBA, LineGB, True, GREEN, 0.2)

        self.play(FadeOut(TicksAB, TicksCA, TicksFA, TicksAG, AngleFAC, AngleBAG, LabelEq))

        self.play(FadeIn(DotA, LabelA, DotB, LabelB, DotC, LabelC, DotD, LabelD, DotE, LabelE, DotF, LabelF, DotG, LabelG,
                        LineGB, LineCF, LineAD, LineBC, LineBD, LineAE, LineCE, LineDG, LineAC, AngleBAC))
        
        TriangleAFC = VGroup(TriangleAFC, AngleAFC, AngleACF)
        TriangleAGB = VGroup(TriangleAGB, AngleBGA, AngleABG)

        self.play(TriangleAFC.animate.shift(-1.5*LEFT),
                  TriangleAGB.animate.shift(-1.5*RIGHT))
        
        AngleAFC1 = CreateAngle(self, DotF1, LineFA, LineCF, False, BLUE, 0.15)
        AngleACF1 = CreateAngle(self, DotC1, LineCA, LineFC, False, GREEN, 0.2, True)

        AngleBGA1 = CreateAngle(self, DotG1, LineGB, LineAG, False, BLUE, 0.15)
        AngleABG1 = CreateAngle(self, DotB1, LineBA, LineGB, False, GREEN, 0.2)
        
        LineCG = CreateLine(self, DotC, DotG, False)
        LineFB = CreateLine(self, DotF, DotB, False)

        self.play(FadeOut(TriangleAFC, TriangleAGB))

        DotB1 = DotB.copy()
        DotB2 = DotB.copy()
        DotC1 = DotC.copy()
        DotC2 = DotC.copy()

        LabelB1 = LabelB.copy()
        LabelB2 = LabelB.copy()
        LabelC1 = LabelC.copy()
        LabelC2 = LabelC.copy()

        LineBC1 = LineBC.copy()
        LineBC2 = LineBC.copy()
        LineFC1 = LineFC.copy()

        TriangleBCG = VGroup(DotB1, DotC1, DotG1, LabelB1, LabelC1, LabelG1, LineBC1, LineGB1, LineCG, AngleBGA)
        TriangleBCF = VGroup(DotB2, DotC2, DotF1, LabelB2, LabelC2, LabelF1, LineBC2, LineFB, LineFC1, AngleAFC)

        self.play(TriangleBCG.animate.shift(1.75*LEFT),
                  TriangleBCF.animate.shift(1.75*RIGHT))
        
        self.play(FadeOut(DotA, LabelA, DotB, LabelB, DotC, LabelC, DotD, LabelD, DotE, LabelE, DotF, LabelF, DotG, LabelG,
            LineGB, LineCF, LineAD, LineBC, LineBD, LineAE, LineCE, LineDG, LineAC,
            AngleBAC, AngleAFC1, AngleACF1, AngleBGA1, AngleABG1))

        TicksCG = CreateLineTick(self, LineCG, 1)
        TicksFB = CreateLineTick(self, LineFB, 1)
        TicksGB = CreateLineTick(self, LineGB1, 2)
        TicksFC = CreateLineTick(self, LineFC1, 2)

        self.wait(1)

        LabelEq = CreateLabel(self, 0, 0, '≡', DOWN*0, True, 40)

        AngleGBC = CreateAngle(self, DotB1, LineBC, LineGB, True, PINK, 0.25)
        AngleBCF = CreateAngle(self, DotC2, LineCF, LineBC, True, PINK, 0.25, True)

        AngleGCB = CreateAngle(self, DotC1, LineCG, LineBC, True, YELLOW, 0.15, True)
        AngleCBF = CreateAngle(self, DotB2, LineBC, LineFB, True, YELLOW, 0.15)
        
        self.play(FadeOut(TicksCG, TicksFB, TicksGB, TicksFC, LabelEq))

        TriangleBCG = VGroup(TriangleBCG, AngleGBC, AngleGCB)
        TriangleBCF = VGroup(TriangleBCF, AngleBCF, AngleCBF)

        self.play(FadeIn(DotA, LabelA, DotB, LabelB, DotC, LabelC, DotD, LabelD, DotE, LabelE, DotF, LabelF, DotG, LabelG,
            LineGB, LineCF, LineAD, LineBC, LineBD, LineAE, LineCE, LineDG, LineAC,
            AngleBAC, AngleAFC1, AngleACF1, AngleBGA1, AngleABG1))

        self.play(TriangleBCG.animate.shift(-1.75*LEFT),
                  TriangleBCF.animate.shift(-1.75*RIGHT))
        
        AngleGBC1 = CreateAngle(self, DotB1, LineBC, LineGB, False, PINK, 0.25)
        AngleBCF1 = CreateAngle(self, DotC2, LineCF, LineBC, False, PINK, 0.25, True)

        AngleGCB1 = CreateAngle(self, DotC1, LineCG, LineBC, False, YELLOW, 0.15, True)
        AngleCBF1 = CreateAngle(self, DotB2, LineBC, LineFB, False, YELLOW, 0.15)

        LineAB = CreateLine(self, DotA, DotB, False)

        self.play(FadeOut(TriangleBCG, TriangleBCF))

        self.wait(2)

        ReduceArcSize(self, AngleGBC1, 0.2)
        AngleABC = CreateAngle(self, DotB, LineBC, LineAB, False, GREEN, 0.2)
        self.play(FadeOut(AngleABG1, AngleGBC1), ApplyMethod(AngleABC.set_color, TEAL))

        ReduceArcSize(self, AngleBCF1, 0.2)
        AngleBCA = CreateAngle(self, DotC, LineCA, LineBC, False, GREEN, 0.2)
        self.play(FadeOut(AngleACF1, AngleBCF1), ApplyMethod(AngleBCA.set_color, TEAL))

        self.play(FadeOut(DotF, DotG, LabelF, LabelG, LineAB, LineGB, LineCF,
                          AngleBAC, AngleBGA1, AngleAFC1))

        Quest = AddQuest(self, "Livro I - Problema V")
        Solution = AddSolution(self, [
            "Portanto, os ângulos junto à base dos triângulos isósceles são iguais, e ao",
            "prolongar as retas iguais, os ângulos sob a base serão iguais, o que era preciso provar."
        ])

        self.wait(3)

        self.play(FadeOut(Solution, Quest, AngleGCB1, AngleCBF1, AngleABC, AngleBCA,
                          DotA, LabelA, DotB, LabelB, DotC, LabelC, DotD, LabelD, DotE, LabelE,
                          LineAB, LineAC, LineBC, LineBD, LineCE, LineAE, LineAD, LineAG, LineDG))

        self.wait(1)
