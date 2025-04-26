from more_itertools import sliced, substrings


def greet():
    print('Welcome to my application!')


if __name__ == "__main__":
    # Этот код будет выполнен только если файл запускается напрямую
    subs = ["".join(s) for s in substrings("more")]
    print(subs)

    slices = list(sliced((1, 2, 3, 4, 5, 6, 7, 8), 3))
    print(slices)

    greet()