from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
import time


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
    tm = time

    def play(self):
        pass

    def make_sound(self):
        self.sound.play()

    def stop_sound(self):
        time.sleep(1)
        self.sound.stop()

    def anime_gif(self):
        gif = self.gf
        print(gif)

class SecondWindow(Screen):
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
