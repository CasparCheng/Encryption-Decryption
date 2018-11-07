# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:
CONVERT_CHAR_NUM = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                    'W', 'X', 'Y', 'Z']


def clean_message(message):
    '''(str) -> str
    Given a message, the function moves move the non-letter item and changes
    the letter to the upper version. Return the message which have only the
    uppper letter of alphabet.

    >>> clean_message("abc")
    'ABC'
    >>> clean_message("cde1")
    'CDE'
    >>> clean_message("1234c")
    'C'
    >>> clean_message("ssdD")
    'SSDD'
    >>> clean_message("msdw")
    'MSDW'

    '''
    # create a empty copy message
    copy_message = ""
    for character in message:
        # check each item in the message whether they are alphabetical letter
        if(character.isalpha()):
            # if the item is alphabetical letter, it would change to uppercase
            copy_message += character.upper()

    return copy_message


def encrypt_letter(character, keystream_value):
    '''(str, int) -> str
    Given a single character and a keystream value, the function carries the
    encryption steps and uses the given keystream value to encrypt this
    character. Return the final letter after enryption.

    >>> encrypt_letter('b', 4)
    'F'
    >>> encrypt_letter('C', 6)
    'I'
    >>> encrypt_letter('Y', 5)
    'D'
    >>> encrypt_letter('N', 3)
    'Q'
    >>> encrypt_letter('z', 1)
    'A'
    '''

    # change the single character to uppercase
    upper_character = character.upper()
    # find the index of this character and add it with the keystream_value to
    # get the new index.
    idx_in_convert = CONVERT_CHAR_NUM.index(upper_character) + keystream_value
    # if the new index is greater than 25, then minus 26 from it
    if (idx_in_convert > len(CONVERT_CHAR_NUM) - 1):
        idx_in_convert = idx_in_convert - len(CONVERT_CHAR_NUM)
    # use the new index to find the final letter for encryption
    result = CONVERT_CHAR_NUM[idx_in_convert]

    return result


def decrypt_letter(upper_character, keystream_value):
    '''(str, int) -> str

    Given a single upper character and a keystream_value, the function carries
    the decryption steps which is the reverse version of encryption steps and
    uses the keystream value to decrypt this letter. Return the final letter
    after decryption.

    >>> decrypt_letter('C', 3)
    'Z'
    >>> decrypt_letter('N', 5)
    'I'
    >>> decrypt_letter('A', 2)
    'Y'
    >>> decrypt_letter('G', 1)
    'F'
    >>> decrypt_letter('Z', 27)
    'Y'
    '''

    # find the index of upper character then substract the keystream value to
    # get the new index
    idx_in_convert = CONVERT_CHAR_NUM.index(upper_character) - keystream_value
    # if the new index is less than 0, then plus 26
    if (idx_in_convert < 0):
        idx_in_convert = idx_in_convert + len(CONVERT_CHAR_NUM)
    # get the final letter from decryption through new index
    result = CONVERT_CHAR_NUM[idx_in_convert]

    return result


def swap_cards(deck_cards, idx):
    '''(list of int, int) -> NoneType
    Given a deck of cards and an index of the deck, the function exchange the
    card of that index with the followed one. If the index is the bottom one
    of this deck, then swap the card with the top card.

    REQ: treat the deck as circular

    >>> swap_cards([1, 2, 3, 4, 5, 6, 7], 3)
    [1, 2, 3, 5, 4, 6, 7]
    >>> swap_cards([2, 3, 4, 9, 1, 6, 5, 8], 2)
    [2, 3, 9, 4, 1, 6, 5, 8]
    >>> swap_cards([3, 4, 1, 6, 2, 5], 5)
    [5, 4, 1, 6, 2, 3]
    >>> swap_cards([6, 7, 8, 2, 1], 4)
    [1, 7, 8, 2, 6]
    >>> swap_cards([4, 5, 7, 8, 1, 3, 6], 1)
    [4, 7, 5, 8, 1, 3, 6]
    '''

    # if the card of the index is the bottom, then swap it with the top card
    # in the deck
    if (idx + 1 == len(deck_cards)):
        deck_cards[0], deck_cards[idx] = deck_cards[idx],\
                                deck_cards[0]
    # find the card of given index and swap it with the followig one.
    else:
        deck_cards[idx], deck_cards[idx + 1] = deck_cards[idx + 1],\
                deck_cards[idx]


def move_joker_1(deck_cards):
    '''(list of int) -> NoneType
    Given a deck of cards, find the joker1, then exchange its position
    with the following card. The deck will be treated as circular.

    REQ: the deck should include joker1
    REQ: treat the deck as circular

    >>> move_joker_1([1, 2, 3, 27, 5, 6, 28])
    [1, 2, 3, 5, 27, 6, 28]
    >>> move_joker_1([5, 7, 28, 11, 22, 27, 21])
    [5, 7, 28, 11, 22, 21, 27]
    >>> move_joker_1([2, 3, 4, 10, 22, 14, 27])
    [27, 3, 4, 10, 22, 14, 2]
    >>> move_joker_1([22, 23, 25, 27, 28, 25])
    [22, 23, 25, 28, 27, 25]
    >>> move_joker_1([15, 26, 14, 25, 27])
    [27, 26, 14, 25, 15]
    '''

    # find the index of joker1
    joker1_idx = deck_cards.index(JOKER1)
    # swap joker1 with following card
    swap_cards(deck_cards, joker1_idx)


def move_joker_2(deck_cards):
    '''(list of int) -> NoneType
    Given a deck of cards, the function finds the joker2, then moves it
    two cards down. the deck will be treated as circular.

    REQ: the deck should include joker2
    REQ: treat the deck as circular

    >>> move_joker_2([1, 2, 3, 4, 5, 6, 7, 28, 10, 11, 12])
    [1, 2, 3, 4, 5, 6, 7, 10, 11, 28, 12]
    >>> move_joker_2([3, 4, 6, 11, 22, 28, 27, 20, 14])
    [3, 4, 6, 11, 22, 27, 20, 28, 14]
    >>> move_joker_2([12, 15, 16, 17, 28])
    [15, 28, 16, 17, 12]
    >>> move_joker_2([17, 18, 19, 28, 20])
    [28, 18, 19, 20, 17]
    >>> move_joker_2([20, 26, 16, 28, 11, 13])
    [20, 26, 16, 11, 13, 28]
    '''

    # find the index of joker2
    joker2_idx = deck_cards.index(JOKER2)
    # swap joker2 with following card
    swap_cards(deck_cards, joker2_idx)
    # find the index of joker2
    joker2_idx = deck_cards.index(JOKER2)
    # swap joker2 with the following card
    swap_cards(deck_cards, joker2_idx)


def triple_cut(deck_cards):
    '''(list of int) -> NoneType
    Given a deck of cards, the function does the triple cut that means find
    the first index of joker then swap the cards above this joker with the
    cards below the second joker

    REQ: the deck of cards should include joker1 and joker2

    >>> triple_cut([1, 2, 4, 5, 27, 6, 7, 8, 28, 9, 10])
    [9, 10, 27, 6, 7, 8, 28, 1, 2, 4, 5]
    >>> triple_cut([2, 4, 5, 6, 27, 28, 11, 12, 13])
    [11, 12, 13, 27, 28, 2, 4, 5, 6]
    >>> triple_cut([10, 22, 23, 27, 24, 26, 11, 28])
    [27, 24, 26, 11, 28, 10, 22, 23]
    >>> triple_cut([3, 4, 6, 10, 9, 7, 27, 28])
    [27, 28, 3, 4, 6, 10, 9, 7]
    >>> triple_cut([28, 1, 2, 3, 5, 6, 7, 8, 27])
    [28, 1, 2, 3, 5, 6, 7, 8, 27]
    '''

    # find indexs of joker1 and joker2,respectively
    joker1_idx = deck_cards.index(JOKER1)
    joker2_idx = deck_cards.index(JOKER2)
    # if the index of joker1 is greater than the index of joker2
    if (joker1_idx > joker2_idx):
        # swap the below cards of joker1 with the above cards of joker2
        deck_cards = deck_cards[joker1_idx+1:] + \
                      deck_cards[joker2_idx:joker1_idx+1] + \
                      deck_cards[:joker2_idx]

    # else, swap the below cards of joker2 with the above cards of joker1
    else:
        deck_cards = deck_cards[joker2_idx+1:] + \
            deck_cards[joker1_idx:joker2_idx+1] + deck_cards[:joker1_idx]


def insert_top_to_bottom(deck_cards):
    '''(list of int) -> NoneType
    Given a deck of cards, the fucntion finds the bottom card, and uses the
    value of this card to get the number of value cards from top of the deck
    to the bottom of the deck, then inserting these cards above the bottom
    deck. If the bottom card is joker2, then use the value of joker1 to
    replace it.

    >>> insert_top_to_bottom([1, 2, 4, 5, 6, 27, 28, 3])
    [5, 6, 27, 28, 1, 2, 4, 3]
    >>> insert_top_to_bottom([2, 4, 3, 10, 8, 27, 28, 6, 1])
    [4, 3, 10, 8, 27, 28, 6, 2, 1]
    >>> insert_top_to_bottom([1, 2, 3, 5, 8, 27, 28, 4])
    [8, 27, 28, 1, 2, 3, 5, 4]
    >>> insert_top_to_bottom([2, 28, 27, 3])
    [2, 28, 27, 3]
    >>> insert_top_to_bottom([5, 27, 9, 28, 10, 2])
    [9, 28, 10, 5, 27, 2]
    '''

    # find the indexs of joker1 and joker2, respectively
    joker1_idx = deck_cards.index(JOKER1)
    joker2_idx = deck_cards.index(JOKER2)
    # find the index of the bottom card in the deck
    bottom_idx = len(deck_cards) - 1
    # if joker2 is the bottom card in the deck
    if (bottom_idx == joker2_idx):
        # the value of joker2 is replaced by the value of joker1
        v = JOKER1
        # use the joker1 value to get the number of cards from top of the deck
        v_top_cards = deck_cards[:v]
        # get the cards between the bottom card and the number of cards from
        # top to value number
        between_v_bottom = deck_cards[v:bottom_idx]
        # inserting the value number of cards above the bottom card of the deck
        deck_cards = between_v_bottom + v_top_cards + \
            deck_cards[bottom_idx:]
    else:
        # get the bottom card
        v = deck_cards[bottom_idx]
        # use the value of bottom card to get the number of cards from top
        # of the deck
        v_top_cards = deck_cards[:v]
        # get the cards between the bottom card and the number of cards from
        # top to value number
        between_v_bottom = deck_cards[v:bottom_idx]
        # inserting the value number of cards above the bottom card of the deck
        deck_cards = between_v_bottom + v_top_cards + deck_cards[bottom_idx:]


def get_card_at_top_index(deck_cards):
    '''(list of int) -> int
    Given a deck of cards, the function uses the value of the top card of
    the deck as index to find the card whose position is that index. Return
    the card.

    REQ: joker2 should be treated as joker1

    >>> get_card_at_top_index([4, 2, 3, 5, 6, 7, 8])
    6
    >>> get_card_at_top_index([5, 2, 4, 6, 27, 23, 26, 28, 27])
    23
    >>> get_card_at_top_index([1, 2, 4, 5, 7])
    2
    >>> get_card_at_top_index([3, 4, 6, 10])
    10
    >>> get_card_at_top_index([2, 5, 7, 10, 12, 20])
    7
    '''

    # if the top card of the deck is joker2
    if (deck_cards[0] == JOKER2):
        # then using the value of joker1 to replace it
        # get the keystream value at that poistion
        keystream_value = deck_cards[JOKER1]

    else:
        # get the top card of the deck
        top_card_idx = deck_cards[0]
        # using the value of the top card as index to get the keystream value
        keystream_value = deck_cards[top_card_idx]

    return keystream_value


def get_next_value(deck_cards):
    '''(list of int) -> int
    Given a deck of card, the function does the previous 5 steps to get the
    keystream value. Return the potential keystream value

    >>> get_next_value([1, 2, 3, 4, 5, 28, 7, 8, 10, 27, 12])
    27
    >>> get_next_value([3, 4, 5, 1, 27, 28, 10, 6, 9, 11, 12])
    6
    >>> get_next_value([27, 2, 4, 5, 28, 9, 11, 6, 3, 1, 8, 7, 10])
    8
    >>> get_next_value([10, 3, 8, 7, 5, 27, 6, 28, 5, 4])
    3
    >>> get_next_value([28, 1, 3, 9, 10, 7, 6, 11, 5, 4, 27])
    7
    '''

    # do the step 1, find the joker1 then swap it with following card
    move_joker_1(deck_cards)
    # do the step 2, find the joker2 then move it two cards down
    move_joker_2(deck_cards)
    # do the step 3, carry on the triple cut
    triple_cut(deck_cards)
    # do the step 4, insert the number of cards which are from the top of
    # the deck through using value of the bottom card to above bottom card
    insert_top_to_bottom(deck_cards)
    # do the step 5, using the value of top card of the deck as index
    # find the card at that position, then it is potential keystream value
    potential_keystream_value = get_card_at_top_index(deck_cards)

    return potential_keystream_value


def get_next_keystream_value(deck_cards):
    '''(list of int) -> int
    Given a deck of cards, the function do the previous 5 steps repeatedly.
    If the keystream value is not in range 1-26, then do the 5 steps again.

    >>> get_next_keystream_value([1, 2, 3, 4, 5, 28, 7, 8, 10, 27, 12, 6, 9])
    7
    >>> get_next_keystream_value([3, 4, 5, 1, 27, 28, 10, 6, 9, 11, 12])
    6
    >>> get_next_keystream_value([10, 3, 8, 7, 5, 27, 6, 28, 5, 4])
    3
    >>> get_next_keystream_value([27, 2, 4, 5, 28, 9, 11, 6, 3, 1, 8, 7, 10])
    8
    >>> get_next_keystream_value([28, 1, 3, 9, 10, 7, 6, 11, 5, 4, 27])
    7
    '''

    # do the 5 steps get the potential keystream value
    potential_keystream_value = get_next_value(deck_cards)
    # when the potential keystream value is not in the range 1-26
    while (potential_keystream_value not in range(1, 27)):
        # carry on the 5 steps again until it is a valid value
        potential_keystream_value = get_next_value(deck_cards)

    valid_keystream_value = potential_keystream_value

    return valid_keystream_value


def process_message(deck_cards, message, e_d):
    '''(list of int, str, str) -> str
    Given a deck of cards, a message and a type(encryption or decryption).
    The function encrpts or decrypts the message. Return the messsage which
    has been enrypted or descryted.

    >>> deck_cards = [1, 2, 3, 4, 5, 6, 28, 7, 8, 9, 10, 11, 13, 14, 15, 16]
    >>> deck_cards += [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 12]
    >>> process_message(deck_cards, 'Welcome', 'e')
    'CBQPRJX'
    >>> deck_cards = [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]
    >>> deck_cards += [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> process_message(deck_cards, 'EQFZVNZVZTRVPAHTKZFJCXXANYSASXQ', 'd')
    'EQGBYREBGBAFAMGQFSNQICBDPZRZRXP'
    >>> deck_cards = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 2, 4]
    >>> deck_cards += [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    >>> process_message(deck_cards, 'Thanks', 'e')
    'ZSVWOJ'
    >>> process_message([1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, \
    17, 20, 23, 26, 4, 7, 10, 13, 16, 19, 22, 25, 28], 'lovelive', 'e')
    'DDHZFWKP'
    >>> process_message([7, 6, 5, 4, 3, 2, 1, 14, 13, 12, 11, 10, 9, 8, 21, \
    20, 19, 18, 17, 16, 15, 27, 26, 25, 24, 23, 22, 28], 'NARUTO', 'd')
    'ZWHHMZ'
    '''

    # create an empty string
    result_message = ""
    # change the message to the uppercase
    upper_message = clean_message(message)
    # if the type is encryption
    if (e_d == 'e'):
        # get every character in this message after changing upper version
        for char in upper_message:
            # do the 5 steps to get the valid keystream value
            valid_keystream_value = get_next_keystream_value(deck_cards)
            # use the getting keystream value to encrypt this letter
            e_char = encrypt_letter(char, valid_keystream_value)
            # add the encryting letter into the empty string
            result_message += e_char
    # if the type is decryption
    elif (e_d == 'd'):
        # get every characther in this message after changing upper version
        for char in upper_message:
            # do the 5 steps to get the valid keystream value
            valid_keystream_value = get_next_keystream_value(deck_cards)
            # use the getting keystream value to decrypt this letter
            d_char = decrypt_letter(char, valid_keystream_value)
            # add the decrypting letter into the empty string
            result_message += d_char

    return result_message


def process_messages(deck_cards, messages_list, e_d):
    '''(list of int, list of str, str)
    Given a deck of cards, a list of messages and a type(encryption or
    decryption), the function encrypts or decryts every message in the list.
    Return the list of messages which has been encrypted or descrypted.

    >>> process_messages([1, 2, 3, 4, 5, 6, 28, 7, 8, 9, 10, 11, 13, \
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 12], ['fullmark', \
    'please', 'cry'], 'e')
    ['LRQYPXKN', 'QIMFLD', 'PGL']
    >>> process_messages([28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, \
    15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], ['utoronto', 'best', \
    'university'], 'e')
    ['UTNPLJOI', 'UWJJ', 'JBJYJYKBNT']
    >>> process_messages([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, \
    2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28], ['ALLIENWARE'], 'd')
    ['UAQZAWQQVJ']
    >>> deck_cards = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17]
    >>> deck_cards = [20, 23, 26, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    >>> process_messages(deck_cards, ['caspar', 'handsome'], 'e')
    ['UPEKUF', 'WLEDDZPY']
    >>> process_messages([7, 6, 5, 4, 3, 2, 1, 14, 13, 12, 11, 10, 9, 8, 21, \
    20, 19, 18, 17, 16, 15, 27, 26, 25, 24, 23, 22, 28], ['KYLE', 'STUPID'], \
    'd')
    ['WUBR', 'LEHATO']
    '''

    # create a empty list
    result_messages_list = []
    # get every string message in this list
    for message in messages_list:
        # process the message according to the type
        message = process_message(deck_cards, message, e_d)
        # change the messsage which has been encrypted or decrypted into a list
        result_message_list = message.split()
        # combine the list with previous empty list
        result_messages_list += result_message_list

    return result_messages_list


def read_messages(message_file):
    '''(io.TextIOWrapper) -> list of str
    Given an open file for reading, the function reads the all contents of
    the file and strip the newline from each line.
    Return the list of messages
    '''

    # create an empty list
    result_list_message = []
    # read the line of this file
    line = message_file.readline()
    # when the line is not empty
    while (line != ""):
        # let this line be a list
        list_message = line.splitlines()
        # add this list to the empty list as element
        result_list_message += list_message
        # read next line
        line = message_file.readline()

    return result_list_message


def read_deck(deck_file):
    '''(io.TextIOWrapper) -> list of int
    Given an open file for reading, the function reads the all contents
    which are the numbers among 1 and 28 in some order.
    Return the all integers as list
    '''

    # create an empty list
    list_deck_num = []
    # read the line of this file
    line = deck_file.readline()
    # when the line is not empty
    while (line != ""):
        # let the each string of number of this line be a list
        list_str_num = line.split()
        # change the each single string to the integer
        list_int_num = [int(i) for i in list_str_num]
        # add the list to the empty list as element
        list_deck_num += list_int_num
        # read next line
        line = deck_file.readline()

    return list_deck_num
