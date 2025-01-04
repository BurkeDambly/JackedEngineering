"Check"
def rec(num):

    if num == 0:
        return 0
    else:
        return 1 + rec(num - 1)
    

if __name__ == "__main__":
    print(rec(100))