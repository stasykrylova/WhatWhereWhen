from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
import time
from kivy.clock import Clock


class MainWindow(Screen):
    sound = SoundLoader.load("meeting (online-audio-converter.com).wav")
    sound.play()

    def change_screen(self):
        vol = 1

        for i in range(0, 20):
            self.sound.volume = vol
            time.sleep(0.05)
            vol -= 0.05
        self.sound.stop()


class ThirdWindow(Screen):
    sound = SoundLoader.load("volchok (online-audio-converter.com).wav")
    cl = Clock
    gamer_score = 0
    viewer_score = 0

    def play(self):
        pass

    def make_score(self):
        self.score.text = str(self.gamer_score) + ':' + str(self.viewer_score)

    def change_screen(self):
        self.manager.transition = RiseInTransition(duration=0.5)
        self.manager.current = 'question'

    def start_anim(self):
        self.sound.play()
        gif = self.ids.gif
        gif.anim_delay = 0.05
        gif._coreimage.anim_reset(True)
        self.cl.schedule_once(callback=lambda dt: self.sound.stop(), timeout=6)
        self.cl.schedule_once(callback=lambda dt: self.change_screen(), timeout=6)


class SecondWindow(Screen):
    sound = SoundLoader.load("button_sound.wav")


class QuestionWindow(Screen):
    correctly = False
    btn_sound = SoundLoader.load("button_sound.wav")

    def check_correct(self):
        ans_gamer = self.answer.text
        answer = "Calling func with answer"

        if self.check(answer, ans_gamer):

            self.correctly = True
            ans_sound = SoundLoader.load("correct.wav")
            self.question.text = "Правильный ответ!"
        else:

            ans_sound = SoundLoader.load("incorrect.wav")
            self.question.text = "Неправильный ответ!"

        ans_sound.play()
        Clock.schedule_once(callback=lambda dt: self.change_screen(), timeout=1)

    def change_screen(self):
        self.manager.transition = RiseInTransition(duration=0.5)
        self.manager.current = 'third'

    @staticmethod
    def check(str_a, str_b):

        if str_a[0] == ' ':
            str_a = str(list(str_a).pop(0))
        if str_a[-1] == ' ':
            str_a = str(list(str_a).pop(-1))

        if str(" " + str_a.lower() + " ") in str(" " + str_b.lower() + " "):
            return True
        else:
            return False

    def ask_question(self):
        self.question.text = "Here will be question func call"


class Manager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    app = MainApp()
    app.run()
