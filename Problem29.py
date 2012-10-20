#!/usr/bin/python3\

answer = set()
for x in range(2, 101):
    for y in range(2, 101):
        answer.add(x**y)
print(str(len(answer)))
