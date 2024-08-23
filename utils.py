import numpy as np
import math
from manim import *

COLOR = WHITE
LABEL_STROKE = 0.4

DOT_RADIUS = 0.05
DOT_STROKE = 0.4

LINE_STROKE = 2
LINE_TIME = 1

GREEK_TEXT = "Στοιχεῖα"
PORTUGUESE_TEXT = "Os Elementos"

UP_LEFT = (UP + LEFT) / 2
UP_RIGHT = (UP + RIGHT) / 2
DOWN_LEFT = (DOWN + LEFT) / 2
DOWN_RIGHT = (DOWN + RIGHT) / 2

def SetOpacity(obj, opacity):
    if isinstance(obj, VGroup):
        for subobj in obj.submobjects:
            SetOpacity(subobj, opacity)
    else:
        if isinstance(obj, Polygon):
            obj.set_stroke(opacity=opacity)
            obj.set_fill(opacity=0)
        elif isinstance(obj, Dot):
            obj.set_fill(opacity=1)
        elif isinstance(obj, Sector):
            obj.set_fill(opacity=0.5)
        elif isinstance(obj, Arc):
            obj.set_stroke(opacity=1)
            obj.set_fill(opacity=0)
        elif hasattr(obj, 'set_opacity'):
            obj.set_opacity(opacity)

def GetPhase(DotA, DotB):
    Ax, Ay, _ = DotA.get_center()
    Bx, By, _ = DotB.get_center()
    dx = Bx - Ax
    dy = By - Ay
    Phase = math.atan2(dy, dx)
    if Phase < 0: Phase += TAU
    return Phase

def Introduction(self, subtitle_text, description_text, Condition, Success):
    self.wait(1)
    
    title_greek = Text(GREEK_TEXT, font_size=40, color=WHITE)
    title_greek.to_edge(UP, buff=1)

    title_portuguese = Text(PORTUGUESE_TEXT, font_size=40, color=WHITE)
    title_portuguese.move_to(title_greek.get_center())

    subtitle = Text(subtitle_text, font_size=30, color=WHITE)
    subtitle.next_to(title_portuguese, DOWN, buff=0.5)

    description_lines = description_text.split('\n')
    description_vgroup = VGroup(*[
        Text(line.strip(), font_size=24, color=WHITE) for line in description_lines if line.strip()
    ])
    description_vgroup.arrange(DOWN, center=True, buff=0)
    description_vgroup.next_to(subtitle, DOWN, buff=0.5)

    self.play(Write(title_greek))
    self.wait(2)
    self.play(ReplacementTransform(title_greek, title_portuguese))
    
    self.play(
        FadeIn(subtitle, shift=UP),
        FadeIn(description_vgroup, shift=UP),
        run_time=3
    )

    self.wait(2)
    SetOpacity(Condition, 1)
    self.play(FadeIn(Condition), run_time=2)
    self.wait(2)

    self.play(FadeOut(Condition), run_time=0.5)

    SetOpacity(Success, 1)
    self.play(FadeIn(Success), run_time=2)
    self.wait(2)

    text_group = VGroup(title_portuguese, subtitle, description_vgroup, Success)
    self.play(FadeOut(text_group), run_time=1)

def AddQuest(self, quest_text):
    quest = Text(quest_text, font_size=30, color=WHITE)
    quest.to_edge(UP, buff=1)

    self.play(
        FadeIn(quest, shift=UP),
        run_time=3
    )

    return quest

def AddSolution(self, lines, font_size=24, color=WHITE, edge=DOWN, buff=1, animation=True):
    description_group = VGroup()
    for line in lines:
        text_line = Text(line, font_size=font_size, color=color)
        description_group.add(text_line)
    
    description_group.arrange(DOWN, center=True, buff=0.1)
    
    description_group.to_edge(edge, buff=buff)
    
    if animation:
        self.play(
            FadeIn(description_group, shift=UP),
            run_time=3
        )
    else:
        self.add(description_group)
    return description_group

def CreateLabel(self, x, y, text, side=DOWN, animate=True, size=20):
    Label = Text(text, font_size=size)
    Label.z_index = 10
    Label.set_stroke(width=0.4, color=BLACK)
    Label.set_opacity(0)

    reference_point = Dot(point=[x, y, 0], radius=DOT_RADIUS, fill_opacity=0)
    Label.next_to(reference_point, side, buff=0.1)

    if animate:
        Label.set_opacity(1)
        self.play(FadeIn(Label), run_time=1)

    return Label

def CreateDot(self, x, y, letter, side=DOWN, animate=True):
    if animate: y += 2

    dot = Dot(point=[x, y, 0], color=COLOR, radius=DOT_RADIUS, fill_opacity=0)

    label = Text(letter, font_size=20)
    label.z_index = 10
    label.set_stroke(width=0.4, color=BLACK)
    label.set_opacity(0)

    dot.z_index = 5

    if animate:
        dot_movement = dot.animate.shift(DOWN * 2).set_fill(opacity=1)
        self.play(dot_movement, run_time=0.5)

        label.next_to(dot, side, buff=0.1)
        label.set_opacity(1)

        self.play(FadeIn(label), run_time=0.5)
    else:
        dot.set_fill(opacity=1)

        label.next_to(dot, side, buff=0.1)
        label.set_opacity(1)
        self.add(dot, label)

    return dot, label

def CreateLine(self, DotA, DotB, animate=True):
    line = Line(DotA.get_center(), DotB.get_center(), color=COLOR, stroke_width=LINE_STROKE)
    line.z_index = 1
    if animate:
        self.play(Create(line), run_time = LINE_TIME)
    else:
        self.add(line)
    return line

def MoveLine(self, group, dotC, dotD):
    shiftA = dotC.get_center() - group[0].get_center()
    shiftB = dotD.get_center() - group[1].get_center()
    
    average_shift = (shiftA + shiftB) / 2
    
    self.play(group.animate.shift(average_shift))

def MoveLineToDot(self, group, dotA, dotB):
    shift_vector = dotB.get_center() - dotA.get_center()
    
    self.play(group.animate.shift(shift_vector))

def RotateLine(self, line_to_rotate, reference_line, Dot, Label):
    angle_to_rotate = line_to_rotate.get_angle()
    reference_angle = reference_line.get_angle()
    
    angle_difference = reference_angle - angle_to_rotate
    
    self.play(Rotate(line_to_rotate, angle_difference, about_point=line_to_rotate.get_start()),
              Rotate(Dot, angle_difference, about_point=line_to_rotate.get_start()),
              Label.animate.next_to(Dot, RIGHT, buff=0.1)
    )


def CreateCircleFromLine(self, Dot, DotB, Line, animate=True):
    center = Dot.get_center()
    Phase = GetPhase(Dot, DotB)
    radius = Line.get_length()
    animation_circle = Circle(radius=radius, color=WHITE, stroke_width=1).move_to(center)
    self.add(Line, animation_circle)

    if animate:
        self.arc_added = False
        self.arc = None

        def update_circle(mob, alpha, Phase):
            normalizated = False
            start_angle = Phase
            end_angle = (alpha * TAU + Phase)
            
            if end_angle > TAU:
                normalizated = True
                end_angle = (alpha * TAU + Phase)%TAU

            if normalizated:
                start_angle = 0
                if not self.arc_added:
                    self.arc = Arc(radius=radius, start_angle=Phase, angle=TAU-Phase, color=COLOR, stroke_width=1)
                    self.arc.move_arc_center_to(center)
                    self.arc.z_index = -1
                    self.add(self.arc)
                    self.arc_added = True

            mob.become(Circle(radius=radius, color=WHITE, stroke_width=1).move_to(center))
            mob.pointwise_become_partial(animation_circle, start_angle / TAU, end_angle / TAU)

        self.play(
            Rotate(Line, angle=2*PI, about_point=center, run_time=4),
            UpdateFromAlphaFunc(animation_circle, lambda m, a: update_circle(m, a, Phase), run_time=4)
        )

    if self.arc_added:
        self.remove(self.arc)

    self.remove(animation_circle)
    circle = Circle(radius=radius, color=WHITE, stroke_width=1).move_to(center)

    self.add(circle)
    return circle

def AddLabelToLine(self, line, label_text, position_factor=0.5, buff=0.1, font_style=None):
    point_on_line = line.point_from_proportion(position_factor)
    
    label = Text(label_text, font_style=font_style)
    label.next_to(point_on_line, UP, buff=buff)

    self.play(Create(label))
    return label

def AssembleTriangle(self, LineA, LineB, LineC):
    Triangle = Polygon(LineA.get_start(), LineB.get_start(), LineC.get_start(), color=COLOR)
    Triangle.set_stroke(width=LINE_STROKE)
    Triangle.set_fill(opacity=0)

    self.remove(LineA, LineB, LineC)
    self.add(Triangle)
    return Triangle

def MoveTriangle(self, triangle, dotD, dotE, dotF):
    target_triangle = Polygon(dotD.get_center(), dotE.get_center(), dotF.get_center(), color=triangle.get_color())
    
    self.play(Transform(triangle, target_triangle))

def AddTicksToTriangle(self, triangle, animate=True, tick_length=0.1, num_ticks=1):
    vertices = triangle.get_vertices()
    sides = [Line(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices))]
    tick_group = VGroup()
    for side in sides:
        tick = CreateTick(self, side, length=tick_length, num_ticks=num_ticks)
        tick_group.add(tick)

    if animate:
        self.play(FadeIn(tick_group), run_time = LINE_TIME)
    else:
        self.add(tick_group)
    tick_group.add(triangle)
    return tick_group

def CreateAngle(self, DotA, LineA, LineB, animate=True, color=WHITE, size=0.3, Inverse=False):
    if Inverse:
        LineA, LineB = LineB, LineA

    direction_A = LineA.get_end() - LineA.get_start()
    direction_B = LineB.get_start() - LineB.get_end()

    angle_A = np.arctan2(direction_A[1], direction_A[0])
    angle_B = np.arctan2(direction_B[1], direction_B[0])

    if (angle_A > angle_B):
        angle_A, angle_B = angle_B, angle_A

    if Inverse:
        angle_A += PI
        angle_B += PI

    arc_border = Arc(
        radius=size,
        start_angle=angle_A,
        angle=angle_B - angle_A,
        color=color,
        stroke_width=2,
        arc_center=DotA.get_center()
    )

    if animate:
        self.play(Create(arc_border), run_time=1)
    else:
        self.add(arc_border)

    return arc_border

def CreateTick(self, mark_line, length=0.1, num_ticks=1, position_factor=0.5):
    ticks = VGroup()
    line_direction = mark_line.get_unit_vector()
    perpendicular_direction = np.cross(line_direction, [0, 0, 1])
    for i in range(num_ticks):
        offset = (i - (num_ticks - 1) / 2.0) * length * 2
        tick = Line(
            start=mark_line.point_from_proportion(position_factor) + perpendicular_direction * length / 2 + offset * line_direction,
            end=mark_line.point_from_proportion(position_factor) - perpendicular_direction * length / 2 + offset * line_direction,
            color=WHITE,
            stroke_width=2,
        )
        ticks.add(tick)
    return ticks

def CreateLineTick(self, mark_line, num_ticks=1, animate=True, length=0.15, position_factor=0.5):
    ticks = VGroup()
    line_direction = mark_line.get_unit_vector()
    perpendicular_direction = np.cross(line_direction, [0, 0, 1])
    for i in range(num_ticks):
        offset = (i - (num_ticks - 1) / 2.0) * length * 0.5
        tick = Line(
            start=mark_line.point_from_proportion(position_factor) + perpendicular_direction * length / 2 + offset * line_direction,
            end=mark_line.point_from_proportion(position_factor) - perpendicular_direction * length / 2 + offset * line_direction,
            color=WHITE,
            stroke_width=2,
        )
        ticks.add(tick)
    if animate:
        self.play(FadeIn(ticks), run_time = 0.5)
    else:
        self.add(ticks)
    return ticks

def LineGetLength(Ax, Ay, Bx, By):
    return math.sqrt((Bx - Ax)**2 + (By - Ay)**2)

def Normalize(dx, dy):
    length = math.sqrt(dx**2 + dy**2)
    if length == 0:
        return 0, 0
    return dx / length, dy / length

def Equilaterar(Ax, Ay, Bx, By):
    Mx, My = (Ax + Bx) / 2, (Ay + By) / 2
    
    distance = math.sqrt((Bx - Ax)**2 + (By - Ay)**2)
    
    height = distance * math.sqrt(3) / 2
    
    vx = -(By - Ay)
    vy = Bx - Ax
    
    length_v = math.sqrt(vx**2 + vy**2)
    vx_norm = vx / length_v
    vy_norm = vy / length_v
    
    C1x, C1y = Mx + height * vx_norm, My + height * vy_norm
    C2x, C2y = Mx - height * vx_norm, My - height * vy_norm
    
    return C1x, C1y, C2x, C2y

def MoveToOrigin(self, group):
    centroid = sum([mobj.get_center() for mobj in group]) / len(group)
    
    shift_vector = ORIGIN - centroid + DOWN * 0.5
    
    self.play(group.animate.shift(shift_vector))

def ReduceArcSize(self, arc, reduced_radius):
    original_angle = arc.angle
    original_color = arc.get_color()
    original_start_angle = arc.start_angle

    reduced_arc = Arc(
        radius=reduced_radius, 
        start_angle=original_start_angle, 
        angle=original_angle, 
        color=original_color,
        stroke_width=arc.stroke_width,
        arc_center=arc.arc_center
    )

    self.play(Transform(arc, reduced_arc))
    self.wait(1)

def Intersection(DotA, radius, LineA, LineB):
    (Ax, Ay) = DotA
    (Bx, By) = LineA
    (Cx, Cy) = LineB

    if Bx != Cx:
        m = (Cy - By) / (Cx - Bx)
        b = By - m * Bx

        A = 1 + m**2
        B = 2 * (m * b - m * Ay - Ax)
        C = Ax**2 + (b - Ay)**2 - radius**2

        discriminant = B**2 - 4 * A * C

        if discriminant < 0:
            raise ValueError("The line does not intersect the circle.")
        
        x1 = (-B + np.sqrt(discriminant)) / (2 * A)
        x2 = (-B - np.sqrt(discriminant)) / (2 * A)
        
        y1 = m * x1 + b
        y2 = m * x2 + b

        DotE1 = (x1, y1)
        DotE2 = (x2, y2)
    else:
        x1 = Bx
        y1 = Ay + radius
        y2 = Ay - radius
        DotE1 = (x1, y1)
        DotE2 = (x1, y2)

    return DotE1, DotE2

def Intercept(self, DotA, DotB, LineAB, LineAC, letter, position, Complete=False):
    CircleABH = CreateCircleFromLine(self, DotA, DotB, LineAB, True)

    CenterE1, CenterE2 = Intersection((DotA.get_center()[0], DotA.get_center()[1]), LineAB.get_length(), (LineAC.get_start()[0], LineAC.get_start()[1]), (LineAC.get_end()[0], LineAC.get_end()[1]))

    DotD, LabelD = CreateDot(self, CenterE1[0], CenterE1[1], letter[0], position[0])
    DotE, LabelE = None, None

    if Complete:
        DotE, LabelE = CreateDot(self, CenterE2[0], CenterE2[1], letter[1], position[1])

    self.play(FadeOut(CircleABH))

    return DotD, LabelD, DotE, LabelE


def ProblemaI(self, DotA, DotB, letter, side, Invert = False):
    Ax, Ay, _ = DotA.get_center()
    Bx, By, _ = DotB.get_center()

    Cx, Cy, _, _ = Equilaterar(Ax, Ay, Bx, By)
    if Invert:
        _, _, Cx, Cy = Equilaterar(Ax, Ay, Bx, By)

    LineAB = CreateLine(self, DotA, DotB)

    CircleBC_1 = CreateCircleFromLine(self, DotA, DotB, LineAB)
    CircleBC_2 = CreateCircleFromLine(self, DotB, DotA, LineAB)

    DotC, LabelC = CreateDot(self, Cx, Cy, letter, side)

    LineBC = CreateLine(self, DotB, DotC)
    LineCA = CreateLine(self, DotC, DotA)

    self.play(FadeOut(CircleBC_1), FadeOut(CircleBC_2))
    return DotC, LabelC, LineAB, LineBC, LineCA

def ProblemaII(self, DotA, DotB, DotC, LineBC, letters=['D', 'E', 'F', 'G', 'L'], position=[RIGHT, LEFT, LEFT, UP, DOWN], Invert=False):
    Ax, Ay, _ = DotA.get_center()
    Bx, By, _ = DotB.get_center()
    Cx, Cy, _ = DotC.get_center()

    LengthBC = LineGetLength(Bx, By, Cx, Cy)

    DotD, LabelD, LineAB, LineBD, LineDA = ProblemaI(self, DotA, DotB, letters[0], position[0], Invert)
    Dx, Dy, _ = DotD.get_center()

    BDx, BDy = Normalize(Dx - Bx, Dy - By)
    BAx, BAy = Normalize(Dx - Ax, Dy - Ay)

    DotE, LabelE = CreateDot(self, Ax-BAx*2, Ay-BAy*2, letters[1], position[1])
    DotF, LabelF = CreateDot(self, Bx-BDx*2, By-BDy*2, letters[2], position[2])

    LineAE = CreateLine(self, DotA, DotE)
    LineBF = CreateLine(self, DotB, DotF)

    CircleCGH = CreateCircleFromLine(self, DotB, DotC, LineBC)

    DotG, LabelG = CreateDot(self, Bx - BDx*LengthBC, By - BDy*LengthBC, letters[3], position[3])
    
    Ex, Ey, _ = DotE.get_center()
    Gx, Gy, _ = DotG.get_center()

    AEx, AEy = Normalize(Ax - Ex, Ay - Ey)

    LineFG = CreateLine(self, DotF, DotG, False)
    LineDG = CreateLine(self, DotD, DotG, False)
    self.remove(LineBF)
    
    CircleGKL = CreateCircleFromLine(self, DotD, DotG, LineDG)
    DotL, LabelL = CreateDot(self, Ax - AEx*LengthBC, Ay - AEy*LengthBC, letters[4], position[4])

    LineAL = CreateLine(self, DotA, DotL, False)
    self.play(
        FadeOut(CircleCGH),
        FadeOut(CircleGKL),
        FadeOut(LineAE),
        FadeOut(LineAB),
        FadeOut(LineBF),
        FadeOut(LineBD),
        FadeOut(LineDA),
        FadeOut(LineDG),
        FadeOut(DotD),
        FadeOut(DotE),
        FadeOut(DotF),
        FadeOut(DotG),
        FadeOut(LabelD),
        FadeOut(LabelE),
        FadeOut(LabelF),
        FadeOut(LabelG),
        FadeOut(LineFG)
    )
    return DotL, LabelL, LineAL

def ProblemaIX(self, DotA, DotB, DotC, LineAB, LineCA, letters=['D', 'E', 'F'], position=[LEFT, RIGHT, DOWN], t=0.75, Invert=False):
    AngleBAC = CreateAngle(self, DotA, LineAB, LineCA, True, RED, 0.4)

    X = (1-t) * DotA.get_center()[0] + t * DotB.get_center()[0]
    Y = (1-t) * DotA.get_center()[1] + t * DotB.get_center()[1]

    DotD, LabelD = CreateDot(self, X, Y, letters[0], position[0])
    
    LineAD = CreateLine(self, DotA, DotD, False)
    LineAC = CreateLine(self, DotA, DotC, False)

    CircleADH = CreateCircleFromLine(self, DotA, DotD, LineAD, True)

    CenterE1, CenterE2 = Intersection((DotA.get_center()[0], DotA.get_center()[1]), LineAD.get_length(), (LineAC.get_start()[0], LineAC.get_start()[1]), (LineAC.get_end()[0], LineAC.get_end()[1]))

    if Invert:
        CenterE1=CenterE2

    DotE, LabelE = CreateDot(self, CenterE1[0], CenterE1[1], letters[1], position[1])

    self.play(FadeOut(CircleADH))

    DotF, LabelF, LineDE, LineEF, LineFD = ProblemaI(self, DotD, DotE, letters[2], position[2], True)

    LineFA = CreateLine(self, DotF, DotA)
    self.play(FadeOut(DotD, DotE, LabelD, LabelE, LineDE, LineEF, LineFD, LineAD, LineAC))

    return AngleBAC, DotF, LabelF, LineFA

def ProblemaX(self, DotA, DotB, letters, position, ratio, Invert):
    DotC, LabelC, LineAB, LineBC, LineCA = ProblemaI(self, DotA, DotB, letters[0], position[0])
    AngleBAC, DotF, LabelF, LineFA = ProblemaIX(self, DotC, DotA, DotB, LineCA, LineBC, [letters[1], letters[2], letters[3]], [position[1], position[2], position[3]], ratio, Invert)

    DotD, LabelD = CreateDot(self, 0, 0, letters[4], position[4])

    self.play(FadeOut(AngleBAC, DotC, DotF, LabelC, LabelF, LineAB, LineBC, LineCA, LineFA))
    return DotD, LabelD
