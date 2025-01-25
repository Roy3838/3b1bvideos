
from manim_imports_ext import *

from _2024.inscribed_rect.helpers import *



class OttoScene(InteractiveScene):
    def construct(self):



        title = TexText(R"Conjetura de Toeplitz, 1911", font_size=72)
        otto = ImageMobject("/Users/jay/Desktop/otto.png").scale(1.3)

        title.to_edge(UP)
        otto.to_edge(RIGHT)
        otto.shift(LEFT)

        self.add(title,otto)

        self.wait(6) 
