import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import Habit, track_habit

def main():
    habits: list[Habit] = [
        track_habit(name='Daydreaming', start=datetime(2024,11,26,22), cost=1, minutes_used=20),
        track_habit(name='Coffee', start=datetime(2024, 11, 1, 7),cost = 5, minutes_used = 10),
        track_habit(name='Helena', start=datetime(2024, 4, 28, 00), cost=100, minutes_used=200)
    ]

    df = pd.DataFrame(habits)

    print(tabulate(df, headers='keys',tablefmt='psql'))

if __name__ == '__main__':
    main()
