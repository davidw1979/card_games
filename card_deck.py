import random


class Card:
    """
    Models a standard playing card
    Rank & suit --> strings 
    score --> int (calculated from rank at instantiation)
    Instance variables utilise double underscores/name mangling & getters/setters to restrict changes
    Class variables provide validity checking during instantiation
    """

    allowed_ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    allowed_suits = ("spade", "heart", "diamond", "club")

    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit
        self.score = self.rank
        self.img_file_name = suit

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"
    
    @property
    def rank(self) -> str:
        return self.__rank
    
    @rank.setter
    def rank(self, rank) -> None: 
        if rank not in Card.allowed_ranks:
            raise ValueError("Card rank is not recognised")
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    
    @suit.setter
    def suit(self, suit):
        match suit:
            case "♠" | "s" | "spade":
                self.__suit = "♠"
            case "♥" | "h" | "heart":
                self.__suit = "♥"
            case "♦" | "d" | "diamond":
                self.__suit = "♦"
            case "♣" | "c" | "club":
                self.__suit = "♣"
            case _:
                raise ValueError("Card suit is not recognised")
    
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, rank):
        if rank != self.rank:
            raise ValueError("Card score and rank do not align")
        match rank:
            case "J" | "Q" | "K":
                self.__score = 10
            case "A":
                self.__score = 11
            case _:
                self.__score = int(rank)
    
    @property
    def img_file_name(self) -> str:
        return self.__img_file_name
    
    @img_file_name.setter
    def img_file_name(self, suit) -> None:
        self.__img_file_name = f"{self.rank.lower()}_of_{suit}s.png"
    
    def __add__(self, other):
        # Uses a cards score to handle addition in form (Card + Card) or (Card + int)
        match type(other).__name__:
            case "Card":
                return self.score + other.score
            case "int":
                return self.score + other
            case _:
                raise ValueError("Incompatible data type being used for addition with Card")
    
    def __radd__(self, other):
        # Uses a cards score to handle addition in form (int + Card)
        if type(other).__name__ == "int":
            return self.score + other


class Deck:
    """
    Models a standard deck of 52 cards
    Takes optional parameter(int) at instantiation if multiple decks are required
    .shuffle() method randomly shuffles all cards in the deck
    .deal() deals single card
    len(deck) returns number of cards in deck
    Class method 'new' allows instantiation via Deck.new(int) parameter = number of decks
    """

    def __init__(self, num_of_decks=1) -> None:
        self.cards = []
        for _ in range (0, num_of_decks):
            for suit in Card.allowed_suits:
                for rank in Card.allowed_ranks:
                    self.cards.append(Card(rank, suit))
    
    @classmethod
    # Allows creation of a deck with syntax Deck.new(int)
    def new(cls, num_of_decks=1):
        return cls(num_of_decks)
    
    def __str__(self) -> str:
        # Print out all cards in deck, each on a new line
        cards = ""
        for card in self.cards:
            cards += f"{card}\n"
        return cards.rstrip("\n")

    def __len__(self):
        # Returns number of cards in the deck
        return len(self.cards)
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()


def main():
    my_deck = Deck.new()
    my_deck.shuffle()
    my_card = my_deck.deal()
    print(my_card)
    print(len(my_deck))
    print(my_card.img_file_name)
    

if __name__ == "__main__":
    main()
