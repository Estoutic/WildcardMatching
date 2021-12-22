class WildcardMatcher:

    def __init__(self) -> None:
        super().__init__()
        self.result: bool = True

    def is_match(self, data: str, pattern: str):

        split_data: list = list(data)
        split_pattern: list = list(pattern)

        if '*' not in pattern:

            if len(split_data) == len(split_pattern):

                self.result = True

                for index in range(len(split_pattern)):
                    if split_pattern[index] != split_data[index] and split_pattern[index] != "?":
                        self.result = False
                        return
            else:
                self.result = False
        else:

            count_of_characters = split_pattern.count("*")
            while count_of_characters != 0:
                start_index = split_pattern.index('*') + 1
                for index in range(split_pattern.index("*") - 1):

                    if split_pattern[index] != split_data[index] and split_pattern[index] != '?':
                        self.result = False
                        return
                if start_index == len(split_data) - 1:
                    self.result = True
                    return
                else:
                    if split_pattern[split_pattern.index('*') + 1] == '?':
                        count_of_characters -= 1
                        self.result = True
                    else:
                        if split_data[start_index + 1] == split_pattern[split_pattern.index("*") + 1] or split_pattern[split_pattern.index("*") + 1] == '?':
                            count_of_characters -= 1
                            self.result = True

                        while split_data[start_index] != split_pattern[split_pattern.index("*") + 1]:

                            start_index += 1

                            if start_index > len(split_data) - 1:
                                self.result = False
                                return
