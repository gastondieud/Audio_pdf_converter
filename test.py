import kivy
from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.11.1')

class VideoPlayer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.video = Video(source='my_video.mp4', state='play')
        self.add_widget(self.video)

class MyApp(App):
    def build(self):
        return VideoPlayer()

if __name__ == '__main__':
    MyApp().run()





