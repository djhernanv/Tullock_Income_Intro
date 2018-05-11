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
    form_model = models.Player
    form_fields = ['t001',
                   't002',
                   't003',
                   't004',
                   't005',
                   'output0'
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


# correct to allow for variable number of strings
# for now created with:
# for i in range(10, 46):
#    print('\'t1{}\','.format(i))


class RET(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
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
                   'output',
                   'switch1',
                   'additional_time'
                   ]

    def before_next_page(self):
        self.player.set_switch1()


class Waiting(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_incomes()


class Feedback(Page):
    pass


class HighWageInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
    #Welcome,
    #Introduction,
    TaskInstructions,
    #Round0,
    #WaitingString,
    #SwitchInstructions,
    #RET,
    #Waiting,  # calculates incomes
    #Feedback,
    HighWageInstructions,
]
