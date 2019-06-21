import matplotlib.pyplot as plt

def plot_ticks(ticks):
	plt.plot([t["time"] for t in ticks], [t["score"] for t in ticks])
	plt.ylabel("Score")
	plt.xlabel("Time [m]")
	plt.show()
