def reverse(S, start, stop):
    """Reverse elements in implicit size"""
    if start >= stop:
        return 0
    else:
        S[start], S[stop] = S[stop], S[start]
        reverse(S, start + 1, stop - 1)
