# Task 1
# написати ф-ію з використанням рекурсії,
# яка перевірятиме чи передане слово поліндром


def palindrome(word: str, f_index: int = 0, s_index: int = 0) -> None:
    """If the result is: Could  be a palindrome, this word is a palindrome """

    s_index = len(word)

    if len(word) < 2:
        return

    if not word[f_index] == word[s_index - 1]:
        print(f"{word} - not a palindrome")
        return

    word = word[int(f_index+1): int(s_index-1)]
    print('Could  be a palindrome')

    palindrome(word, f_index, s_index)


print(palindrome('abba'))

# Task 1*
# щоб функція працювала з реченням


def palindrome_sentence(sent: str, f_index: int = 0, s_index: int = 0) -> None:
    """If the result is: Could  be a palindrome, this word is a palindrome """

    sent = sent.replace(" ", "")

    s_index = len(sent)

    if len(sent) < 2:
        return

    if not sent[f_index] == sent[s_index - 1]:
        print(f"{sent} - not a palindrome")
        return

    sent = sent[int(f_index+1): int(s_index-1)]
    print('Could  be a palindrome')

    palindrome_sentence(sent, f_index, s_index)


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
