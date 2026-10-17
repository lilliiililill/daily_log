# 2026.10.18
# monty_hall_sim.py

import random

def monty_hall(trials = 10000):

    switch_wins = 0
    stay_wins = 0

    for i in range(trials):

        doors = [0, 1, 2]
        car = random.choice(doors)
        pick = random.choice(doors)


        host_options = [d for d in doors if d != pick and d != car]
        host_open = random.choice(host_options) if host_options else [d for d in doors if d != pick][0]

        switch_pick = [d for d in doors if d != pick and d != host_open][0]

        if switch_pick == car:

            switch_wins += 1

        if pick == car:

            stay_wins += 1

    return switch_wins / trials, stay_wins / trials

switch_rate, stay_rate = monty_hall()

print(f"바꾸기 승률: {switch_rate:.3f}")
print(f"유지 승률: {stay_rate:.3f}")
