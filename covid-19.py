import numpy as np
import matplotlib.pyplot as plt

covid_data = np.array([
    [1500, 2000, 1800, 1200, 900], 
    [1600, 2100, 1900, 1300, 950], 
    [1700, 2200, 2000, 1400, 1000],
    [1650, 2150, 1950, 1350, 980],
    [1750, 2250, 2050, 1450, 1020],
    [1800, 2300, 2100, 1500, 1050],
    [1900, 2400, 2200, 1600, 1100],  
])

countries = ['Country_A', 'Country_B', 'Country_C', 'Country_D', 'Country_E']


total_cases = np.sum(covid_data, axis=0)
print("Total cases per country:", total_cases)

max_cases_country = countries[np.argmax(total_cases)]
print("Country with the highest total cases:", max_cases_country)

daily_average_cases = np.mean(covid_data, axis=1)
print("Daily average cases across all countries:", daily_average_cases)

total_cases_per_day = np.sum(covid_data, axis=1)
highest_cases_day = np.argmax(total_cases_per_day) + 1
print("Day with the highest total cases:", highest_cases_day)

percentage_change = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
print("Percentage change in cases for each country from Day 1 to Day 7:", percentage_change)

highest_increase_country = countries[np.argmax(percentage_change)]
print("Country with the highest percentage increase:", highest_increase_country)

normalized_data = (covid_data - np.min(covid_data, axis=0)) / (np.max(covid_data, axis=0) - np.min(covid_data, axis=0))
print("Normalized dataset:\n", normalized_data)

plt.figure(figsize=(10, 6))
for i, country in enumerate(countries):
    plt.plot(range(1, 8), covid_data[:, i], label=country)

plt.axvline(x=highest_cases_day, color='red', linestyle='--', label=f'Highest Cases Day (Day {highest_cases_day})')

plt.title("Daily COVID-19 Cases for Each Country")
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.show()
