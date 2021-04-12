from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
import time
from kivy.clock import Clock


class MainWindow(Screen):
    sound = SoundLoader.load("start_sound.wav")
    sound.play()

    def change_screen(self):
        vol = 1

        for i in range(0, 20):
            self.sound.volume = vol
            time.sleep(0.05)
            vol -= 0.05
        self.sound.stop()


class ThirdWindow(Screen):
    sound = SoundLoader.load("game_sound.wav")
    cl = Clock
    gamer_score = 0
    viewer_score = 0

    def play(self):
        pass

    def if_win(self):
        if self.viewer_score == 6 or self.gamer_score == 6:

            if self.gamer_score == 6:
                self.cl.schedule_once(callback=lambda dt: self.win_game(), timeout=2)

            elif self.viewer_score == 6:
                self.cl.schedule_once(callback=lambda dt: self.loose_game(), timeout=2)

            self.cl.schedule_once(callback=lambda dt: self.update_score(), timeout=2)

# to do:
    # server part
    # make notepad with Question
    def update_score(self):
        self.viewer_score = 0
        self.gamer_score = 0

    def make_score(self):
        self.score.text = str(self.gamer_score) + ':' + str(self.viewer_score)
        self.but1.disabled = False

    def change_screen(self):
        self.manager.transition = RiseInTransition(duration=0.5)
        self.manager.current = 'question'

    def loose_game(self):
        self.manager.transition = RiseInTransition(duration=0.8)
        self.manager.current = 'last_loose'

    def win_game(self):
        self.manager.transition = RiseInTransition(duration=0.8)
        self.manager.current = 'last_win'

    def start_anim(self):
        self.sound.play()
        gif = self.ids.gif
        gif.anim_delay = 0.05
        gif._coreimage.anim_reset(True)
        self.but1.disabled = True
        self.cl.schedule_once(callback=lambda dt: self.sound.stop(), timeout=6)
        self.cl.schedule_once(callback=lambda dt: self.change_screen(), timeout=6)


class SecondWindow(Screen):
    sound = SoundLoader.load("button_sound.wav")


class QuestionWindow(Screen):
    correctly = False
    btn_sound = SoundLoader.load("button_sound.wav")

    def check_correct(self):
        ans_gamer = self.answer.text
        self.ans_btn.disabled = True
        # Calling func with answer in answer var
        answer = "ans"

        if self.check(answer, ans_gamer):

            self.correctly = True
            ans_sound = SoundLoader.load("correct_sound.wav")
            self.question.text = "Правильный ответ!"
        else:
            self.correctly = False
            ans_sound = SoundLoader.load("incorrect_sound.wav")
            self.question.text = "Неверно! " + "\n" + "Правильный ответ: " + "\n" + answer

        ans_sound.play()
        Clock.schedule_once(callback=lambda dt: self.change_screen(), timeout=3)

    def change_screen(self):
        self.answer.text = ''
        self.answer.hint_text = 'Введите ответ: '
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
        # Here will be question func call
        self.question.text = " Please answer the question "
        self.ans_btn.disabled = False
        # maybe will be needed to parse the string by 3 words in line (using list and /n)


class LastWin(Screen):
    sound = SoundLoader.load("end_sound.wav")

    def play_sound(self):
        self.sound.play()

    def change_screen(self):
        vol = 1

        for i in range(0, 20):
            self.sound.volume = vol
            time.sleep(0.05)
            vol -= 0.05
        self.sound.stop()


class LastLoose(Screen):
    sound = SoundLoader.load("end_sound.wav")

    def play_sound(self):
        self.sound.play()

    def change_screen(self):
        vol = 1

        for i in range(0, 20):
            self.sound.volume = vol
            time.sleep(0.05)
            vol -= 0.05
        self.sound.stop()


class Manager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MainApp(App):
    def build(self):
        self.icon = 'icon.png'
        self.title = 'What?Where?When?'
        return kv


if __name__ == "__main__":
    app = MainApp()
    app.run()
