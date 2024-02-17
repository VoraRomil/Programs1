#!/usr/bin/env python3

if __name__ == '__main__':
    def group_division(total_students, group_size):
        Full_groups = total_students // group_size
        leftover_students = total_students % group_size
        return Full_groups, leftover_students

# Number of students is 113
Full_groups, leftover_students = group_division(113, 24)
print(f"For 113 students, there are {Full_groups} full groups of 24, with {leftover_students} students left over.")

# Number of students is 175
Full_groups, leftover_students = group_division(175, 24)
print(f"For 175 students, there are {Full_groups} full groups of 24, with {leftover_students} students left over.")

# Number of students is 12
Full_groups, leftover_students = group_division(12, 24)
print(f"For 12 students, there are {Full_groups} full groups of 24, with {leftover_students} students left over.")