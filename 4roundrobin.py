from time import time

# yield return control and freeze to next iteration

def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time()*1000)
        yield pattern.format(str(t))

        var = 12*12*12 - 73*11
        print(var)

# g = gen_filename()

def gen1(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(n):
        yield i

g1 = gen1('hzeh')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)

    except StopIteration:
        pass