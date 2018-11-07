"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message-decrypted.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    """
    # open the file of deck
    deck_file = open(DECK_FILENAME, "r")
    # get the deck of cards
    deck_cards = cipher_functions.read_deck(deck_file)
    # open the file of messages
    msg_file = open(MSG_FILENAME, "r")
    # get the list of messages
    messages_list = cipher_functions.read_messages(msg_file)
    # gets the new list of messages
    n_messages_list = cipher_functions.process_messages(deck_cards, \
                                                        messages_list, MODE)
    # print the new messages per line
    for message in n_messages_list:
        print(message)
                                                        
main()
# print(main())