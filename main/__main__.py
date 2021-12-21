from main.service.WildcardMatcher import WildcardMatcher

if __name__ == '__main__':
    wildcard_matcher: WildcardMatcher = WildcardMatcher()
    wildcard_matcher.is_match("cb", "??")