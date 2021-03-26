from random import randint
import plotly.graph_objects as go
import plotly.io as pio
# pio.renderers.default = 'svg'
pio.renderers.default = 'browser'
import matplotlib.pyplot as plt

def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted numbers that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use external libraries other than those already
        imported.
    """
    ints_count = {}
    for i in data:
        ints_count[i] = ints_count.get(i,0) + 1
    histogram_bins = dict.fromkeys(bins, 0)
    for i in range(len(bins)-1):
        filtered = {k : v for k,v in ints_count.items() if bins[i] < k < bins[i+1]}
        histogram_bins[bins[i]] = sum(filtered.values())
    return histogram_bins

def plot_histogram(bins_count):
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    y = list(bins_count.values())
    bins = list(bins_count.keys())
    labels = []
    for i in range(len(bins)-1):
        labels.append(f"{bins[i]}".zfill(3) + f"-{bins[i+1]}".zfill(4))
    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=y,
        text=y,
        textposition='auto',)])
    fig.update_layout(
        title="histogram chart of counts per bin",
        xaxis_title="bins",
        yaxis_title="count")
    fig.show()

if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
