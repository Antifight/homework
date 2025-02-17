def check_exam_consistency(grades_results):
    passed = []
    failed = []

    for grade, result in grades_results:
        if result == "Passed":
            passed.append(grade)
        else:
            failed.append(grade)

    if passed and failed and min(passed) < max(failed):
        print("Inconsistent")
    else:
        print("Consistent")

    if passed:
        lower_bound = min(passed)
    else:
        lower_bound = None

    if failed:
        upper_bound = max(failed)
    else:
        upper_bound = None

    print(f"Passing threshold range: {upper_bound} - {lower_bound}")

students_results = [(60, "Failed"), (70, "Passed"), (80, "Passed"), (65, "Failed")]
check_exam_consistency(students_results)



