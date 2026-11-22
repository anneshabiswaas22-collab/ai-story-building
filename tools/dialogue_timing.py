"""Provisional in-clip speech cues for the 15-second Maple House screenplays."""

def cue_windows(dialogue):
    """Return ordered clip-local (start, end) pairs in milliseconds."""
    start = 250
    gap = 150
    # Allow short replies to land and give longer lines time proportional to length.
    weights = [max(850, len(line.split()) * 440 + 80) for _, line in dialogue]
    turn_gaps = (len(weights) - 1) * gap
    last_end = min(14300, max(12400, start + sum(weights) + turn_gaps))
    speech_budget = last_end - start - turn_gaps
    windows = []
    elapsed_weight = 0
    total_weight = sum(weights)
    for i, weight in enumerate(weights):
        begin = start + i * gap + round(speech_budget * elapsed_weight / total_weight)
        elapsed_weight += weight
        end = start + i * gap + round(speech_budget * elapsed_weight / total_weight)
        windows.append((begin, end))
    return windows


def performance_note(dialogue, windows):
    cues = ' · '.join(
        f'{speaker} {start / 1000:.2f}–{end / 1000:.2f}s'
        for (speaker, _), (start, end) in zip(dialogue, windows)
    )
    return ('**Delivery:** Begin speaking on the opening action. Keep replies close and in order. '
            'Let listeners react during speech. Finish the physical beat on the cut. '
            f'Speaker cues from clip start (estimated): {cues}.')
