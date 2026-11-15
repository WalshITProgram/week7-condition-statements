# IT 410 - Week 7 - Working with Condition Statements
# Name: Ahmed Gulam

# =====================================================
# Requirement 1: Create a single list with the data
# =====================================================
employee_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma",
]

# =====================================================
# Requirements 2 and 3: Sort into three lists by type,
# with no duplicates
# =====================================================
employee_numbers = []
employee_names = []
hourly_wages = []

for item in employee_data:
    # bool is a subclass of int in Python, so booleans must be
    # skipped first or True/False would be treated as numbers
    if isinstance(item, bool):
        continue
    if isinstance(item, int):
        if item not in employee_numbers:
            employee_numbers.append(item)
    elif isinstance(item, str):
        if item not in employee_names:
            employee_names.append(item)
    elif isinstance(item, float):
        if item not in hourly_wages:
            hourly_wages.append(item)

print("Employee numbers:", employee_numbers)
print("Employee names:", employee_names)
print("Hourly wages:", hourly_wages)

# =====================================================
# Requirement 4: Add 30% for benefits, then check the max
# =====================================================
total_hourly_rate = []

for wage in hourly_wages:
    total_hourly_rate.append(wage * 1.3)

max_rate = max(total_hourly_rate)
print(f"\nHighest total hourly rate: {max_rate:.2f}")

if max_rate > 37.30:
    print("WARNING: Someone's salary may be a budget concern.")

# =====================================================
# Requirement 5: Total hourly rates between 28.15 and 30.65
# =====================================================
underpaid_salaries = []

for rate in total_hourly_rate:
    if 28.15 <= rate <= 30.65:
        underpaid_salaries.append(rate)

print("\nUnderpaid salaries:", [round(rate, 2) for rate in underpaid_salaries])

# =====================================================
# Requirement 6: Calculate raises (in dollars) on the
# unmodified hourly wages
# =====================================================
company_raises = []

for wage in hourly_wages:
    if 22 <= wage < 24:
        raise_amount = wage * 0.05
    elif 24 <= wage < 26:
        raise_amount = wage * 0.04
    elif 26 <= wage < 28:
        raise_amount = wage * 0.03
    else:
        raise_amount = wage * 0.02
    company_raises.append(raise_amount)

print("\nCompany raises ($):", [round(raise_amount, 2) for raise_amount in company_raises])

# =====================================================
# Requirement 7: My own complex condition (4 truth tests)
# =====================================================
# Behavior: print a staffing review message only if
#   1) there are at least 5 unique employee numbers, AND
#   2) the highest employee number is above 1150, AND
#   3) either the lowest hourly wage is under $23.00
#      OR there is at least one entry in underpaid_salaries.
if len(employee_numbers) >= 5 and max(employee_numbers) > 1150 and (min(hourly_wages) < 23 or len(underpaid_salaries) > 0):
    print("\nStaffing review needed: newer employees and low wages detected.")
