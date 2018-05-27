from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

import numpy as np
import string

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

doc = """
Real Effort Task - Letter Count
This is the introduction to a Tullock Contest in form of a Real Effort Task
It welcomes the participants and helps them trough the first stages
"""


# This page does not have a next button and has to be advanced manually.
# It makes sure, that all participants have roughly the same time for the instructions
class Welcome(Page):
    def is_displayed(self):
        return self.round_number == 1


# This pages is a rough introduction without instructions
class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class TaskInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Round0(Page):
    form_model = 'player'
    form_fields = ['t001',
                   't002',
                   't003',
                   't004',
                   't005',
                   'output_trial'
                   ]

    def is_displayed(self):
        return self.round_number == 1


class WaitingString(WaitPage):
    def after_all_players_arrive(self):
        # Make Sure the generating seed depends on the round or session
        string_list = []  # this will be the list of strings to be used
        for n in range(10, 200,
                       Constants.increase_per_string):  # where "a" is the smallest and "b-1" the largest possible string.
            # For now with an increment of "c"
            character_list = string.ascii_lowercase  # where the random sample for the strings will be drawn
            np.random.seed(
                113 + n + self.round_number)  # on every turn of the loop a new character list will be created
            character_list += "a" * np.random.randint(15, 30)  # this gives, in average one "a" for each letter
            np.random.seed(114 + n + self.round_number)  # to ensure reproducibility
            #  of the alphabet s.t. the relationship is 2:1 but still allows for enough variability
            string_list.append("".join(np.random.choice(list(character_list), size=n)))
        self.session.vars['string_list'] = string_list
        # count solutions
        a_count = []
        for i in range(len(string_list)):
            a_count.append(string_list[i].count("a"))
        self.session.vars['a_count'] = a_count


class SwitchInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class ControlInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['solution_1',
                   'solution_2',
                   'solution_3',
                   'solution_4',
                   'solution_5',
                   ]

    def error_message(self, values):
        print('values is', values)
        if values["solution_1"] != 15 or values["solution_2"] != 6 \
                or values["solution_3"] != 17 or values["solution_4"] != 11 or values["solution_5"] != 3:
            return 'Check your answers and try again'


class StartSubmit(Page):
    pass


# correct to allow for variable number of strings
# for now created with:
# for i in range(10, 46):
#    print('\'t1{}\','.format(i))

class RET(Page):
    timeout_seconds = Constants.t
    form_model = 'player'
    form_fields = ['t101',
                   't102',
                   't103',
                   't104',
                   't105',
                   't106',
                   't107',
                   't108',
                   't109',
                   't110',
                   't111',
                   't112',
                   't113',
                   't114',
                   't115',
                   't116',
                   't117',
                   't118',
                   't119',
                   't120',
                   't121',
                   't122',
                   't123',
                   't124',
                   't125',
                   't126',
                   't127',
                   't128',
                   't129',
                   't130',
                   't131',
                   't132',
                   't133',
                   't134',
                   't135',
                   't136',
                   't137',
                   't138',
                   't139',
                   't140',
                   't141',
                   't142',
                   't143',
                   't144',
                   't145',
                   'production_strings',
                   'switch1',
                   'additional_time'
                   ]

    def before_next_page(self):
        self.player.set_switch1()


class Waiting(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_incomes()


class Feedback(Page):

    def vars_for_template(self):
        if self.round_number > 1:
            return {'production_strings_last': self.player.in_round(self.round_number - 1).production_strings,
                    'income_strings_last': self.player.in_round(self.round_number - 1).income_strings,
                    'time_in_switch_last': self.player.in_round(self.round_number - 1).time_in_switch,
                    'income_in_switch_last': self.player.in_round(self.round_number - 1).income_in_switch,
                    'income_last': self.player.in_round(self.round_number - 1).income}


class HighWageInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class ControlInstructionsHigh(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['solution_6',
                   'solution_7',
                   'solution_8',
                   'solution_9',
                   'solution_10',
                   ]

    def error_message(self, values):
        print('values is', values)
        if values["solution_6"] != 48 or values["solution_7"] != 4 \
                or values["solution_8"] != 19 or values["solution_9"] != 12 or values["solution_10"] != 9:
            return 'Check your answers and try again'


page_sequence = [
    Welcome,
    Introduction,
    TaskInstructions,
    Round0,
    WaitingString,
    SwitchInstructions,
    ControlInstructions,
    StartSubmit,
    RET,
    Waiting,  # calculates incomes
    Feedback,
    HighWageInstructions,
    ControlInstructionsHigh,
]
