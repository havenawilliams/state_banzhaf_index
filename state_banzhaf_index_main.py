import pandas as pd
import itertools
import os

os.chdir("G:\\My Drive\\R\\ON Research Projects\\state_banzhaf_index")

def generate_power_sets(s):
    return list(itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1)))

def banzhaf_index(states):
    total_votes = sum(states.values())
    quota = total_votes // 2 + 1

    power_sets = generate_power_sets(list(states.keys()))

    banzhaf_dict = {k: 0 for k in states.keys()}

    for power_set in power_sets:
        power_set_votes = sum(states[state] for state in power_set)

        for state in power_set:
            without_state_votes = power_set_votes - states[state]

            if without_state_votes < quota <= power_set_votes:
                banzhaf_dict[state] += 1

    total_power = sum(banzhaf_dict.values())
    banzhaf_dict = {k: v / total_power for k, v in banzhaf_dict.items()}

    return banzhaf_dict

# Import CSV file into a DataFrame
N = 52
df = pd.read_csv('states_votes.csv', nrows = N)

# Convert the DataFrame into a dictionary where the state names are keys and their votes are values
states = df.set_index('state')['votes'].to_dict()

banzhaf_dict = banzhaf_index(states)

# Creating a DataFrame
df_banzhaf = pd.DataFrame(list(banzhaf_dict.items()), columns=['State', 'Banzhaf Power Index'])
print(df_banzhaf)
len(df_banzhaf)
