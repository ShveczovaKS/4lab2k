#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(acc):
    if acc[0] < 0:
        return 0
    else:
        return acc[0] + f(acc[1:])


def ff(acc):
    if acc[0] < 0:
        return 0
    else:
        return 1 + ff(acc[1:])


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
    print(f(a))
    print(ff(a))
