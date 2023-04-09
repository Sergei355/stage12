def check_sequence(ls):

    for i in ls:
        if ls[i] < ls[i + 1]:
            msg = "образует возрастающую последовательность"
            break
    else:
        msg = " не образуют возрастающую последовательность"

    return msg


def main():
    ls = [1, 2, 3, 4, 5, 6, 7]
    check = check_sequence(ls)
    msg = f"Вектор {check}"
    print(msg)




if __name__ == "__main__":
    main()
