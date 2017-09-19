from collections import deque

def search(lines, pattern, history=5):
    pre_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, pre_lines
        pre_lines.append(line)


if __name__ == '__main__':
    with open('D:\python\workspace\learn-py\chapter-1\est.txt', 'r') as f:
        for line, prelines in search(f, 'python', 5):
            for pline in prelines:
                print(pline, end='')
            print(line, end='')
            print('_' * 20)