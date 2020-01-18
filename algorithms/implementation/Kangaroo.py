import os


def kangaroo(x1, v1, x2, v2):
    jumps = 0

    while jumps < 10000:
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"

        jumps += 1

    return "NO"


# Include IO from STDIN / STDOUT
if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inp = input().split()
    res = kangaroo(int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3]))

    fptr.write(res + '\n')
    fptr.close()
