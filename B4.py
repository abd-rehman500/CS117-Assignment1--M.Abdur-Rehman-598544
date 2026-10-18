#A battery management system records voltage readings every minute. Given a hardcoded list of readings such as voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2], use a loop to find the longest consecutive streak of strictly decreasing voltage readings. Do not use built-in sorting or grouping functions. Print the length of the longest streak, as well as the starting and ending voltages of that specific sequence. Sample run: Longest continuous drop: 4 minutes Started at: 12.5 V Ended at: 11.9 V

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

current_strk = 1
great_strk = 0

for i in range(1, len(voltages)):
    if (voltages[i] < voltages[i - 1]):
        current_strk += 1
    else:
        if (current_strk > great_strk):
            great_strk = current_strk
            start_v = voltages[i - current_strk]
            end_v = voltages[i - 1]
        current_strk = 1

print(f"Longest continuous drop: {great_strk} minutes")
print(f"Started at: {start_v} V")
print(f"Ended at: {end_v} V")


