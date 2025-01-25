from manim_imports_ext import *

from _2024.inscribed_rect.helpers import *



class Thanks(InteractiveScene):
    CONFIG={"background_color": "#E2E2E2",}
    def construct(self):

        title = TexText(R"Re-rendered animations made by 3b1b using",font_size=62).to_edge(UP)
        by = TexText(R"Translation by Roy Medina").shift(3*DOWN+2.5*RIGHT)

        logo = ImageMobject("/Users/jay/repos/manim/logo/cropped.png").shift(0.5*UP)
        
        self.play(FadeIn(logo))
        self.play(Write(title))
        self.play(Write(by))

        self.wait(6) 
