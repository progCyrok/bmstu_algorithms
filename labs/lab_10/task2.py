#Задача о покрытии отрезками

def min_segments_to_cover(target_segment, segments):
    segments.sort(key=lambda x: x[1])

    target_start, target_end = target_segment
    covered_until = target_start
    segments_used = 0
    i = 0

    while covered_until < target_end:
        best_next_cover = covered_until
        while i < len(segments) and segments[i][0] <= covered_until:
            best_next_cover = max(best_next_cover, segments[i][1])
            i += 1

        if best_next_cover == covered_until:
            return -1

        covered_until = best_next_cover
        segments_used += 1

    return segments_used


target_segment = (1, 5)
segments = [(1, 2), (2, 3), (3, 4), (0, 1), (4, 5), (1, 3)]

result = min_segments_to_cover(target_segment, segments)
print(f"Минимальное количество отрезков для покрытия: {result}")
