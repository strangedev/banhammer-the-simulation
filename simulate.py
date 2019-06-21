import random


def tick(random_events, scheduled_events, score: float, dt: int, t: int):
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
            for predicate in event["only_if"]:
                if predicate(score, dt, t) and random.uniform(0, 1) >= event["p"]:
                    event_function = event["f"]
                    delta_score = event_function(score, dt, t)
                    events_occurred.append({
                        "id": event_function.__name__,
                        "delta_score": delta_score
                    })
                    score += delta_score
        if score < 0:
            score = 0
        
    return score, events_occurred


def simulate(n_ticks, dt_tick, random_events, scheduled_events, bad: int):
    score = 0
    ticks = []
    for tick_count in range(n_ticks):
        score, events_occurred = tick(random_events, scheduled_events, score, dt_tick, tick_count)
        ticks.append({
            "time": tick_count,
            "score": score,
            "events": events_occurred
        })
    return ticks

def show_ticks(ticks):
    previous = None
    same_same_flag = False
    for i in range(len(ticks)):
        current = ticks[i]

        if previous:
            if previous["score"] == current["score"]:
                if not same_same_flag:
                    print("  [...]")
                same_same_flag = True
                continue
            else:
                same_same_flag = False

        previous = current
        print(current)