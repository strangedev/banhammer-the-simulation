import matplotlib.pyplot as plt
import numpy as np

from simulate import prune_ticks

def plot_ticks(ticks):
	x, y = [t["time"] for t in ticks], [t["score"] for t in ticks]
	x_int_leet = [t["time"] for t in prune_ticks(ticks) if any([e["id"] == "interrupted_leet" for e in t["events"]])]
	y_int_leet = [t["score"] for t in prune_ticks(ticks) if any([e["id"] == "interrupted_leet" for e in t["events"]])]
	x_leet_timing = [t["time"] for t in prune_ticks(ticks) if any([e["id"] == "incorrectly_timed_leet" for e in t["events"]])]
	y_leet_timing = [t["score"] for t in prune_ticks(ticks) if any([e["id"] == "incorrectly_timed_leet" for e in t["events"]])]
	x_decay = [t["time"] for t in prune_ticks(ticks) if any([e["id"] == "decay" for e in t["events"]])]
	y_decay = [t["score"] for t in prune_ticks(ticks) if any([e["id"] == "decay" for e in t["events"]])]

	plt.plot(x, y, c='k')
	plt.scatter(x_int_leet, y_int_leet, 33, c="r", alpha=1, marker=r'$\Delta$', label="Interrupted")
	plt.scatter(x_leet_timing, y_leet_timing, 33, c="b", alpha=1, marker=r'$\Delta$', label="Mistimed")
	plt.scatter(x_decay, y_decay, 33, c="g", alpha=0.2, marker=r'$\nabla$', label="Decay")
	
	plt.grid(True)
	plt.ylabel("Score")
	plt.xlabel("Time [d]")
	start, end = plt.xlim()
	xtick_count = int(end) // 1440

	plt.xticks(np.arange(0, end, 1440), range(xtick_count))
	plt.show()
