def calculate_grade(score):
    # Check the score from highest to lowest threshold
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
        
    return grade

# Quick test cases
scores = [95, 82, 74, 61, 45]