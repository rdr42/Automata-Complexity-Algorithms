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
    print("This is our stack after tokenizing:")
    print(tokens)

    result = evaluate(tokens)

    # return value or exception
    return result


def evaluate(expression):
    # Evaluation strategy:
    # Recurse on (
    # Solve in order of ops: (, *, +
    # replace relevant portions of the expression as we simplify

    # first pass: resolve parentheses
    cur_term = 0
    start_paren = -1
    end_paren = -1
    paren_depth = 0
    for term in expression[:]:
        if term == '(':
            if paren_depth == 0:
                start_paren = cur_term
            paren_depth += 1
        elif term == ')':
            # try to find end of parenthetical portion
            # if we find a ')' at depth = 1 then we've closed our parentheses
            if paren_depth == 1:
                end_paren = cur_term
                # recursion!
                newterm = evaluate(expression[(start_paren + 1):end_paren])
                del expression[start_paren:(end_paren + 1)]
                expression.insert(start_paren, newterm)
                cur_term -= (end_paren - start_paren)
            paren_depth -= 1

            # recurse to subterms
            # replace parenthetical with result

        cur_term += 1
    print(expression)

    # second pass: do multiplication
    cur_term = 0
    for term in expression[:]:  # slice copy of expression because Python is Python
        if term == '*':
            # do the multiplication
            newterm = expression[cur_term - 1] * expression[cur_term + 1]
            # remove the terms and replace with the result
            del expression[(cur_term - 1):(cur_term + 2)]
            expression.insert((cur_term - 1), newterm)
            cur_term -= 1
        else:
            cur_term += 1
        print(expression)

    # third pass: do addition
    cur_term = 0
    for term in expression[:]:  # slice copy of expression because Python is Python
        if term == '+':
            # do the addition
            newterm = expression[cur_term - 1] + expression[cur_term + 1]
            # remove the terms and replace with the result
            del expression[(cur_term - 1):(cur_term + 2)]
            expression.insert((cur_term - 1), newterm)
            cur_term -= 1
        else:
            cur_term += 1
        print(expression)

    # should be down to a single term now
    return expression[0]


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
    # setting this to OP enforces that we get NUM, OP, NUM inputs
    previous_token_type = 'OP'
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

    # one last check that we don't have a trailing operator with no value
    if previous_token_type == 'OP':
        raise InvalidNeighborError

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
