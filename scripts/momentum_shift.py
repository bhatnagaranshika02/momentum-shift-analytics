import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("match_cleaned_full.csv")
over_data = data.copy()

penalty = 5
over_data['momentum'] = over_data["runs"] - over_data['wicket'] * penalty

powerplay = over_data[over_data['over'] < 6]
middle = over_data[(over_data['over'] >= 6) & (over_data['over'] < 16)]
death = over_data[over_data['over'] >= 16]

def analyze_phase(phase_data, name):
    avg_runs = phase_data['runs'].mean()
    total_wickets = phase_data['wicket'].sum()
    avg_momentum = phase_data['momentum'].mean()
    max_shift = phase_data['momentum'].diff().abs().max()

    print(f"\n📊 {name.upper()} PHASE")
    print(f"Avg Runs/Over     : {avg_runs:.2f}")
    print(f"Total Wickets     : {total_wickets}")
    print(f"Avg Momentum Score: {avg_momentum:.2f}")
    print(f"Max Momentum Shift: {max_shift:.2f}")

analyze_phase(powerplay, "Powerplay")
analyze_phase(middle, "Middle")
analyze_phase(death, "Death")

plt.figure(figsize=(12, 6))
plt.plot(over_data['over'], over_data['momentum'], marker='o', label="Momentum Score", color='black')


for i, row in over_data.iterrows():
    plt.text(row['over'], row['momentum'] + 1, f"{int(row['momentum'])}", 
             ha='center', fontsize=8, color='darkblue')

plt.axvspan(0, 5, color='green', alpha=0.1, label='Powerplay')
plt.axvspan(6, 15, color='blue', alpha=0.1, label='Middle Overs')
plt.axvspan(16, max(over_data['over']), color='red', alpha=0.1, label='Death Overs')

plt.title("Cricket Match Momentum Graph by Anshika")
plt.xlabel("Over")
plt.ylabel("Momentum Score")
plt.xticks(np.arange(min(over_data['over']), max(over_data['over']) + 1, 1))
plt.yticks(np.arange(min(over_data['momentum']), max(over_data['momentum']) + 5, 5))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("phase_wise_momentum_labeled.png")
plt.show()
