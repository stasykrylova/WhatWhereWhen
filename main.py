from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
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

    def play(self):
        pass

    def change_screen(self):
        self.manager.current = 'question'

    def start_anim(self):
        self.sound.play()
        gif = self.ids.gif
        gif.anim_delay = 0.05
        gif._coreimage.anim_reset(True)
        self.cl.schedule_once(callback=lambda dt: self.sound.stop(), timeout=6)
        self.cl.schedule_once(callback=lambda dt: self.change_screen(), timeout=6)


class SecondWindow(Screen):
    pass


class QuestionWindow(Screen):
    pass


class Manager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    app = MainApp()
    app.run()
