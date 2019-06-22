import matplotlib.pyplot as plt
import numpy as np

from simulate import i_prune_ticks


def plot_ticks(ticks):
    """
    Takes a series of ticks (not pruned!) and plots them.
    """
    eventful_ticks = list(i_prune_ticks(ticks))

    def tick_contains_event(tick, event_name):
        return any([e["id"] == event_name for e in tick["events"]])

    # score vs time
    x, y = [t["time"] for t in ticks], [t["score"] for t in ticks]

    # data points for interrupted_leet event
    x_int_leet = [t["time"] for t in eventful_ticks if tick_contains_event(t, "interrupted_leet")]
    y_int_leet = [t["score"] for t in eventful_ticks if tick_contains_event(t, "interrupted_leet")]

    # data points for incorrectly_timed_leet event
    x_leet_timing = [t["time"] for t in eventful_ticks if tick_contains_event(t, "incorrectly_timed_leet")]
    y_leet_timing = [t["score"] for t in eventful_ticks if tick_contains_event(t, "incorrectly_timed_leet")]

    # data points for decay event
    x_decay = [t["time"] for t in eventful_ticks if tick_contains_event(t, "decay")]
    y_decay = [t["score"] for t in eventful_ticks if tick_contains_event(t, "decay")]

    plt.plot(x, y, c='k')
    plt.scatter(x_int_leet, y_int_leet, 33, c="r", alpha=1, marker=r'$\Delta$', label="Interrupted")
    plt.scatter(x_leet_timing, y_leet_timing, 33, c="b", alpha=1, marker=r'$\Delta$', label="Mistimed")
    plt.scatter(x_decay, y_decay, 33, c="g", alpha=0.2, marker=r'$\nabla$', label="Decay")

    plt.grid(True)
    plt.ylabel("Score")
    plt.xlabel("Time [d]")

    start, end = plt.xlim()
    xtick_count = int(end) // 1440  # one xtick per day
    plt.xticks(np.arange(0, end, 1440), range(xtick_count))

    plt.show()
