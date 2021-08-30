from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, style_from_dict, Token, Separator
from pprint import pprint
from lotto.lotto_bet import Bet
from lotto.lotto_city import City
from lotto.lotto_numbers import NumbersForTicket


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def select_bet():
    questions = [
        {
            'type': 'list',
            'name': 'bet',
            'message': 'select BET type',
            'choices': Bet.get_bets()
        }
    ]
    answer = prompt(questions)
    # print_json(answers)  # use the answers as input for your app
    return answer["bet"]


def select_city():
    questions = [
        {
            'type': 'list',
            'name': 'city',
            'message': 'select CITY (aka "ruota")',
            'choices': City.get_cities()
        }
    ]
    answer = prompt(questions)
    return answer["city"]


def select_amount(bet):
    questions = [
        {
            'type': 'list',
            'name': 'amount',
            'message': 'How many numbers ?',
            'choices': NumbersForTicket.get_allowed_amounts(bet)
        }
    ]
    answer = prompt(questions)
    return answer["amount"]


def confirm_numbers(options):
    questions = [
        {
            'type': 'list',
            'name': 'confirm_numbers',
            'message': 'Would you like to confirm the above numbers ?',
            'choices': options
        }
    ]
    answer = prompt(questions)
    return answer["confirm_numbers"]


def confirm_ticket(options, ticket_number):
    questions = [
        {
            'type': 'list',
            'name': 'confirm_ticket',
            'message': f'Would you like to confirm ticket {ticket_number} ?',
            'choices': options
        }
    ]
    answer = prompt(questions)
    return answer["confirm_ticket"]