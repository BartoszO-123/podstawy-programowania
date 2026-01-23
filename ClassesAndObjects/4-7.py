class Statistics:
    def __init__(self):
        self.numbers = []

    def add_from_keyboard(self):
        self.numbers.append(float(input()))

    def add(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        print(*self.numbers)

    def get_max(self):
        return max(self.numbers)

    def get_min(self):
        return min(self.numbers)

    def get_mean(self):
        return sum(self.numbers) / len(self.numbers)

    def get_median(self):
        sorted_nums = sorted(self.numbers)
        n = len(sorted_nums)
        if n % 2 == 1:
            return sorted_nums[n // 2]
        else:
            return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

    def print_stats(self):
        print(f'Minimum: {self.get_min()}')
        print(f'Maximum: {self.get_max()}')
        print(f'Mean: {self.get_mean()}')
        print(f'Median: {self.get_median()}')

stats = Statistics()
data = [12, 37, 6, 9, 17]

for num in data:
    stats.add(num)

stats.display_numbers()
stats.print_stats()