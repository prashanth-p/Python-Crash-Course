import sys
import time
print(sys.version)

# Using decorators


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000000) +
              " micro seconds to compute result")
        return result
    return wrapper


@time_it
def square_num(x):
    result = []
    for each in x:
        result.append(each * each)
    return result


@time_it
def cube_num(x):
    result = []
    for each in x:
        result.append(each * each * each)
    return result


@time_it
def main():
    numbers = range(0, 501)
    result_cube = cube_num(numbers)
    print()
    result_square = square_num(numbers)
    # print(result_cube[-10:])
    print()
    # print(result_square[-10:])

if __name__ == '__main__':
    main()
