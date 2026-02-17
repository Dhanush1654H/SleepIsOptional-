def average_passing_grades(grades: list[int]) -> float:
    passing = [g for g in grades if g >= 50]
    if not passing:
        return 0.0
    return sum(passing) / len(passing)
