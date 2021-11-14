def my_compare(str1, str2):
    if str1 < str2:
        return -1
    elif str1 == str2:
        return 0
    elif str1 > str2:
        return 1


def is_char_in(string, char):
    if char in string:
        return True
    else:
        return False


def is_char_not_in(string, char):
    if char not in string:
        return True
    else:
        return False


def my_count(string, char):
    count = 0
    for character in string:
        if character == char:
            count += 1
    return count


def my_endswith(string, char):
    if string[len(string) - 1] == char:
        return True
    else:
        return False


def my_find(string, char):
    if char not in string:
        return -1
    else:
        for character in range(len(string)):
            if string[character] == char:
                return character


def my_replace(string, char1, char2):
    replaced_string = ''
    for character in range(len(string)):
        if string[character] == char1:
            replaced_string += char2
        else:
            replaced_string += string[character]
    return replaced_string


def my_upper(string):
    uppercase_string = ''
    for character in string:
        if 97 <= ord(character) < 123:
            uppercase_string += chr(ord(character) - 32)
        else:
            uppercase_string += character
    return uppercase_string


def my_lower(string):
    lowercase_string = ''
    for character in string:
        if 65 <= ord(character) < 91:
            lowercase_string += chr(ord(character) + 32)
        else:
            lowercase_string += character
    return lowercase_string


# Extra Credit
def my_title(string):
    titlecase_string = ''
    next_char_new_word = False
    for character in range(len(string)):
        if character == 0:  # For the first letter, always uppercase
            if 97 <= ord(string[character]) < 123:
                titlecase_string += chr(ord(string[character]) - 32)
            else:
                titlecase_string += string[character]
        elif ord(string[character]) == 32:  # Space
            titlecase_string += string[character]
            next_char_new_word = True
        elif next_char_new_word:  # If it's a new word, as determined by the previous character which should've been
            # a space, check to see if the current character is lowercase; if so, uppercase
            if 97 <= ord(string[character]) < 123:
                titlecase_string += chr(ord(string[character]) - 32)
                next_char_new_word = False
            else:
                titlecase_string += string[character]
                next_char_new_word = False
        elif 65 <= ord(string[character]) < 91:  # If character is uppercase, lowercase by default
            titlecase_string += chr(ord(string[character]) + 32)
        else:
            titlecase_string += string[character]
    return titlecase_string


def main():
    check_my_compare = input('Check my_compare? [y/N] ')
    if check_my_compare == 'Y' or check_my_compare == 'y':
        my_compare_str1 = input('Enter the first string to compare: ')
        my_compare_str2 = input('Enter the second string to compare: ')
        print(str(my_compare(my_compare_str1, my_compare_str2)))

    check_is_char_in = input('Check is_char_in? [y/N] ')
    if check_is_char_in == 'Y' or check_is_char_in == 'y':
        is_char_in_string = input('Enter the string to check if a character is present: ')
        is_char_in_char = input('Enter the character to check within the string: ')
        print(str(is_char_in(is_char_in_string, is_char_in_char)))

    check_is_char_not_in = input('Check is_char_not_in? [y/N] ')
    if check_is_char_not_in == 'Y' or check_is_char_not_in == 'y':
        is_char_not_in_string = input('Enter the string to check if a character is not present: ')
        is_char_not_in_char = input('Enter the character to check within the string: ')
        print(str(is_char_not_in(is_char_not_in_string, is_char_not_in_char)))

    check_my_count = input('Check my_count? [y/N] ')
    if check_my_count == 'Y' or check_my_count == 'y':
        my_count_string = input('Enter the string to check the count of a character: ')
        my_count_char = input('Enter the character to check how many times it appears in the string: ')
        print(str(my_count(my_count_string, my_count_char)))

    check_my_endswith = input('Check my_endswith? [y/N] ')
    if check_my_endswith == 'Y' or check_my_endswith == 'y':
        my_endswith_string = input('Enter the string to check if it ends with a specific character: ')
        my_endswith_char = input('Enter the character to check if the string ends with it: ')
        print(str(my_endswith(my_endswith_string, my_endswith_char)))

    check_my_find = input('Check my_find? [y/N] ')
    if check_my_find == 'Y' or check_my_find == 'y':
        my_find_string = input('Enter the string to find where a character is in it: ')
        my_find_char = input('Enter the character to find where in the string it is: ')
        print(str(my_find(my_find_string, my_find_char)))

    check_my_replace = input('Check my_replace? [y/N] ')
    if check_my_replace == 'Y' or check_my_replace == 'y':
        my_replace_string = input('Enter the string to perform find and replace on: ')
        my_replace_char1 = input('Enter the character to find: ')
        my_replace_char2 = input('Enter the character to replace all instances of the first with: ')
        print(my_replace(my_replace_string, my_replace_char1, my_replace_char2))

    check_my_upper = input('Check my_upper? [y/N] ')
    if check_my_upper == 'Y' or check_my_upper == 'y':
        my_upper_string = input('Enter the string to uppercase: ')
        print(my_upper(my_upper_string))

    check_my_lower = input('Check my_lower? [y/N] ')
    if check_my_lower == 'Y' or check_my_lower == 'y':
        my_lower_string = input('Enter the string to lowercase: ')
        print(my_lower(my_lower_string))

    # Extra Credit
    check_my_title = input('Check my_title? [y/N] ')
    if check_my_title == 'Y' or check_my_title == 'y':
        my_title_string = input('Enter the string to titlecase: ')
        print(my_title(my_title_string))


main()
