import numpy as np
import math


def p_to_c(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y


def gen_line(phase, mic_in_line, s_a, s_b):
    line_p_theta = np.array(range(0, mic_in_line)) * 1.8 * math.pi / mic_in_line
    line_p_r = s_a + s_b * line_p_theta / 1.8 / math.pi
    return zip(line_p_r, phase + line_p_theta)


def main():
    phase = 2 * math.pi / 3
    mic_in_line = 8
    s_a = 0.01
    size_r = 0.08
    line_p0 = gen_line(phase * 0, mic_in_line, s_a, size_r)
    line_p1 = gen_line(phase * 1, mic_in_line, s_a, size_r)
    line_p2 = gen_line(phase * 2, mic_in_line, s_a, size_r)
    line_p = [*line_p0, *line_p1, *line_p2]

    line = np.array([p_to_c(r, th) for r, th in line_p])  # * 100 / 0.00254  # as mil
    print('position')
    for x, y in line:
        print(x, end=' ')
    print(';', end=' ')
    for x, y in line:
        print(y, end=' ')
    print(';', end=' ')
    for x, y in line:
        print(0, end=' ')
    print()

    print('normal')
    for i in line_p:
        print(0, end=' ')
    print(';', end=' ')
    for i in line_p:
        print(90, end=' ')
    print()

if __name__ == '__main__':
    main()
