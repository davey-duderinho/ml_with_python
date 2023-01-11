import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):

    def __int__(self, prob=0.5, size=25):

        self.p = prob
        self.n = size

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
        # mu is the mean (default constructor with value of 0)
        # sigma is the standard deviation (default constructor with value of 1)
        # p is the probability
        # n is the size of the data set

    def calculate_mean(self):
        self.mean = self.p * self.n
        return self.mean

    def calculate_stdev(self):
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev

    def replace_stats_with_data(self):

        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.n, self.p

    def plot_bar(self):

        plt.bar(x=[0, 1], height=[(1 - self.p) * self.n, self.p * self.n])
        plt.title('Bar Chart of data')
        plt.xlabel('outcome')
        plt.ylabel('count')
        plt.show()

    def pdf(self, k):

        a = math.factorial(self.n) / math.factorial(k) * (math.factorial(self.n - k))
        b = (self.p ** k) * (1 - self.p) ** (self.n - k)
        return a * b

    def plot_bar_pdf(self):

        x = []
        y = []

        # calculate the x values to visualise
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))

        # make the bar plot
        plt.bar(x, y)
        plt.title('Distribution of Outcome')
        plt.xlabel('Probability')
        plt.ylabel('Outcome')
        plt.show()

        return x, y

    def __add__(self, other):

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = other.n + self.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def __repr__(self):

        print('mean {}. standard deviation {}, p {}, n{}'.format(self.mean, self.stdev, self.p, self.n))
