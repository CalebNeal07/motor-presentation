from manim import Circle, Title, Dot, GrowFromEdge, GrowFromCenter, MoveAlongPath, ORIGIN, BLUE, linear
# from manim_physics.electromagnetism.magnetostatics import *

from manim.mobject.opengl.opengl_mobject import LEFT
from manim_slides import Slide

class Test(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        title = Title("How Motors Create Rotational Motion")
        self.play(GrowFromEdge(title, LEFT))
        self.next_slide()

        self.play(GrowFromCenter(circle))
        self.next_slide()

        self.next_slide(loop=True)
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide()

        self.play(dot.animate.move_to(ORIGIN))
