class WildcardMatcher:

    def is_match(self, data: str, pattern: str) -> bool:
        split_data: list = list(data)
        split_pattern: list = list(pattern)
        if '*' not in pattern:
            if len(split_data) == len(split_pattern):
                count_of_single = split_pattern.count("?")
                if count_of_single != 0:
                    while count_of_single != 0:
                        split_pattern[split_pattern.index("?")] = split_data[split_pattern.index("?")]
                        count_of_single -= 1
                identified_char = True
                for index in range(len(split_pattern)):
                    if split_pattern[index] != split_data[index]:
                        identified_char = False
                        break

                if not identified_char:
                    print(False)
                else:
                    print(True)
            else:
                print(False)

        else:
            count_of_characters = split_pattern.count("*")
            while count_of_characters != 0:
                identified_char = None
                for index in range(split_pattern.index("*") + 1):
                    if split_pattern[index] != split_data[index]:
                        if split_pattern[index] != '?':
                            identified_char = False
                            break
                if not identified_char:
                    print(False)
                    break
                start_index = split_pattern.index("*")
                if len(split_pattern) != 1 and split_pattern.index("*") != len(split_pattern) - 1:
                    while split_data[start_index] != split_pattern[split_pattern.index("*") + 1]:
                        start_index += 1
                        if start_index > len(split_data) - 1:
                            print(False)
                            count_of_characters -= 1
                            break
                else:
                    print(True)
                    break


