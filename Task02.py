def mirroring_numbers(ls):

    l = len(ls)
    

    for i in range(l // 2):
        if ls[i] != ls[-1 - i]:
            msg = "Числа в списке не зеркальны"
    else:
            msg = "Числа в списке зеркальны"

    return msg


def main():
    ls = [1, 2, 3, 2, 1]
    mirror = mirroring_numbers(ls)
    msg = f"{mirror}"

    print(msg)


if __name__ == "__main__":
    main()

