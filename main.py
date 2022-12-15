from card_deck import Card, Deck
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.properties import StringProperty


class WidgetExample(GridLayout):
    my_deck = Deck.new()
    my_deck.shuffle()
    my_card = my_deck.deal()
    my_text = StringProperty(str(my_card))
    def on_button_click(self):
        self.my_card = self.my_deck.deal()
        print(self.my_card)
        print(f'images/{self.my_card.img_file_name}')
        self.ids.playerCardImage.source = f'images/{self.my_card.img_file_name}'
        

class PracticeApp(App):
    pass


if __name__ == '__main__':
    PracticeApp().run()