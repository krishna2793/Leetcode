import operator
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #print(string.punctuation)
        words = re.sub('['+string.punctuation+']',' ', paragraph).split()
        words = [word.lower() for word in words]
        freq = {}
        for word in words:
            if word not in banned:
                if word not in freq:
                    freq[word] = 0
                else:
                    freq[word]+=1
        return max(freq.items(), key = operator.itemgetter(1))[0]