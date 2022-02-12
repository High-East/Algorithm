import sys

N = int(sys.stdin.readline())


def star(current=1, target=1, sample='*'):
    if current == target:
        return sample
    sample = '*'
    return star(current=current + 1, sample=sample)


star(target=N // 3)


sample = "***\n* *\n***"
sample.split('\n')

sample2 = f"{sample}{sample}{sample}"
print(sample, sample, sep='')

"**** ****"

sample = '*'
sample = [[sample for _ in range(3)] for _ in range(3)]
sample[1][1] = ' '
sample[1][1] = [[' ' for _ in range(3)] for _ in range(3)]


[sample[i] * 3 for i in range(3)]


for i in range(3):
    print(*sample[i])











