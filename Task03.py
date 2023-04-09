def equality_numbers(ls):

    for i in ls:
        if ls[i] == ls[i + 1]:
            msg = "Все числа вектора равны"
            break
    else:
        msg = "Числа вектора не равны"

    return msg


def main():
    ls = [2, 2, 2, 2, 2, 2, 2]
    equality = equality_numbers(ls)
    msg = f"{equality}"
    print(msg)




if __name__ == "__main__":
    main()
