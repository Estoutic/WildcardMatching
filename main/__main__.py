import time

from main.service.WildcardMatcher import is_match

if __name__ == '__main__':
    input_data = input("please, enter a string ")
    pattern_data = input("please, enter a pattern ")
    start_time = time.time()
    print(f'{is_match(input_data, pattern_data)}\nSeconds {time.time() - start_time}')