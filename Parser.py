# define alphabet
alphabet_full = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '*', '(', ')', ' '}
alphabet_num = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
alphabet_op = {'+', '*'}
alphabet_od = {'(', ')', ' '}

tokens = []


def parsing(input):

    # check basic structure and contents of input
    validate_input(input)

    # TODO: This is for debugging.
    print("This is our stack after debugging:")
    print(tokens)





    # How to solve the calculation:
    # Order of operations:
    # () first - recursion.
    # * second
    # + last

    # return value or exception
    return 1


def validate_input(input):

    # invalid character check
    # build set of characters not in alphabet_full
    a = {c for c in input if c not in alphabet_full}
    # if set is not empty, then we have an invalid character
    if a != set():
        raise InvalidCharacterError()

    # tokenize: find sets of numbers, or individual parentheses and operators
    # while we're doing this, check for numbers next to numbers or symbols next to symbols

    position = 0
    num_length = 0
    num_end = 0
    open_paren_count = 0
    close_paren_count = 0
    previous_token_type = ''
    for c in input:

        if c in alphabet_num:
            if position < num_end:              # make sure we don't count a digit twice
                pass
            elif previous_token_type == 'NUM':  # if we're looking at a new number and we just did a number, error
                raise InvalidNeighborError
            else:                               # if new valid number
                # find end of number and pull it out
                for sub_char in input[position:]:
                    if sub_char in alphabet_num:
                        num_length += 1
                    else:
                        break
                tokens.append(int(input[position:(position+num_length)]))
                previous_token_type = 'NUM'
                num_end = position + num_length
                num_length = 0

        elif c in alphabet_op:
            if previous_token_type == 'OP':
                raise InvalidNeighborError
            tokens.append(c)
            previous_token_type = 'OP'

        elif c in alphabet_od:
            if c == '(':
                tokens.append(c)
                open_paren_count += 1
            if c == ')':
                tokens.append(c)
                close_paren_count += 1

        position += 1

    # we kept track, so now we can raise an exception if we have mismatched parentheses
    if open_paren_count != close_paren_count:
        raise ParenthesesMismatchError

    # Exceptions:
    # Missing parantheses
    # Numbers separated by space
    # Operators followed by operators


class InvalidCharacterError(Exception):
    pass


class InvalidNeighborError(Exception):
    pass


class ParenthesesMismatchError(Exception):
    pass
