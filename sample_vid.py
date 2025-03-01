from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        self.wait(2)
        self.play(FadeOut(circle))
        # self.wait(2)
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen
class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()
class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()

class FibonacciSpiral(Scene):
    def construct(self):
        scaler = 0.1
        a= 1 * scaler
        b = 1 * scaler
        arcs = []
        pt1 = Point(location=[0, 1 * scaler, 0], color = BLACK)
        arc1 = Arc(radius = 1 * scaler, start_angle=-PI/2, angle=PI, arc_center=pt1.location)
        arcs.append(arc1)
        pt2 = Point(location = [pt1.location[0], pt1.location[1]-b, 0], color = BLACK)
        arc2 = Arc(radius = 2 * scaler, start_angle=PI/2, angle=PI/2, arc_center=pt2.location)
        arcs.append(arc2)
        self.add(pt1)
        self.add(pt2)
        init_pt = pt2
        for i in range(10):
            a, b = a+b, a
            if i%4 == 0:
                new_pt = Point(location = [init_pt.location[0]+b, init_pt.location[1], 0], color = BLACK)
                self.add(new_pt)
                init_pt = new_pt
                new_arc = Arc(radius = a+b, start_angle = PI, angle = PI/2, arc_center=new_pt.location)
                arcs.append(new_arc)
            elif i%4 == 1:
                new_pt = Point(location = [init_pt.location[0], init_pt.location[1]+b, 0], color = BLACK)
                self.add(new_pt)
                init_pt = new_pt
                new_arc = Arc(radius = a+b, start_angle = -PI/2, angle = PI/2, arc_center=new_pt.location)
                arcs.append(new_arc)
            elif i%4 == 2:
                new_pt = Point(location = [init_pt.location[0]-b, init_pt.location[1], 0], color = BLACK)
                self.add(new_pt)
                init_pt = new_pt
                new_arc = Arc(radius = a+b, start_angle = 0, angle = PI/2, arc_center=new_pt.location)
                arcs.append(new_arc)
            else:
                new_pt = Point(location = [init_pt.location[0], init_pt.location[1]-b, 0], color = BLACK)
                self.add(new_pt)
                init_pt = new_pt
                new_arc = Arc(radius = a+b, start_angle = PI/2, angle = PI/2, arc_center=new_pt.location)
                arcs.append(new_arc)
        arcs_grp = VGroup(arcs)
        self.play(Create(arcs_grp), run_time = 3)
        self.wait(2)
        fibo_seq = Tex(r"1 \quad 1 \quad 2 \quad 3\quad 5\quad 8\quad 13\quad 21\quad 34\quad 55\quad 89\quad 144", font_size=40)
        self.play(FadeOut(arcs_grp),Write(fibo_seq), run_time = 2)
        self.wait(2)
        self.play(FadeOut(fibo_seq))
class PetersonGraph(Scene):
    def construct(self):
        scaler = 3
        # Define the vertices of the Peterson graph
        vertices = [
            [scaler * np.cos(2 * np.pi * i / 5),scaler *  np.sin(2 * np.pi * i / 5), 0] for i in range(5)
        ] + [
            [scaler * 0.5 * np.cos(2 * np.pi * i / 5 + np.pi / 5), scaler * 0.5 * np.sin(2 * np.pi * i / 5 + np.pi / 5), 0] for i in range(5)
        ]

        # Define the edges of the Peterson graph
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),  # Outer pentagon
            (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),  # Inner pentagon
            (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)   # Connecting edges
        ]

        # Create the vertices as dots
        dots = VGroup(*[Dot(point=vertices[i], color=BLUE) for i in range(10)])

        # Create the edges as lines
        lines = VGroup(*[Line(vertices[start], vertices[end], color=WHITE) for start, end in edges])

        # Add the vertices and edges to the scene
        name = Text("Đồ thị Peterson", font_size = 30)
        name.next_to(dots, DOWN)
        self.play(Create(dots), Create(lines), Write(name), run_time = 3)
        self.wait(2)
        self.play(FadeOut(dots), FadeOut(lines), FadeOut(name))

class Question1(Scene):
    def construct(self):
        question1 = Text("Bạn đã bao giờ tự hỏi...", font_size=80)
        self.play(Write(question1), run_time = 4)
        self.wait(2)
        self.play(FadeOut(question1))
        
class Question2(Scene):
    def construct(self):
        question2 = Text("Tại sao thế giới  tuân theo \n những quy luật kỳ diệu?", font_size=50)
        self.wait(2)
        self.play(Write(question2), run_time = 4)
        self.wait(2)
        self.play(FadeOut(question2))
class WeierstrassFunction(Scene):
    def construct(self):
        # Define the Weierstrass function
        def weierstrass(x, a=0.5, b=3, n=100):
            return sum(a**k * np.cos(b**k * np.pi * x) for k in range(n))

        # Create the axes
        axes = Axes(
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            axis_config={"color": BLUE},
        )

        # Create the graph of the Weierstrass function
        graph = axes.plot(lambda x: weierstrass(x), color=RED)
        name = Text("Hàm Weierstrass", font_size = 30)
        name.next_to(graph, DOWN)
        # Add the axes and graph to the scene
        self.play(Create(graph), run_time = 3)
        self.wait(2)
class Figure8Knot(Scene):
    def construct(self):
        # Define the parametric function for the figure-8 knot
        def figure_8_knot(t):
            x = (2 + np.cos(2 * t)) * np.cos(3 * t)
            y = (2 + np.cos(2 * t)) * np.sin(3 * t)
            z = np.sin(4 * t)
            return np.array([x, y, z])

        # Create the parametric curve for the figure-8 knot
        knot = ParametricFunction(
            figure_8_knot,
            t_range=[0, TAU],
            color=BLUE
        )
        # Add the knot to the scene
        self.play(Create(knot), run_time=4)
        self.wait(2)
# OK, I know how to edit videos :) But can do all in Python too.
class EulerFormula(Scene):
    def construct(self):
        euler_formula = MathTex(r"e^{i\pi} + 1 = 0", font_size = 60)
        self.play(Write(euler_formula), run_time = 2)
        self.wait(1)
        self.play(FadeOut(euler_formula))
class MyFaculty(Scene):
    def construct(self):
        img = ImageMobject(r"Images\\mim_inversed.v1.png")
        name = Text(r"Khoa Toán - Cơ - Tin học", font_size = 70)
        img.next_to(ORIGIN, UP)
        name.next_to(img, DOWN)
        self.play(FadeIn(img), Write(name))
        self.wait(2)
        self.play(FadeOut(img), FadeOut(name))
class SolarSystem(Scene):
    def construct(self):
        # Create the Sun
        sun = Dot(color=YELLOW).scale(2)
        # sun_label = Text("Sun", font_size=24).next_to(sun, DOWN)
        # Create the planets and their orbits
        planets = [
            {"name": "Mercury", "color": GREY, "radius": 1.5, "orbit_radius": 1},
            {"name": "Venus", "color": ORANGE, "radius": 1.5, "orbit_radius": 1.25},
            {"name": "Earth", "color": BLUE, "radius": 1.5, "orbit_radius": 1.5},
            {"name": "Mars", "color": RED, "radius": 1.5, "orbit_radius": 1.75},
            {"name": "Jupiter", "color": DARK_BROWN, "radius": 2, "orbit_radius": 2},
            {"name": "Saturn", "color": GOLD, "radius": 2, "orbit_radius": 2.25},
            {"name": "Uranus", "color": BLUE_D, "radius": 1.7, "orbit_radius": 2.5},
            {"name": "Neptune", "color": DARK_BLUE, "radius": 1.7, "orbit_radius": 2.75},
        ]

        # Add the Sun to the scene
        self.play(FadeIn(sun))

        # Create and add the planets and their orbits to the scene
        for i in range(len(planets)):
            planet = planets[i]
            orbit = Circle(radius=planet["orbit_radius"], color=WHITE, stroke_opacity=0.5, arc_center = sun.get_center())
            planet_dot = Dot(color=planet["color"]).scale(planet["radius"])
            
            # Position the planet on its orbit
            planet_dot.move_to(orbit.point_from_proportion(np.random.rand()))
            
            # Add the orbit, planet, and label to the scene
            self.play(Create(orbit), FadeIn(planet_dot))

class FlyablePaperPlaneAndSolarAndPeterson(Scene):
    def construct(self):
        # Create a paper plane shape using a Polygon
        paper_plane = Polygon(
            [-6, -6, 0], [-6-1/4,-6+ 1/4, 0], [-6+2/4, -6, 0], [-6-1/4, -6-1/4, 0],
            color=WHITE, fill_opacity=1
        )

        # Define the path for the paper plane to follow
        path = VMobject()
        path.set_points_smoothly([
            [-6, -5, 0], [-4, -3, 0], [-2, -1, 0], [-4, 1, 0], [-2, 3, 0], [-1, 5, 0]
        ])
        
        # Create the animation
        
        angle_tracker = ValueTracker(0)
        # Function to update the rotation of the paper plane
        def update_rotation(mob: Polygon, alpha):
            point = path.point_from_proportion(alpha)
            next_point = path.point_from_proportion(min(alpha + 0.01, 1))
            direction = next_point - point
            angle = np.arctan2(direction[1], direction[0])
            mob.move_to(point)
            mob.rotate(angle - angle_tracker.get_value(), about_point = point)
            angle_tracker.set_value(angle)
        dashed_path = DashedVMobject(path)
        scaler = 1
        # Define the vertices of the Peterson graph
        vertices = [
            [3+scaler * np.cos(2 * np.pi * i / 5),2+scaler *  np.sin(2 * np.pi * i / 5), 0] for i in range(5)
        ] + [
            [3+scaler * 0.5 * np.cos(2 * np.pi * i / 5 + np.pi / 5), 2+scaler * 0.5 * np.sin(2 * np.pi * i / 5 + np.pi / 5), 0] for i in range(5)
        ]

        # Define the edges of the Peterson graph
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),  # Outer pentagon
            (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),  # Inner pentagon
            (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)   # Connecting edges
        ]

        # Create the vertices as dots
        dots = VGroup(*[Dot(point=vertices[i], color=BLUE) for i in range(10)])

        # Create the edges as lines
        lines = VGroup(*[Line(vertices[start], vertices[end], color=WHITE) for start, end in edges])

        # Add the vertices and edges to the scene
        name = Text("Đồ thị Peterson", font_size = 25)
        name.next_to(dots, DOWN)
        # Create the Sun
        sun = Dot(color=YELLOW).scale(2)
        # sun_label = Text("Sun", font_size=24).next_to(sun, DOWN)
        # Create the planets and their orbits
        planets = [
            {"name": "Mercury", "color": GREY, "radius": 1, "orbit_radius": 0.4},
            {"name": "Venus", "color": ORANGE, "radius": 1, "orbit_radius": 0.5},
            {"name": "Earth", "color": BLUE, "radius": 1, "orbit_radius": 0.6},
            {"name": "Mars", "color": RED, "radius": 1, "orbit_radius": 0.7},
            {"name": "Jupiter", "color": DARK_BROWN, "radius": 1.5, "orbit_radius": 0.8},
            {"name": "Saturn", "color": GOLD, "radius": 1.5, "orbit_radius": 0.9},
            {"name": "Uranus", "color": BLUE_D, "radius": 1.2, "orbit_radius": 1},
            {"name": "Neptune", "color": DARK_BLUE, "radius": 1.2, "orbit_radius": 1.1},
        ]


        # Create and add the planets and their orbits to the scene
        sun.shift(RIGHT * 3 + 1*DOWN)
        self.play(FadeIn(sun))
        for i in range(len(planets)):
            planet = planets[i]
            orbit = Circle(radius=planet["orbit_radius"], color=WHITE, stroke_opacity=0.5, arc_center = sun.get_center())
            planet_dot = Dot(color=planet["color"]).scale(planet["radius"])
            
            
            # Position the planet on its orbit
            planet_dot.move_to(orbit.point_from_proportion(np.random.rand()))
            
            # Add the Sun to the scene
            self.play(Create(orbit), FadeIn(planet_dot))
        kepler = MathTex("T^2 = \dfrac{4\pi^2 r^3}{GM}")
        kepler.next_to(orbit, DOWN)
        self.play(Create(dots),  Create(dashed_path), run_time = 1.5)
        # Move the paper plane along the path and update its rotation
        self.play(
            MoveAlongPath(paper_plane, path, rate_func = linear),
            UpdateFromAlphaFunc(paper_plane, update_rotation), Create(lines), Write(name),Write(kepler),
            run_time=5
        )
        animations_out = []
        for obj in self.mobjects:
            animations_out.append(FadeOut(obj))
        self.play(*animations_out)
        self.wait(1)
class PaperPlanePlusFibo(Scene):
    def construct(self):
        scaler = 0.1
        a= 1 * scaler
        b = 1 * scaler
        arcs = []
        pt1 = Point(location=[0, 1 * scaler, 0], color = BLACK)
        arc1 = Arc(radius = 1 * scaler, start_angle=-PI/2, angle=PI, arc_center=pt1.location)
        arcs.append(arc1)
        pt2 = Point(location = [pt1.location[0], pt1.location[1]-b, 0], color = BLACK)
        arc2 = Arc(radius = 2 * scaler, start_angle=PI/2, angle=PI/2, arc_center=pt2.location)
        arcs.append(arc2)
        self.add(pt1)
        self.add(pt2)
        init_pt = pt2
        for i in range(10):
            a, b = a+b, a
            if i%4 == 0:
                new_pt = Point(location = [init_pt.location[0]+b, init_pt.location[1], 0], color = BLACK)
                self.add(new_pt)
                init_pt = new_pt
                new_arc = Arc(radius = a+b, start_angle = PI, angle = PI/2, arc_center=new_pt.location)
                arcs.append(new_arc)
            elif i%4 == 1:
                new_pt = Point(location = [init_pt.location[0], init_pt.location[1]+b, 0], color = BLACK)
                self.add(new_pt)
                init_pt = new_pt
                new_arc = Arc(radius = a+b, start_angle = -PI/2, angle = PI/2, arc_center=new_pt.location)
                arcs.append(new_arc)
            elif i%4 == 2:
                new_pt = Point(location = [init_pt.location[0]-b, init_pt.location[1], 0], color = BLACK)
                self.add(new_pt)
                init_pt = new_pt
                new_arc = Arc(radius = a+b, start_angle = 0, angle = PI/2, arc_center=new_pt.location)
                arcs.append(new_arc)
            else:
                new_pt = Point(location = [init_pt.location[0], init_pt.location[1]-b, 0], color = BLACK)
                self.add(new_pt)
                init_pt = new_pt
                new_arc = Arc(radius = a+b, start_angle = PI/2, angle = PI/2, arc_center=new_pt.location)
                arcs.append(new_arc)
        path = VMobject()
        for arc in arcs:
            path.append_points(arc.get_all_points())
        dashed_path = DashedVMobject(path, num_dashes=100)
        self.play(Create(dashed_path), run_time = 4)
        paper_plane = Polygon(
            [0, 0, 0], [-1/4, 1/4, 0], [2/4,0 , 0], [-1/4, -1/4, 0],
            color=WHITE, fill_opacity=1
        )
        angle_tracker = ValueTracker(0)
        # Function to update the rotation of the paper plane
        def update_rotation(mob: Polygon, alpha):
            point = path.point_from_proportion(alpha)
            next_point = path.point_from_proportion(min(alpha + 0.01, 1))
            direction = next_point - point
            angle = np.arctan2(direction[1], direction[0])
            mob.move_to(point)
            mob.rotate(angle - angle_tracker.get_value(), about_point = point)
            angle_tracker.set_value(angle)
        self.play(
            MoveAlongPath(paper_plane, path, rate_func = linear),
            UpdateFromAlphaFunc(paper_plane, update_rotation),
            run_time=5
        )
        self.play(FadeOut(paper_plane, dashed_path))
class EulerLine(Scene):
    def construct(self):
        A = np.array([0, 6, 0])
        B = np.array([4, 2, 0])
        C = np.array([-4, -2, 0])
        triangle = Polygon(A, B, C, color = BLUE, fill_opacity = 0.4)
        centroid = (A+B+C)/3
        # Calculate the circumcenter
        def perpendicular_bisector(p1, p2):
            midpoint = (p1 + p2) / 2
            slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            perpendicular_slope = -1 / slope
            return midpoint, perpendicular_slope

        mid_AB, slope_AB = perpendicular_bisector(A, B)
        mid_BC, slope_BC = perpendicular_bisector(B, C)

        circumcenter_x = (mid_BC[1] - mid_AB[1] + slope_AB * mid_AB[0] - slope_BC * mid_BC[0]) / (slope_AB - slope_BC)
        circumcenter_y = slope_AB * (circumcenter_x - mid_AB[0]) + mid_AB[1]
        circumcenter = np.array([circumcenter_x, circumcenter_y, 0])

        # Calculate the orthocenter
        def altitude(p1, p2, p3):
            slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            perpendicular_slope = -1 / slope
            return p3, perpendicular_slope

        alt_A, slope_A = altitude(B, C, A)
        alt_B, slope_B = altitude(A, C, B)

        orthocenter_x = (alt_B[1] - alt_A[1] + slope_A * alt_A[0] - slope_B * alt_B[0]) / (slope_A - slope_B)
        orthocenter_y = slope_A * (orthocenter_x - alt_A[0]) + alt_A[1]
        orthocenter = np.array([orthocenter_x, orthocenter_y, 0])

        # Create dots to mark the centroid, circumcenter, and orthocenter
        centroid_dot = Dot(centroid, color=ORANGE)
        centroid_label = Text("G", font_size=24).next_to(centroid_dot, DOWN + RIGHT)

        circumcenter_dot = Dot(circumcenter, color=ORANGE)
        circumcenter_label = Text("O", font_size=24).next_to(circumcenter_dot, DOWN + RIGHT)

        orthocenter_dot = Dot(orthocenter, color=ORANGE)
        orthocenter_label = Text("H", font_size=24).next_to(orthocenter_dot, DOWN + RIGHT)
        euler_line = Line(circumcenter_dot, orthocenter_dot)
        # Add the triangle, centroid, circumcenter, and orthocenter to the scene
        self.play(Create(triangle))
        self.play(FadeIn(centroid_dot), Write(centroid_label))
        self.play(FadeIn(circumcenter_dot), Write(circumcenter_label))
        self.play(FadeIn(orthocenter_dot), Write(orthocenter_label))
        self.play(Create(euler_line), run_time = 1)
        self.wait(2)
class CollatzSequence(Scene):
    def construct(self):
        # the outtro
        row1 = MathTex(r"27\qquad 41\qquad 62\qquad 31\qquad 47\qquad 71\qquad 107", font_size = 40)
        row1.shift(UP*2.5)
        row2 = MathTex(r"161\qquad 242\qquad 121\qquad 182\qquad 91\qquad 137\qquad 206", font_size = 40)
        row2.next_to(row1, DOWN)
        row3 = MathTex(r"103\qquad 155\qquad 233\qquad 350\qquad 175\qquad 263\qquad 395", font_size = 40)
        row3.next_to(row2, DOWN)
        row4 = MathTex(r"593\qquad 890\qquad 445\qquad 668\qquad 334\qquad 167\qquad 251", font_size = 40)
        row4.next_to(row3, DOWN)
        row5 = MathTex(r"377\qquad 566\qquad 283\qquad 425\qquad 638\qquad 319\qquad 479", font_size = 40)
        row5.next_to(row4, DOWN)
        row6 = MathTex(r"719\qquad 1079\qquad 1619\qquad 2429\qquad 3644\qquad 1822\qquad 911", font_size = 40)
        row6.next_to(row5, DOWN)
        row7 = MathTex(r"1367\qquad 2051\qquad 3077\qquad 4616\qquad 2308\qquad 1154\qquad 577", font_size = 40)
        row7.next_to(row6, DOWN)
        row8 = MathTex(r"866\qquad 433\qquad 650\qquad 325\qquad 488\qquad 244\qquad 122", font_size = 40)
        row8.next_to(row7, DOWN)
        row9 = MathTex(r"61\qquad 92\qquad 46\qquad 23\qquad 35\qquad 53\qquad 80", font_size = 40)
        row9.next_to(row8, DOWN)
        row10 = MathTex(r"40\qquad 20\qquad 10\qquad 5\qquad 8\qquad 4\qquad 2\qquad 1\qquad", font_size = 40)
        row10.next_to(row9, DOWN)
        thanks1 = Text("Hãy kết nối với chúng tôi", font_size = 44)
        thanks1.shift(UP)
        thanks2 = Text("và bắt đầu hành trình Toán học của bạn!", font_size=44)
        thanks2.next_to(thanks1, DOWN)
        self.play(Write(row1))
        self.play(FadeOut(row1), Write(row2))
        self.play(FadeOut(row2, target_position = row1), Write(row3))
        self.play(FadeOut(row3,target_position = row2), Write(row4))
        self.play(FadeOut(row4, target_position = row3), Write(row5))
        self.play(FadeOut(row5, target_position = row4), Write(row6))
        self.play(FadeOut(row6, target_position = row5), Write(row7), Write(thanks1))
        self.play(FadeOut(row7, target_position = row6), Write(row8), Write(thanks2))
        self.play(FadeOut(row8, target_position = row7), Write(row9))
        self.play(FadeOut(row9, target_position = row8), Write(row10))
        self.play(FadeOut(thanks1,thanks2))
        self.play(FadeOut(row10))




class JuliaSet(Scene):
    def construct(self):
        img = ImageMobject(r"Images\\julia_set.png")
        label = Text("Một tập Julia", font_size=24)
        label.next_to(img, DOWN)
        self.play(FadeIn(img), Write(label))
        self.wait(2)
        self.play(FadeOut(img), FadeOut(label))
class PseudoSphere(Scene):
    def construct(self):
        img = ImageMobject(r"Images\\pseudosphere-inversed.png")
        label = Text("Mặt giả cầu (pseudosphere)", font_size=24)
        label.next_to(img, DOWN)
        self.play(FadeIn(img), Write(label))
        self.wait(2)
        self.play(FadeOut(img), FadeOut(label))
# begin the execution by adjusting Master
class Declares(Scene):
    def construct(self):
        declare1 = Text("Toán học chính là ngôn ngữ của vũ trụ!", font_size =50, t2c={"ngôn ngữ của vũ trụ!": BLUE})
        self.play(Write(declare1), run_time = 2)
        self.wait(2)
        self.play(FadeOut(declare1))
        declare2 = Text("Không chỉ là những con số, hình dạng...", font_size = 50)
        self.play(Write(declare2), run_time = 2)
        self.wait(2)
        self.play(FadeOut(declare2))
class VisualMath(Scene):
    def construct(self):
        A = np.array([-3, -4, 0])
        B = np.array([-1, -0, 0])
        C = np.array([-5, -2, 0])
        triangle = Polygon(A, B, C, color = BLUE, fill_opacity = 0.4)
        centroid = (A+B+C)/3
        # Calculate the circumcenter
        def perpendicular_bisector(p1, p2):
            midpoint = (p1 + p2) / 2
            slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            perpendicular_slope = -1 / slope
            return midpoint, perpendicular_slope

        mid_AB, slope_AB = perpendicular_bisector(A, B)
        mid_BC, slope_BC = perpendicular_bisector(B, C)

        circumcenter_x = (mid_BC[1] - mid_AB[1] + slope_AB * mid_AB[0] - slope_BC * mid_BC[0]) / (slope_AB - slope_BC)
        circumcenter_y = slope_AB * (circumcenter_x - mid_AB[0]) + mid_AB[1]
        circumcenter = np.array([circumcenter_x, circumcenter_y, 0])

        # Calculate the orthocenter
        def altitude(p1, p2, p3):
            slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            perpendicular_slope = -1 / slope
            return p3, perpendicular_slope

        alt_A, slope_A = altitude(B, C, A)
        alt_B, slope_B = altitude(A, C, B)

        orthocenter_x = (alt_B[1] - alt_A[1] + slope_A * alt_A[0] - slope_B * alt_B[0]) / (slope_A - slope_B)
        orthocenter_y = slope_A * (orthocenter_x - alt_A[0]) + alt_A[1]
        orthocenter = np.array([orthocenter_x, orthocenter_y, 0])

        # Create dots to mark the centroid, circumcenter, and orthocenter
        centroid_dot = Dot(centroid, color=ORANGE)
        centroid_label = Text("G", font_size=12).next_to(centroid_dot, DOWN + RIGHT)

        circumcenter_dot = Dot(circumcenter, color=ORANGE)
        circumcenter_label = Text("O", font_size=12).next_to(circumcenter_dot, DOWN + RIGHT)

        orthocenter_dot = Dot(orthocenter, color=ORANGE)
        orthocenter_label = Text("H", font_size=12).next_to(orthocenter_dot, DOWN + RIGHT)
        euler_line = Line(orthocenter_dot, circumcenter_dot)
        # Add the triangle, centroid, circumcenter, and orthocenter to the scene
        euler_formula = MathTex(r"e^{i\pi} + 1 = 0", font_size = 30)
        pseudosphere = ImageMobject(r"Images\\pseudosphere-inversed.png")
        julia_set = ImageMobject(r"Images\\julia_set.png")  
        pseudosphere.set_z_index(1)
        julia_set.set_z_index(0)
        euler_formula.next_to(triangle, 5*UP)
        pseudosphere.next_to(euler_formula,9*RIGHT)
        julia_set.next_to(triangle, 5*RIGHT)
        self.play(Create(triangle), Write(euler_formula))
        self.play(FadeIn(centroid_dot), Write(centroid_label), FadeIn(pseudosphere))
        self.play(FadeIn(circumcenter_dot), Write(circumcenter_label), FadeIn(julia_set))
        self.play(FadeIn(orthocenter_dot), Write(orthocenter_label))
        self.play(Create(euler_line), run_time = 1)  
        self.wait(2)
        animations_out = []
        for obj in self.mobjects:
            animations_out.append(FadeOut(obj, target_position = ORIGIN))
        self.play(*animations_out, run_time = 1.5)
        declare3 = Text("Toán học là vẻ đẹp của sự chính xác.", font_size = 50)
        self.play(Write(declare3), run_time = 2)
        self.wait(2)
        self.play(FadeOut(declare3))
class Introduction(Scene):
    def construct(self):
        name = Text("Nhóm Tư vấn Tuyển sinh ngành Toán học", font_size = 40)
        name.next_to(ORIGIN, 4*UP)
        members = ["Đặng Thùy Trang", "Nguyễn Ngọc Mai Anh", "Nguyễn Duy Nam", "Vũ Thùy Linh", "Trịnh Xuân Vũ", "Đỗ Thị Hải Hằng", "Nguyễn Thùy Trang", "Nguyễn Thị Mai Hương", "Hà Thủy Linh", "Nguyễn Tiến Khánh", "Phạm Ngọc Mai", "Lê Xuân Hoàng", "Hán Lê Khánh Linh", "Nguyễn Thị Như"]
        cool_names = ["The Axiomatist", "The Dreamer", "The Innovator", "The Paradox", "The Topologist", "The Conjecturer", "The Proof Chaser", "The Infinity Explorer", "The Prime Hunter", "The Geometer", "The Cryptographer", "The Logician", "The Chaos Tamer", "The Mathemagician"]
        mob_mem = [Text(members[i] + " - " + cool_names[i], font_size = 30) for i in range(len(members))]
        self.play(Write(name))
        for member in mob_mem:
            self.play(Write(member))
            self.play(FadeOut(member), run_time = 0.5)
        self.play(FadeOut(name))
        who = Text("Chúng tôi là ai?", font_size = 50)
        how_can_we_help = Text("Bạn sẽ được giúp đỡ như thế nào?", font_size = 50)
        who.next_to(ORIGIN, 2*UP)
        how_can_we_help.next_to(who, DOWN)
        answer1 = Text("Chúng tôi là những sinh viên ngành Toán học,", font_size = 30, t2c={"Toán học": BLUE})
        answer2 = Text("sẽ đồng hành cùng bạn...", font_size = 30)
        answer1.next_to(ORIGIN, 5*UP)
        answer2.next_to(answer1, DOWN)
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage[utf8]{inputenc}")
        tex_template.add_to_preamble(r"\usepackage[T5]{fontenc}")
        tex_template.add_to_preamble(r"\usepackage{vntex}")
        ans = Tex(r"\begin{itemize}\item[$\bullet$] Tư vấn tuyển sinh\item[$\bullet$] Khám phá chương trình học\item[$\bullet$] Giải đáp thắc mắc\end{itemize}", tex_template=tex_template, font_size = 50)
        ans.next_to(answer2, 2*DOWN)
        self.play(Write(who),Write(how_can_we_help), run_time = 2)
        self.play(FadeOut(who, how_can_we_help))
        self.play(Write(answer1))
        self.play(Write(answer2))
        self.play(Write(ans))
        self.wait(2)
        self.play(FadeOut(answer1, answer2, ans))

class MasterScreen(Scene):
    def construct(self):
        PaperPlanePlusFibo.construct(self)
        Question1.construct(self)
        Question2.construct(self)
        FlyablePaperPlaneAndSolarAndPeterson.construct(self)
        Declares.construct(self)
        VisualMath.construct(self)
        MyFaculty.construct(self)
        Introduction.construct(self)
        CollatzSequence.construct(self)

