#!/bin/python

from simulate import simulate, show_ticks

def decay(score, dt, time):
    return -1

def incorrectly_timed_leet(score, dt, time):
    return 1

def interrupted_leet(score, dt, time):
    return 1

def predicate_is_leet_time(score, dt, time):
    return time % 1440 == 100
    

SCHEDULED_EVENTS = [
    {
        "interval": 1440,  # 1 day
        "f": decay
    }
]

RANDOM_EVENTS = [
    {
        "p": 0.01,  # 1% chance of event happening
        "f": incorrectly_timed_leet
    },
    {
        "p": 0.05,
        "f": interrupted_leet,
        "only_if": [
            predicate_is_leet_time
        ]
    }
]

def main():
	ticks =  simulate(2000, 1, RANDOM_EVENTS, SCHEDULED_EVENTS, 1)
	show_ticks(ticks)

if __name__ == '__main__':
	main()
