class Solution:
    def isValid(self, s: str) -> bool:
        validation_stack= []
        mapping= {
            "[": "]",
            "(": ")",
            "{": "}"
        }
        for ch in s:
            print(ch)
            if ch in ("(","{", "[" ):
                validation_stack.append(ch)
            elif ch in (")","}", "]" ):
                print(ch, validation_stack)
                if not validation_stack:
                    return False
                o = validation_stack.pop()
                print("o", o)
                if mapping.get(o) != ch:
                    return False
        if validation_stack:
            return False
        return True
        
            



