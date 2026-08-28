SCORES = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}


def calculate_score(lines_cleared: int) -> int:
    return SCORES.get(lines_cleared, 0)
