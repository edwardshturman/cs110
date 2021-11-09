heart_rates = [[72, 75, 71, 73],  # resting
               [91, 90, 94, 93],  # walking slowly
               [130, 135, 139, 142],  # running on treadmill
               [120, 118, 110, 105, 100, 98]]  # after a minute of recovery

hr_averages = []

for hr_set in heart_rates:
    hr_set_sum = 0
    for hr in hr_set:
        hr_set_sum += hr
    hr_averages.append(hr_set_sum / len(hr_set))

print(hr_averages)
