#!/bin/python

from simulate import simulate, show_ticks
from plot import plot_ticks

import funstuffs

def decay(score, dt, time):
    return -funstuffs.exp_decay(0.045)(score)

def incorrectly_timed_leet(score, dt, time):
    return funstuffs.bad_factory(1, y_scale=0.5)(score)

def interrupted_leet(score, dt, time):
    return funstuffs.bad_factory(1, y_scale=1.5)(score)

def predicate_is_leet_time(score, dt, time):
    return time % 1440 == 100
    

SCHEDULED_EVENTS = [
    {
        "interval": 100,  # 1 day
        "f": decay
    }
]

RANDOM_EVENTS = [
    {
        "p": 0.0006,  # 1% chance of event happening
        "f": incorrectly_timed_leet
    },
    {
        "p": 0.3,
        "f": interrupted_leet,
        "only_if": [
            predicate_is_leet_time
        ]
    }
]

def main():
	ticks =  simulate(50000, 1, RANDOM_EVENTS, SCHEDULED_EVENTS, 1)
	show_ticks(ticks)
	plot_ticks(ticks)

if __name__ == '__main__':
	main()
