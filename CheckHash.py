from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import hashlib
import pyperclip

class sfondo(Widget):
    lab = ObjectProperty(None)
    but = ObjectProperty(None)
    def md5(self, fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    def _on_file_drop(self, window, file_path):
        result=self.md5(file_path.decode("utf-8"))
        self.lab = result
        print(result)
        return
    def start(self):
        Window.bind(on_dropfile=self._on_file_drop)
        self.lab = "Drag a file here"
        return
    def copy(self):
        pyperclip.copy(self.lab)

class CheckHashApp(App):
    def build(self):
        sf = sfondo()
        Window.size = (600, 100)
        sf.start()
        return sf

if __name__ == '__main__':
    CheckHashApp().run()
