import time

from main.service.WildcardMatcher import WildcardMatcher

if __name__ == '__main__':
    wildcard_matcher: WildcardMatcher = WildcardMatcher()
    input_data = input("please, enter a string ")
    pattern_data = input("please, enter a pattern ")
    start_time = time.time()
    wildcard_matcher.is_match(input_data, pattern_data)
    print(f'{wildcard_matcher.result}\nSeconds {time.time() - start_time}')