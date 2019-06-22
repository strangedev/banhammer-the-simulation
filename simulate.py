import random


def tick(random_events, scheduled_events, score, dt, t):
    """
    Simulate a single tick.

    Arguments:
        random_events: list of events that may happen randomly every tick
        scheduled_events: list of reoccuring events
        score: score previous to the tick
        dt: how long the tick is (timewise)
        t: time elapsed before the tick

    Returns:
        Tuple:
            - The new score
            - List of events that occurred in the tick
    """
    events_occurred = []

    for job in scheduled_events:  # run scheduled jobs
        if t % job["interval"] == 0:
            event_function = job["f"]
            delta_score = event_function(score, dt, t)
            events_occurred.append({
                "id": event_function.__name__,
                "delta_score": delta_score
            })
            score += delta_score

    for event in random_events:  # run random events
        if "only_if" in event:
            if not all(pred(score, dt, t) for pred in event["only_if"]):
                continue

        if random.uniform(0, 1) <= event["p"]:
            event_function = event["f"]
            delta_score = event_function(score, dt, t)
            events_occurred.append({
                "id": event_function.__name__,
                "delta_score": delta_score
            })
            score += delta_score

        if score < 0:  # no positive karma, only punishments :(
            score = 0

    return score, events_occurred


def simulate(n_ticks, dt_tick, random_events, scheduled_events, bad):
    """
    Simulate n_ticks steps.

    Arguments:
        n_ticks: number of ticks to simulate
        dt_tick: how long one tick is (timewise)
        random_events: list of events that may happen randomly every tick
        scheduled_events: list of reoccuring events
        bad: score threshold for penalties

    Returns:
        a list of all ticks simulated.
    """
    score = 0
    ticks = []
    for tick_count in range(n_ticks):
        time_passed = dt_tick * tick_count
        score, events_occurred = tick(
            random_events,
            scheduled_events,
            score,
            dt_tick,
            time_passed
        )
        ticks.append({
            "time": tick_count,
            "score": score,
            "events": events_occurred
        })
    return ticks


def i_prune_ticks(ticks):
    """
    Generator yielding only those ticks, which have events in them.
    """
    previous = None
    for i in range(len(ticks)):
        current = ticks[i]

        if previous:
            if previous["score"] == current["score"]:
                continue

        previous = current
        yield current


def show_events(ticks):
    """
    Print those ticks which have events in them.
    """
    for tick in i_prune_ticks(ticks):
        print(tick)
