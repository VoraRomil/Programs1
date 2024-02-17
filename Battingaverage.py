#!/usr/bin/env python3

if __name__ == '__main__':
    Matches = 609
    team_Batted = 1014
    Not_out = 162
    Total_runs = 48426

# how many times out
completed_innings = team_Batted - Not_out

print(f"The average of Geoffrey Boycott is {Total_runs / completed_innings}")