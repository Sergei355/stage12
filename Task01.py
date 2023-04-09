def reads_even_numbers(ls):

    count = 0

    for i in ls:
        if i % 2 == 0:
            count += 1

    return count


def main():
    ls = [1, 4, 7, 56, 73, 94, 100]
    even_numbers = reads_even_numbers(ls)
    msg = f"Четные числа в векторе составляют {even_numbers} шт"
    print(msg)




if __name__ == "__main__":
    main()