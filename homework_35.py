# Task 1
# написати ф-ію з використанням рекурсії,
# яка перевірятиме чи передане слово поліндром


def palindrome(word: str) -> None:
    """If the result is: Could  be a palindrome, this word is a palindrome """

    if len(word) < 2:
        return

    if not word[0] == word[len(word) - 1]:
        print(f"{word} - not a palindrome")
        return

    word = word[int(1): int(len(word)-1)]
    print('Could  be a palindrome')

    palindrome(word)


#print(palindrome('abbsfgsa'))

# Task 1*
# щоб функція працювала з реченням


def palindrome_sentence(sent: str) -> None:
    """If the result is: Could  be a palindrome, this word is a palindrome """

    sent = sent.replace(" ", "")

    if len(sent) < 2:
        return

    if not sent[0] == sent[len(sent) - 1]:
        print(f"{sent} - not a palindrome")
        return

    sent = sent[int(1): int(len(sent)-1)]
    print('Could  be a palindrome')

    palindrome_sentence(sent)


print(palindrome_sentence('evil olive'))


# Task 2
# написати ф-ію з використанням рекурсії,
# яка повертатиме суму усіх чисел в списку


def ordinary_list(list_of_n: list):
    new = []
    while list_of_n:
        e = list_of_n.pop()
        if type(e) == list:
            list_of_n.extend(e)
        else:
            new.append(e)
    return new


def add_func(list_of: list, index: int = 0, all_sum: int = 0) -> None:

    if len(list_of) - 1 < index:
        print(all_sum)
        return

    if type(list_of[index]) == int:
        all_sum += list_of[index]

    add_func(list_of, index + 1, all_sum)


num = ordinary_list([2, 3, [1, 2], [4, 5, [10, 1]]])

print(add_func(num))
