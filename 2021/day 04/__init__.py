import numpy as np


def read_input():

    with open('input.txt') as f:
        lines = f.readlines()

    numbers = np.array([int(num) for num in lines[0].split(',')])

    lines = lines[1:]
    raw_cards = [lines[((6*n) + 1): 6*(n+1)] for n in range(int(len(lines)/6))]
    int_cards = [[[int(n) for n in r.strip().replace('  ', ' ').replace('\n', '').split(' ')] for r in card] for card in raw_cards]
    np_cards = [np.array(card) for card in int_cards]

    return numbers, np_cards


def part_1():
    numbers, cards = read_input()

    card_wins = []

    for i, card in enumerate(cards):
        num_rows, num_cols = card.shape

        rows = [card[n, :] for n in range(num_rows)]
        cols = [card[:, n] for n in range(num_cols)]
        diag = [card.diagonal(), np.fliplr(card).diagonal()]

        card_wins.append(rows + cols + diag)

    selections = 5
    winning_cards = 0
    n = 0

    winning_row = None
    winninc_card_id = None

    while winning_cards != 1 and n < 100:

        print(n, winning_cards, selections)

        if winning_cards == 0:
            selections += 5
        elif winning_cards > 1:
            selections -= 1

        winning_cards = 0

        selection = numbers[0:selections]

        for i, possible_wins in enumerate(card_wins):
            for j, win in enumerate(possible_wins):
                if all([n in selection for n in win]):
                    winninc_card_id = i
                    winning_row = win
                    winning_cards += 1
        n+=1

    winning_card = cards[winninc_card_id]

    total = 0

    for num in selection:
        if num in winning_card:
            total += num

    for num in selection[::-1]:
        if num in winning_row:
            winning_ball = num
            break

    print((winning_card.sum() - total)*winning_ball)


class BinarySearch:
    def __init__(self, n, start=0):
        self.n = n - start
        self.curr = start + ((n-start)/2)
        self.factor = 4

    def up(self):
        self.curr = self.curr + (self.n / self.factor)
        self.factor = 2 * self.factor
        return round(self.curr)

    def down(self):
        self.curr = self.curr - (self.n / self.factor)
        self.factor = 2 * self.factor
        return round(self.curr)


def part_2():
    numbers, cards = read_input()

    card_potential_wins = []

    for i, card in enumerate(cards):
        num_rows, num_cols = card.shape

        rows = [card[n, :] for n in range(num_rows)]
        cols = [card[:, n] for n in range(num_cols)]
        # diag = [card.diagonal(), np.fliplr(card).diagonal()]

        card_potential_wins.append(rows + cols)

    winning_cards = []
    n = 0
    length = len(cards)
    all_but_1 = length - 1
    bi = BinarySearch(length)
    selections = round(bi.curr)

    while len(winning_cards) != all_but_1 and n < 100:

        print(n, selections, len(winning_cards))

        if len(winning_cards) < all_but_1:
            selections = bi.up()
        elif len(winning_cards) > all_but_1:
            selections = bi.down()

        winning_cards = []

        selection = numbers[0:selections]

        for i, possible_wins in enumerate(card_potential_wins):
            for j, win in enumerate(possible_wins):
                if all([n in selection for n in win]):
                    winning_cards.append(i)
                    break
        n += 1

    losing_card_id = None

    for n in range(length):
        if n not in winning_cards:
            losing_card_id = n
            break

    losing_card_possible_wins = card_potential_wins[losing_card_id]
    losing_card = cards[losing_card_id]
    losing_card_solved = False

    i = selections - 1

    while losing_card_solved is False and i < length:
        i += 1

        print('i', i)
        selection = numbers[0: i]

        for j, possible_win in enumerate(losing_card_possible_wins):
            if all([n in selection for n in possible_win]):
                losing_card_solved = True
                break

    losing_card_marked_numbers = 0

    for num in numbers[0:i]:
        if num in losing_card:
            losing_card_marked_numbers += num

    print(numbers[i-1] * (losing_card.sum()-losing_card_marked_numbers))


# part_1()
part_2()
