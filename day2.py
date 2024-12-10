reports = []

with open("day2.txt", "r") as file:
    for report in file:
        report_list = [int(l) for l in report.strip().split()]

        reports.append(report_list)


num_safe = 0

for report in reports:
    increasing = report[0] < report[-1]

    is_safe = True

    for (level, next_level) in zip(report, report[1:]):
        if not 1 <= abs(level - next_level) <= 3:
            is_safe = False
            break
        if increasing:
            if level >= next_level:
                is_safe = False
                break
        else:
            if level <= next_level:
                is_safe = False
                break

    if is_safe:
        num_safe += 1

print(num_safe)


def is_report_safe(report: list[int]) -> (bool, int | None):
    increasing = report[0] < report[-1]

    is_safe = True
    failed_at = None

    for i, (level, next_level) in enumerate(zip(report, report[1:])):
        if not 1 <= abs(level - next_level) <= 3:
            is_safe = False
            failed_at = i
            break
        if increasing:
            if level >= next_level:
                is_safe = False
                failed_at = i
                break
        else:
            if level <= next_level:
                is_safe = False
                failed_at = i
                break

    if is_safe:
        return True, None
    return False, failed_at


num_safe = 0

for report in reports:
    initial_result, failed_at = is_report_safe(report)

    if initial_result:
        num_safe += 1
        continue

    dampening_worked = False

    for i in range(failed_at, len(report) - 1):
        new_report = report[:i] + report[i + 1:]
        result, _ = is_report_safe(new_report)
        if result:
            num_safe += 1
            dampening_worked = True
            break

    if not dampening_worked:
        new_report = report[:-1]
        result, _ = is_report_safe(new_report)
        if result:
            num_safe += 1
            continue

print(num_safe)
