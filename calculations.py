import math


class Calculations:

    @staticmethod
    def calculate_mean(data):

        return float(sum(data)) / max(len(data), 1)

    @staticmethod
    def calculate_mode(data):

        hits = []
        for item in data:
                tally = data.count(item)
                values = (tally, item)
                if values not in hits:
                    hits.append(values)

        hits.sort(reverse=True)

        if hits[0][0] > hits[1][0]:
            return hits[0][1]
        else:
            # There is not a median.
            return None

    @staticmethod
    def calculate_median(data):

        sortedList = sorted(data)
        length = len(data)

        if length < 1:
            return None
        if length % 2 == 1:
            return sortedList[length//2]
        else:
            return sum(sortedList[length//2-1:length//2+1])/2.0

    @staticmethod
    def calculate_standard_deviation(data):
        standardDtemp = Calculations.calculate_variance(data)
        standardD = math.sqrt(standardDtemp)
        return standardD

    @staticmethod
    def calculate_variance(data):
        variance = 0
        amean = Calculations.calculate_mean(data)
        for item in data:
            variance += (item-amean)**2 / (len(data) - 1)
        return variance

    @staticmethod
    def calculate_coefficient_of_variance(data):
        sd = Calculations.calculate_standard_deviation(data)
        thismean = Calculations.calculate_mean(data)
        coeffofVar = sd / thismean
        return coeffofVar

    @staticmethod
    def calculate_percentiles(percentile, data):
        data = sorted(data)
        print(data)
        index = len(data) * percentile
        index = int(index)
        thepercentile = data[0+(index-1)]
        return thepercentile

    @staticmethod
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * Calculations.fact(n - 1)

    @staticmethod
    def calculate_probability_distribution(successes, trials):
        #successes is the number you want to find probability of getting.
        #trials could receive len(data)
        #if user wants cumulative, can acheive by calling this in for loop.
        fail = trials-successes
        probDist = successes / (successes+fail)
        return probDist

    @staticmethod
    def calculate_binomial_distribution(prob, trials, succ):
        fail = 1-prob
        binDist = ((Calculations.fact(trials))/(Calculations.fact(trials-succ)*Calculations.fact(succ)))*((prob**succ)*(fail**(trials-succ)))
        return binDist

    @staticmethod
    def calculate_covariance(x, y):
        mean_x = Calculations.calculate_mean(x)
        mean_y = Calculations.calculate_mean(y)
        length = len(x)
        a = [item - mean_x for item in x]
        b = [item - mean_y for item in y]
        ev_sum = sum([i * j for i, j in zip(a, b)])
        cov = ev_sum / (length - 1)
        return cov

    @staticmethod
    def calculate_pearson_correlation(x, y):
        cov = Calculations.calculate_covariance(x, y)
        stddev_x = Calculations.calculate_standard_deviation(x)
        stddev_y = Calculations.calculate_standard_deviation(y)
        pearson_cor = cov / (stddev_x * stddev_y)
        return pearson_cor

    @staticmethod
    def calculate_least_square_line(x, y):

        mean_x = Calculations.calculate_mean(x)
        mean_y = Calculations.calculate_mean(y)
        stddev_x = Calculations.calculate_standard_deviation(x)
        stddev_y = Calculations.calculate_standard_deviation(y)
        pearson_cor = Calculations.calculate_pearson_correlation(x, y)

        slope = pearson_cor * (stddev_y / stddev_x)
        intercept = mean_y - (slope * mean_x)
        regression = "Y = " + "{0:.4f}".format(intercept) + " + (" + "{0:.4f}".format(slope) + ")X"
        return regression

    @staticmethod
    def calculate_chi_square(x, y):

        sum_col_x = sum(x)
        sum_col_y = sum(y)
        sum_rows = [a + b for a, b in zip(x, y) ]
        sum_sums = sum(sum_rows)

        expected_x = [(a * sum_col_x) / sum_sums for a in sum_rows]
        expected_y = [(a * sum_col_y) / sum_sums for a in sum_rows]

        x_squared_x = sum([((a - b) ** 2) / b for a, b in zip(x, expected_x)])
        x_squared_y = sum([((a - b) ** 2) / b for a, b in zip(y, expected_y)])
        x_squared = x_squared_y + x_squared_x
        return x_squared

    @staticmethod
    def calculate_correlation_coefficient(x, y):

        mean_x = Calculations.calculate_mean(x)
        mean_y = Calculations.calculate_mean(y)
        stddev_x = Calculations.calculate_standard_deviation(x)
        stddev_y = Calculations.calculate_standard_deviation(y)

        diff_x = [a - mean_x for a in x]
        diff_y = [a - mean_y for a in y]
        prod = [a * b for a, b in zip(diff_x, diff_y)]
        sum_prod = sum(prod)

        div = sum_prod / (stddev_x * stddev_y)
        cor = div / (len(x) - 1)
        return cor

    @staticmethod
    def calculate_sign_test(x, y):

        positives = 0
        negatives = 0
        zeroes = 0
        differences = [a - b for a, b in zip(x,y)]

        for item in differences:
            if item > 0:
                positives += 1
            if item < 0:
                negatives += 1
            else:
                zeroes += 1

        sum = positives + negatives - zeroes
        pval = Calculations.calculate_binomial_distribution(.5, sum, positives)

        if pval < 0.05:
            return "Reject"
        else:
            return "Accept"

    @staticmethod
    def calculate_rank_sum_test(x, y):
        merged_list = x + y
        ranks = Calculations.get_rank(merged_list)
        ranks_x = ranks[:len(x)]
        ranks_y = ranks[len(x):]
        count_x = len(ranks_x)
        count_y = len(ranks_y)
        rank_sum_x = sum(ranks_x)
        rank_sum_y = sum(ranks_y)

        w = min(rank_sum_x, rank_sum_y)

        if count_x < count_y:
            n_s = count_x
            n_l = count_y
        else:
            n_s = count_y
            n_l = count_x

        mean_w = (n_s *(n_s + n_l + 1)) / 2
        std_w = ((n_s * n_l *(n_s + n_l + 1)) / 12) ** 0.5
        z = (w - mean_w) / std_w

        return z

    @staticmethod
    def calculate_spearman_rank(x, y):

        rank_x = Calculations.get_rank(x)
        rank_y = Calculations.get_rank(y)
        spearman = Calculations.calculate_pearson_correlation(rank_x, rank_y)
        return spearman

    @staticmethod
    def get_rank(data):

        n = len(data)
        rank = []

        for i in range(0, n):
            r = 1
            s = 1

            for j in range(0, i):
                if data[j] < data[i]:
                    r += 1
                if data[j] == data[i]:
                    s += 1

            for j in range(i + 1, n):
                if data[j] < data[i]:
                    r += 1
                if data[j] == data[i]:
                    s += 1

            rank.append(r + (s - 1) * 0.5)

        return rank
