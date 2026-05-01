#Problem 1: Dictionary- Gradebook summary

grades = {
"alice": {"CS1350": [85, 92, 78], "MATH201": [90, 88]},
"bob": {"CS1350": [72, 75, 80], "PHYS100": [65, 70]},
"carol": {"CS1350": [95, 98, 92], "MATH201": [85, 90]},
}

print("=" * 50)

def gradebook_summary(grades):
    student_averages = {}
    course_averages = {}
    top_per_course = {}

    for student, courses in grades.items():
        total_scores = []
        for course, scores in courses.items():
            total_scores.extend(scores)
            if course not in course_averages:
                course_averages[course] = []
            course_averages[course].extend(scores)

            avg_score = sum(scores) / len(scores)
            if course not in top_per_course or avg_score > top_per_course[course][1]:
                top_per_course[course] = (student, avg_score)
            elif avg_score == top_per_course[course][1]:
                top_per_course[course] = min(top_per_course[course], (student, avg_score))

        student_averages[student] = sum(total_scores) / len(total_scores)

    for course in course_averages:
        course_averages[course] = sum(course_averages[course]) / len(course_averages[course])

    return {
        "student_averages": student_averages,
        "course_averages": course_averages,
        "top_per_course": {course: student for course, (student, _) in top_per_course.items()}
    }
    
print(gradebook_summary(grades))
print("=" * 50)


#Problem 2: Candidate Skill matcher


candidates = {
"alice": {"python", "sql", "git", "docker"},
"bob": {"python", "java", "git"},
"carol": {"python", "sql", "git", "docker", "kubernetes"},
"dave": {"java", "c++"},
"eve": {"python", "sql"},
}
required = {"python", "sql", "git"}


def skill_analysis(candidates, required):
    fully_qualified = []
    best_match = None
    max_skills = 0
    unique_skills = {}

    for candidate, skills in candidates.items():
        if required.issubset(skills):
            fully_qualified.append(candidate)

        num_required_skills = len(skills.intersection(required))
        if num_required_skills > max_skills or (num_required_skills == max_skills and (best_match is None or candidate < best_match)):
            best_match = candidate
            max_skills = num_required_skills

        unique = skills.copy()
        for other_candidate, other_skills in candidates.items():
            if other_candidate != candidate:
                unique -= other_skills
        if unique:
            unique_skills[candidate] = sorted(unique)

    return {
        "fully_qualified": sorted(fully_qualified),
        "best_match": best_match,
        "unique_skills": unique_skills
    }

print(skill_analysis(candidates, required))
print("=" * 50)