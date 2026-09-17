class Solution:
    def isPalindrome(self, s: str) -> bool:
        santized_s = ""
        for ch in s:
            if ord(ch) >= ord("a") and ord(ch) <= ord("z") or ord(ch) >= ord("A") and ord(ch) <= ord("Z") or ord(ch) >= ord("0") and ord(ch) <= ord("9"):
                santized_s+=ch
        string_len = len(santized_s)
        for index in range(string_len):
            if santized_s[index].lower() != santized_s[string_len-index - 1].lower():
                return False
        return True
