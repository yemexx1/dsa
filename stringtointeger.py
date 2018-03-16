class Solution(object):
    def myAtoi(self, str):
        int_max = 2147483647
        int_min = 2147483648
        stripped_str = str.strip()

        i = 0
        place = len(stripped_str) - 1
        number = 0
        integer_list = '1 2 3 4 5 6 7 8 9 0'.split(' ')
        is_negative = False
        encountered_string = ''
        encountered_numbers = 0
        while i < len(stripped_str):
            if stripped_str[i] in integer_list:
                if len(encountered_string) > 0:
                    if encountered_string == '-' or encountered_string == '+':
                        return 0
                    else:
                        return str

                encountered_numbers += 1
                to_add = int(stripped_str[i]) * pow(10, place)
                has_passed_negative_boundary = int_min - number < to_add
                has_passed_positive_boundary = int_max - number < to_add
                if (not is_negative and has_passed_positive_boundary) or (
                            is_negative and has_passed_negative_boundary):
                    if is_negative:
                        number = int_min
                    else:
                        number = int_max
                    break
                else:
                    number += to_add

            elif stripped_str[i] == '-' and i == 0:
                is_negative = True

            elif stripped_str[i] == '+' and i == 0:
                is_negative = False
            elif encountered_numbers >= 1:
                number /= pow(10, len(stripped_str) - i)
                break
            else:
                encountered_string += stripped_str[i]

            place -= 1
            i += 1

        if is_negative:
            number *= -1

        if encountered_string == '-' or encountered_string == '+':
            return 0

        if encountered_numbers == 0 and len(encountered_string) > 0:
            return str

        return number


solution = Solution()
print solution.myAtoi("-1")
