from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.settings import SettingsWithTabbedPanel
from settings import settings_json

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
                        on_release: app.open_settings()
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
                        on_release: root.number(5)
                        on_release: root.poop()
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
    def poop(self):
        print( "poop")
    
    def rev(self, listy):
        return list(reversed(listy))
    
    def countdown(self,worktime):
        l = Label(text= "{0}".format( self.rev(   [i for i in range(0, int(worktime))]   )   ))
        self.add_widget(l)

    def setter(self, instance, value):
        instance.text_size = (value-20, None)

    def number(self, num):
        l = Label(text= ' [b] {0} [b] '.format(int(num)), markup = True, allow_stretch= True, font_size = '400px')
        self.add_widget(l)

class Accordion(Screen):
    pass

class TestApp(App):
    def build(self):
        self.settings_cls = SettingsWithTabbedPanel
        self.use_kivy_settings = False
        self.preptime = self.config.get('customize', 'preptime')
        setting = self.config.get('customize', 'boolexample')
        setting = self.config.get('customize', 'boolexample')
        setting = self.config.get('customize', 'boolexample')
        setting = self.config.get('customize', 'boolexample')
        return Beautiful()
  
    def swagg(self):
        l = Label(text='THIS IS SWAGG')
        add_widget(l) 
    def build_config(self, config):
        config.setdefaults('customize', {
            'sound': True,
            'preptime': 10,
            'worktime': 20,
            'resttime': 10,
            'reps': 8,
            'sets': 1})
    
    def build_settings(self, settings):
        settings.add_json_panel('BEST Tabata \n Timer', self.config, data = settings_json)

    def on_config_change(self, config, section, key, value):
        print( "You have changed a setting, dear friend")

if __name__ == '__main__':
    TestApp().run()
    
