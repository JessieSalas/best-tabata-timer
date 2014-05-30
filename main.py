from kivy.app import App
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager,Screen, WipeTransition
from kivy.uix.floatlayout import FloatLayout


Builder.load_string("""
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

<Beautiful>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            id: manager
            Screen:
                name: 'landing'
                FloatLayout:
                    canvas.before:
                        Color:
                            rgb: ( 0.968627451, 0.905882353, 0.77254902 )
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    Image: 
                        source: 'logo.png'
                        pos_hint: {'x':0.11, 'y': 0.22}
                        allow_stretch: True
                        size_hint: 0.87, 0.87
                    Button:
                        background_color: (0.945098039, 0.349019608, 0.164705882, 1)
                        background_normal: '' #disables premade kivy button background
                        text: '[color=f7e7c5] [b] CUSTOMIZE SETTINGS [b]'
                        markup: True
                        text_size: self.size
                        font_size: 20 
                        halign: 'center'
                        valign: 'middle'
                        size_hint: (1, 0.05)
                        pos_hint: {'x':0, 'y': 0}
                    Button:
                        background_color: (0.058823529, 0.458823529, 0.741176471, 1)
                        background_normal: ''
                        text: '[color=f7e7c5] [b] BEGIN [b]'
                        markup: True
                        text_size: self.size
                        font_size: 100 
                        halign: 'center'
                        valign: 'middle'
                        text_hint: (0.5, 0.5)
                        size_hint: (1, 0.13)
                        pos_hint: {'x':0, 'y':0.047}
                        on_press: manager.transition = FadeTransition()
                        on_release: manager.current = 'workspace'

            Screen: 
                name: 'workspace'
                FloatLayout:
                    canvas.before:
                        Color:
                            rgb: ( 0.968627451, 0.905882353, 0.77254902 )
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    Image: 
                        source: 'good_circle.png'
                        pos_hint: {'x': 0.11, 'y': 0.22}
                        allow_stretch: True
                        size_hint: 0.87, 0.87

""")

class Beautiful(FloatLayout):
    pass

class Accordion(Screen):
    pass

class TestApp(App):
    def build(self):
        return Beautiful()

if __name__ == '__main__':
    TestApp().run()
    
