from card_deck import Card
import pytest

@pytest.fixture
def ace_of_spades():
    '''Returns A♠ playing card'''
    return Card("A", "♠")

@pytest.fixture
def four_of_diamonds():
    '''Returns 4♦ playing card'''
    return Card("4", "♦")

def test_initial_rank(ace_of_spades, four_of_diamonds):
    assert ace_of_spades.rank == "A"
    assert four_of_diamonds.suit == "♦"

def test_initial_suit(four_of_diamonds):
    assert four_of_diamonds.suit == "♦"

# def test_wallet_add_cash(wallet):
#     wallet.add_cash(80)
#     assert wallet.balance == 100

# def test_wallet_spend_cash(wallet):
#     wallet.spend_cash(10)
#     assert wallet.balance == 10

# def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
#     with pytest.raises(InsufficientAmount):
#         empty_wallet.spend_cash(100)