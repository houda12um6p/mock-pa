# scoring logic for merge requests
def calculate_score(base, comments, story_points):
    return max(0, base - 1.4 ** max(0, comments - story_points))
