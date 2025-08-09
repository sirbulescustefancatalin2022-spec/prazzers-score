
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window

# Dark theme
Window.clearcolor = (0.05, 0.05, 0.05, 1)

class Player(BoxLayout):
    name = StringProperty("Jucător")
    score = NumericProperty(501)
    image_path = StringProperty("")

class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)
        header = Label(text='[b]Prazzers Darts Club[/b]\n501 (demo instalabil)',
                       markup=True, size_hint_y=None, height=80)
        self.add_widget(header)

        # Two players (demo)
        self.p1 = Player(); self.p1.name = "Jucător 1"
        self.p2 = Player(); self.p2.name = "Jucător 2"

        row = BoxLayout(size_hint_y=None, height=200, spacing=10)
        row.add_widget(self._player_card(self.p1))
        row.add_widget(self._player_card(self.p2))
        self.add_widget(row)

        # Score input
        input_row = BoxLayout(size_hint_y=None, height=60, spacing=10)
        self.score_input = TextInput(hint_text="Scor aruncare (ex: 60)", input_filter="int", multiline=False)
        input_row.add_widget(self.score_input)
        input_row.add_widget(Button(text="Aplică P1", on_release=lambda *_: self.apply_score(self.p1)))
        input_row.add_widget(Button(text="Aplică P2", on_release=lambda *_: self.apply_score(self.p2)))
        input_row.add_widget(Button(text="Reset", on_release=lambda *_: self.reset_scores()))
        self.add_widget(input_row)

        self.info = Label(text="[i]Demo rapid. În build-ul următor adăugăm: Cricket, 6 jucători, echipe, undo, medii, clasament.[/i]",
                          markup=True)
        self.add_widget(self.info)

    def _player_card(self, player):
        card = BoxLayout(orientation='vertical', padding=10, spacing=6)
        name = Label(text=player.name, size_hint_y=None, height=30)
        score_lbl = Label(text=str(player.score), size_hint_y=None, height=40)

        def upd(*_): score_lbl.text = str(player.score)
        player.bind(score=lambda *_: upd())
        upd()

        img = Image(source=player.image_path or "", size_hint_y=None, height=90)

        def pick_image(*_):
            chooser = FileChooserIconView(filters=['*.png','*.jpg','*.jpeg'])
            def select(*__):
                if chooser.selection:
                    player.image_path = chooser.selection[0]
                    img.source = player.image_path
                    popup.dismiss()
            btns = BoxLayout(size_hint_y=None, height=50, spacing=10)
            btns.add_widget(Button(text="Alege", on_release=select))
            btns.add_widget(Button(text="Renunță", on_release=lambda *_: popup.dismiss()))
            box = BoxLayout(orientation='vertical')
            box.add_widget(chooser); box.add_widget(btns)
            popup = Popup(title="Alege imagine jucător", content=box, size_hint=(0.95,0.95))
            popup.open()

        card.add_widget(name)
        card.add_widget(score_lbl)
        card.add_widget(img)
        card.add_widget(Button(text="Imagine jucător", on_release=pick_image, size_hint_y=None, height=40))
        return card

    def apply_score(self, player):
        try:
            val = int(self.score_input.text or "0")
        except ValueError:
            val = 0
        if val <= 0:
            self.info.text = "[color=ff4444]Scor invalid[/color]"; return
        new_score = player.score - val
        if new_score < 0:
            self.info.text = "[color=ffbb33]Bust![/color]"; return
        player.score = new_score
        if player.score == 0:
            self.info.text = f"[b][color=44ff44]{player.name} a câștigat![/color][/b]"
        else:
            self.info.text = f"{player.name}: {player.score} rămase."
        self.score_input.text = ""

    def reset_scores(self):
        self.p1.score = 501; self.p2.score = 501
        self.info.text = "Scor resetat."

class PrazzersScoreApp(App):
    def build(self):
        return Root()

if __name__ == "__main__":
    PrazzersScoreApp().run()
