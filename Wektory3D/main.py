from modules import Vectors


def fun(*args, **kwargs):
    print(args)
    print(kwargs)
    # if kwargs:
    #     print(True)
    # else:
    #     print(False)


if __name__ == '__main__':
    fun([1, 1, "2"], num=10)
