from card_deck import Card, Deck
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import StringProperty


class Hand:
    """
    Models a players Blackjack hand
    cards_held always initialized as blank list
    """
    def __init__(self, cards_held=None) -> None:
        self.cards_held = []
    
    @classmethod
    # Allows creation of a hand with syntax Hand.new()
    def new(cls):
        return cls()
    
    @property
    def cards(self) -> list:
        return self.cards_held
    
    def __add__(self, card):
        # Uses addition to append a new card to those held in the hand
        match type(card).__name__:
            case "Card":
                self.cards_held.append(card)
            case _:
                raise ValueError("Incompatible data type being added to a hand. Must be a Card")

class PlayerUI(BoxLayout):
    Window.clearcolor = (0, 81/255, 44/255)

    deal_or_hit_btn_txt = StringProperty("Deal")
    deck = Deck.new()
    deck.shuffle()
    player_hand = Hand.new()
    print(len(deck))
    
    
    def on_button_click(self):
        # If player holds 0 cards deal 2 cards otherwise hit with 1 card
        if not len(self.player_hand.cards_held):
            self.player_hand + self.deck.deal()
        self.player_hand + self.deck.deal()

        if len(self.player_hand.cards_held) > 2:
            print(f"New Card: {self.player_hand.cards_held[-1]}")
        print(f"Cards in Deck: {len(self.deck)}")

        self.ids.playerCardImage1.source = f'images/{self.player_hand.cards_held[0].img_file_name}'
        self.ids.playerCardImage2.source = f'images/{self.player_hand.cards_held[1].img_file_name}'
        
        # Change button text from deal to hit
        self.deal_or_hit_btn_txt = "Hit"


class BlackJackApp(App):
    pass


if __name__ == '__main__':
    BlackJackApp().run()