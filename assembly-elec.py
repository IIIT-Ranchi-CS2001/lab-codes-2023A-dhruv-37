import matplotlib.pyplot as plt

data = {
    'Madhya Pradesh': {'BJP': 163, 'INC': 66, 'BSP': 0, 'Others': 1},
    'Rajasthan': {'BJP': 115, 'INC': 69, 'BSP': 2, 'Others': 13}
}

colors = ['#FFD700', '#1E90FF', '#8A2BE2', '#32CD32']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle("Assembly Elections 2023: Party-wise Seat Share", fontsize=16)

def create_pie_chart(ax, state, data, colors):
    seats = list(data.values())
    labels = list(data.keys())
    explode = [0.1 if i == seats.index(max(seats)) else 0 for i in range(len(seats))]
    ax.pie(seats, labels=[f"{label} - {seat} ({seat/sum(seats)*100:.1f}%)" for label, seat in zip(labels, seats)],
           autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, wedgeprops={'edgecolor': 'black'})
    ax.set_title(f"{state}")

create_pie_chart(ax1, 'Madhya Pradesh', data['Madhya Pradesh'], colors)
create_pie_chart(ax2, 'Rajasthan', data['Rajasthan'], colors)

parties = list(data['Madhya Pradesh'].keys())
mp_seats = list(data['Madhya Pradesh'].values())
rj_seats = list(data['Rajasthan'].values())

fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
x = range(len(parties))
bar_width = 0.35
ax_bar.bar(x, mp_seats, width=bar_width, color='#FFD700', label='Madhya Pradesh', edgecolor='black')
ax_bar.bar([p + bar_width for p in x], rj_seats, width=bar_width, color='#1E90FF', label='Rajasthan', edgecolor='black')
ax_bar.set_xticks([p + bar_width / 2 for p in x])
ax_bar.set_xticklabels(parties)
ax_bar.set_xlabel("Parties")
ax_bar.set_ylabel("Seats Won")
ax_bar.set_title("Assembly Elections 2023: Party-wise Seats Won (Bar Chart)")
ax_bar.legend()

plt.show()
