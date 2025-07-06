import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

years = ['2020', '2021', '2022', '2023', '2024']
stations = ['Anand Vihar', 'Collectorate', 'Rajbansi Nagar', 'Chhoti Gwaltoli', 'GVM Corporation']
categories = ['0-50 : Good', '51-100 : Satisfactory', '101-200 : Moderate', '201-300 : Poor', '301-400 : Very Poor', '401-500 : Severe']

colors = aqi_colors = [
     '#009865',          # Green
    '#A3C853',  # Light Green/Yellow-Green
   '#FFF833',      # Yellow
   '#F29C33',          # Orange
   '#E93F33',     # Red
    '#AF2D24'         # Dark Red
]





raw_data = [
    [   # 2020
        [3, 65, 91, 62, 55, 30],        # Anand Vihar
        [0, 23, 54, 46, 38, 29],        # Collectorate
        [2, 33, 54, 90, 95, 43],        # Rajbansi Nagar
        [3, 30, 79, 78, 62, 48],        # Chhoti Gwaltoli
        [0, 17, 79, 67, 92, 46]         # GVM Corporation
    ],
    [   # 2021
        [3, 98, 145, 49, 2, 0],         # Anand Vihar
        [0, 62, 162, 64, 8, 0],         # Collectorate
        [5, 90, 79, 108, 63, 2],        # Rajbansi Nagar
        [np.nan]*6,                             # Chhoti Gwaltoli (no data)
        [22, 86, 191, 38, 7, 0]         # GVM Corporation
    ],
    [   # 2022
        [37, 39, 63, 32, 23, 2],        # Anand Vihar
        [31, 54, 89, 69, 46, 0],        # Collectorate
        [14, 83, 67, 81, 83, 5],        # Rajbansi Nagar
        [3, 63, 120, 84, 58, 2],        # Chhoti Gwaltoli
        [26, 82, 124, 82, 17, 0]        # GVM Corporation
    ],
    [   # 2023
        [36, 119, 130, 14, 0, 0],       # Anand Vihar
        [38, 66, 106, 37, 0, 0],        # Collectorate
        [22, 77, 138, 7, 0, 0],         # Rajbansi Nagar
        [np.nan]*6,                             # Chhoti Gwaltoli (no data)
        [4, 142, 165, 40, 2, 0]         # GVM Corporation
    ],
    [   # 2024
        [37, 84, 86, 31, 4, 0],         # Anand Vihar
        [31, 70, 100, 24, 0, 0],        # Collectorate
        [27, 130, 148, 21, 1, 0],       # Rajbansi Nagar
        [6, 107, 160, 39, 2, 0],        # Chhoti Gwaltoli
        [20, 145, 157, 16, 5, 0]        # GVM Corporation
    ]
]


raw_data = np.array(raw_data)

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.12
indices = np.arange(len(years))

# Hatches for stations (optional, for visual distinction)
hatches = ['', '//', '\\\\', 'xx', 'oo']

for i, station in enumerate(stations):
    bottoms = np.zeros(len(years))
    for j, category in enumerate(categories):
        values = raw_data[i, :, j]
        label = categories[j] if i == 0 else None
        ax.bar(indices + i * bar_width, values, bar_width, bottom=bottoms,
               color=colors[j], label=label, alpha=0.85, edgecolor='black', linewidth=1,
               hatch=hatches[i])
        bottoms += values

ax.set_xlabel('Year')
ax.set_ylabel('Number of Days')
ax.set_title('AQI of various monitoring stations across the years')
ax.set_xticks(indices + 2 * bar_width)
ax.set_xticklabels(years)

# 1st legend: AQI Category
handles_cat = [Patch(facecolor=colors[j], edgecolor='black', label=categories[j]) for j in range(len(categories))]
legend1 = ax.legend(handles=handles_cat, title="AQI Category", bbox_to_anchor=(1.01, 1), loc='upper left',fontsize=12, title_fontsize=14)

# 2nd legend: Stations (using hatches for distinction)
handles_station = [Patch(facecolor='white', edgecolor='black', label=stations[i], hatch=hatches[i]) for i in range(len(stations))]
legend2 = ax.legend(handles=handles_station, title="Station", bbox_to_anchor=(1.04, 0.55), loc='upper left',fontsize=12, title_fontsize=14)

# Add both legends
ax.add_artist(legend1)  # Add the first legend manually


plt.show()
