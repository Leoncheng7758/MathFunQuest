import kivy
kivy.require('2.3.0')
from kivy.app import App
from kivy.uix.label import Label

class MathFunQuestApp(App):
    def build(self):
        return Label(text='Math Fun Quest Coming Soon! \U0001F9E9', font_size=50)

if __name__ == '__main__':
    MathFunQuestApp().run()