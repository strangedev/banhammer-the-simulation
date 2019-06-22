#!/bin/python

from simulate import simulate, show_events
from plot import plot_ticks

import funstuffs


# score altering functions, called on event
def decay(score, dt, time):
    return -funstuffs.log_decay_factory(y_scale=0.045)(score)


def incorrectly_timed_leet(score, dt, time):
    return funstuffs.sigmoid_like_factory(decay_factor=1, y_scale=0.5)(score)


def interrupted_leet(score, dt, time):
    return funstuffs.sigmoid_like_factory(decay_factor=1, y_scale=1.5)(score)


# predicates for conditionally running events
def predicate_is_leet_time(score, dt, time):
    return time % 1440 == 817  # 13*60 + 37 == 817


def predicate_is_allowed_to_leet(score, dt, time):
	return score < 1
    

SCHEDULED_EVENTS = [
    {
        "interval": 100,  # 100 minutes
        "f": decay
    }
]


RANDOM_EVENTS = [
    {
        "p": 0.0006,  # .06% chance of event happening
        "f": incorrectly_timed_leet
    },
    {
        "p": 0.3,
        "f": interrupted_leet,
        "only_if": [
            predicate_is_leet_time,
            predicate_is_allowed_to_leet
        ]
    }
]


def main():
	ticks = simulate(50000, 1, RANDOM_EVENTS, SCHEDULED_EVENTS, 1)
	show_events(ticks)
	plot_ticks(ticks)


if __name__ == '__main__':
	main()
