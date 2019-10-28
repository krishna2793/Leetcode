class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}
        def match(freq,word,n):
            if len(word) > n:
                return 0
            freqCpy = freq.copy()
            for c in word:
                if (c not in freqCpy) or (freqCpy[c] == 0):
                    return 0
                else:
                    freqCpy[c] -= 1
            return len(word)
            
                
                        
        n = 0
        for c in chars:
            n+=1
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        total = 0
        for word in words:
            total += match(freq,word,n)
        return total