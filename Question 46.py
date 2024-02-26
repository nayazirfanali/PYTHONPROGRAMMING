def determine_season(month, day):
    # Convert the month to a standardized format to simplify comparison
    month = month.lower()[:3]
    months = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4,
        "may": 5, "jun": 6, "jul": 7, "aug": 8,
        "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }

    # Assign numerical values to each season's starting month and day
    seasons = {
        "spring": ("mar", 20),
        "summer": ("jun", 21),
        "fall": ("sep", 22),
        "winter": ("dec", 21)
    }

    # Determine the current season based on the month and day
    if (months[month], day) >= (months[seasons["spring"][0]], seasons["spring"][1]) and (months[month], day) < (months[seasons["summer"][0]], seasons["summer"][1]):
        return "The season is currently spring"
    elif (months[month], day) >= (months[seasons["summer"][0]], seasons["summer"][1]) and (months[month], day) < (months[seasons["fall"][0]], seasons["fall"][1]):
        return "The season is currently summer"
    elif (months[month], day) >= (months[seasons["fall"][0]], seasons["fall"][1]) and (months[month], day) < (months[seasons["winter"][0]], seasons["winter"][1]):
        return "The season is currently fall"
    else:
        return "The season is currently winter"

# Example usage
month = input("Enter the month: ")
day = int(input("Enter the date: "))
print(determine_season(month, day))
