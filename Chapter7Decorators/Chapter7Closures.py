"""
This creates an averaging instance varible
avg = Average()
avg(10) = 10
avg(11) = 11
if we used the first version of make_averager()

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

In this case, the series was just appended to, rather than updated
hence, lists are immutable and this works

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total/count

Since we are reassigning count and total, it is creating count as a local
similar to how globals work when we have a similarly named global.

freevars allow us to access variables outside the scope. using nonlocal,
we can add a variable to the freevar set.

The nonlocal Declaration:

"""


class Averager():

    def __init__():
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)
