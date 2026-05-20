import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
import random

# 设置窗口大小（适合儿童平板/手机）
Window.size = (800, 600)

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)
        
        title = Label(text='🧮 Math Fun Quest 🧮', 
                     font_size=80, 
                     color=get_color_from_hex('#FF6B6B'),
                     bold=True)
        subtitle = Label(text='数学益智冒险', font_size=40, color=get_color_from_hex('#4ECDC4'))
        
        btn_count = Button(text='1️⃣ 计数挑战', font_size=50, size_hint=(1, 0.2),
                          background_color=get_color_from_hex('#45B8AC'))
        btn_math = Button(text='2️⃣ 加减法小英雄', font_size=50, size_hint=(1, 0.2),
                         background_color=get_color_from_hex('#FF9F1C'))
        btn_shape = Button(text='3️⃣ 形状魔法', font_size=50, size_hint=(1, 0.2),
                          background_color=get_color_from_hex('#6C5CE7'))
        
        btn_count.bind(on_press=self.go_to_count)
        btn_math.bind(on_press=self.go_to_math)
        btn_shape.bind(on_press=self.go_to_shape)
        
        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(btn_count)
        layout.add_widget(btn_math)
        layout.add_widget(btn_shape)
        
        self.add_widget(layout)
    
    def go_to_count(self, instance):
        self.manager.current = 'count'
    
    def go_to_math(self, instance):
        self.manager.current = 'math'
    
    def go_to_shape(self, instance):
        self.manager.current = 'shape'


class CountGame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.question = Label(text='数一数有多少个🍎？', font_size=60)
        self.answer_layout = GridLayout(cols=3, spacing=20, size_hint_y=0.6)
        
        self.create_options()
        
        self.layout.add_widget(self.question)
        self.layout.add_widget(self.answer_layout)
        self.add_widget(self.layout)
    
    def create_options(self):
        self.answer_layout.clear_widgets()
        correct = random.randint(3, 8)
        options = [correct]
        while len(options) < 3:
            wrong = random.randint(1, 10)
            if wrong not in options:
                options.append(wrong)
        random.shuffle(options)
        
        for num in options:
            btn = Button(text=str(num), font_size=80)
            if num == correct:
                btn.bind(on_press=self.correct_answer)
            else:
                btn.bind(on_press=self.wrong_answer)
            self.answer_layout.add_widget(btn)
    
    def correct_answer(self, instance):
        self.score += 1
        Animation(opacity=0.3, duration=0.2).start(instance)
        instance.text = '✅'
        self.question.text = f'太棒了！当前 {self.score} 颗星 ✨'
        Clock.schedule_once(lambda dt: self.create_options(), 1.5)
    
    def wrong_answer(self, instance):
        Animation(opacity=0.4, duration=0.1).start(instance)


# 简化版加减法和形状游戏（后续再完善）
class MathGame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='加减法小英雄\n\n敬请期待更多关卡！', font_size=60))
        back_btn = Button(text='返回主菜单', font_size=40, size_hint=(1, 0.2))
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(back_btn)
        self.add_widget(layout)


class ShapeGame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='形状魔法\n\n识别圆形、正方形...\n敬请期待！', font_size=60))
        back_btn = Button(text='返回主菜单', font_size=40, size_hint=(1, 0.2))
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(back_btn)
        self.add_widget(layout)


class MathFunQuestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(CountGame(name='count'))
        sm.add_widget(MathGame(name='math'))
        sm.add_widget(ShapeGame(name='shape'))
        return sm


if __name__ == '__main__':
    from kivy.clock import Clock  # 延迟导入
    MathFunQuestApp().run()