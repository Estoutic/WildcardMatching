def is_match(data: str, pattern: str) -> bool:
    split_data: list = list(data)
    split_pattern: list = list(pattern)
    result: bool

    if '*' not in pattern:

        if len(split_data) == len(split_pattern):
            for index in range(len(split_pattern)):
                if split_pattern[index] != split_data[index] and split_pattern[index] != "?":
                    return False
        if split_pattern == split_data:
            return True
        else:
            return False
    else:

        count_of_characters = split_pattern.count("*")

        while count_of_characters != 0:

            pattern_index = split_pattern.index('*') + 1
            start_index = split_pattern.index('*') + 1

            for index in range(split_pattern.index("*") - 1):

                if split_pattern[index] != split_data[index] and split_pattern[index] != '?':
                    return False

            if len(split_data) - pattern_index + 1 != len(split_pattern) and count_of_characters == 0:
                return False

            if split_pattern.count("*") == len(split_pattern) or split_pattern.index('*') == len(split_pattern) - 1:
                return True

            if split_pattern[split_pattern.index('*') + 1] == '?':
                count_of_characters -= 1

            else:
                if start_index == 1:
                    start_index = 0
                    if split_data[start_index] == split_pattern[split_pattern.index("*") + 1]:
                        split_data = split_data[(start_index + 1):]
                        split_pattern = split_pattern[(split_pattern.index("*") + 1):]
                        count_of_characters -= 1
                if count_of_characters != 0:
                    while split_data[start_index] != split_pattern[split_pattern.index("*") + 1]:

                        start_index += 1

                        if start_index != len(split_data):
                            if split_data[start_index] == split_pattern[split_pattern.index("*") + 1]:
                                split_data = split_data[(start_index):]
                                split_pattern = split_pattern[(split_pattern.index("*") + 1):]
                                count_of_characters -= 1
                                break

        return True
# 123ab456cd
# ?23*4?*?
