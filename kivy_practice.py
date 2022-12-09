from card_deck import Card, Deck
from kivy.app import App

# The Image widget is used to display an image
# # this module contain all features of images
from kivy.uix.image import Image
#   
# # The Widget class is the base class required for creating Widgets
from kivy.uix.widget import Widget
#   
# # to change the kivy default settings we use this module config
from kivy.config import Config
#    
# # 0 being off 1 being on as in true / false
# # you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)

class MyApp(App):
    def build(self):
        my_deck = Deck.new()
        my_deck.shuffle()
        my_card = my_deck.deal()

        # return Label(text="Hello World", font_size=72)
        self.img = Image(source = f"images/{my_card.img_file_name}")

        # By default, the image is centered and fits
        # inside the widget bounding box.
        # If you don’t want that,
        # you can set allow_stretch to
        # True and keep_ratio to False.
        self.img.allow_stretch = True
        self.img.keep_ratio = True

        # Providing Size to the image
        # it varies from 0 to 1
        self.img.size_hint_x = 1
        self.img.size_hint_y = 1

        # Position set
        self.img.pos = (200, 100)

        # Opacity adjust the fadeness of the image if
        # 0 then it is complete black
        # 1 then original
        # it varies from 0 to 1
        self.img.opacity = 1

        # adding image to widget
        s = Widget()
        s.add_widget(self.img)

        # return widget
        return s


if __name__ == "__main__":
    MyApp().run()
