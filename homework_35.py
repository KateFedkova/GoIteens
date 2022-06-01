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


print(palindrome('abbsfgsa'))

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


def add_func(list_of: list, all_sum: int = 0):

    for i in list_of:
        if type(i) == list:
            all_sum += add_func(i)
        else:
            all_sum += i

    return all_sum


print(add_func([2, 3, [1, 2], [4, 5, [10, 1]]]))
