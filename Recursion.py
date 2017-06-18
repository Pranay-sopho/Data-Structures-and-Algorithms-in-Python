import os


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(3))

def draw_line(tick_length, tick_label=''):
    if tick_label == '':
        print('-' * tick_length)
    else:
        print('-' * tick_length, tick_label)


def draw_interval(center_length):
    """
    if center_length == 1:
    draw_line(1)
    else:
    """
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j + 1))


# draw_ruler(3, 6)


def binary_search(data, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return False
    else:
        if target == data[mid]:
            return True
        elif target > data[mid]:
            return binary_search(data, target, mid + 1, high)
        else:
            return binary_search(data, target, low, mid - 1)


"""
data = [1,2,3,4,5,6,7]
print(binary_search(data, 0, 0, 6))
"""


def reverse(S, start, stop):
    if start >= stop:
        return 0
    else:
        S[start], S[stop] = S[stop], S[start]
        reverse(S, start + 1, stop - 1)


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for child in os.listdir(path):
            child_path = os.path.join(path, child)
            total += disk_usage(child_path)
    print('{0:<7}'.format(total), path)
    return total


# disk_usage('E:\BOOKS')

def good_power(x, n):
    if n == 0:
        return 1
    else:
        partial = good_power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


def binary_sum(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (stop + start) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
