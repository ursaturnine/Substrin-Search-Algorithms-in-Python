

class RabinKarp:

    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text

        # the size of the alphabet
        self.d = 26

        # prime number for the % operator
        self.q = 31
    
    def search(self):

        m = len(self.pattern)
        n = len(self.text)

        # hashes for region of the text and pattern
        hash_text = 0
        hash_pattern = 0

        # the largest polynomial term in the integer function
        h = 1


        for _ in range(m-1):
            h = (h * self.d) % self.q
        
        # pre-computer the hash of the pattern O(M) -Robin Karp fingerprint function
        for i in range(m):
            # ord() transforms letter into ASCII representation
            hash_pattern = (self.d * hash_pattern + ord(self.pattern[i])) % self.q
            hash_text = (self.d * hash_text + ord(self.text[i])) % self.q
        
        # slide the pattern over the text 1-by-1 -Rolling hash function
        for i in range(n-m + 1):

            # check the hash values of current window  of text
            # and pattern. If the hash values match then only 
            # check for characters one-by-one
            if hash_text == hash_pattern:

                # naive approach to check the characters
                j = 0

                while j < m:
                    if self.text[i + j ] != self.pattern[j]:
                        break
                    
                    j += 1
                
                if j == m:
                    print('Found match at index %s' % i)
                
            # update the hash for the actual substring of the text
            # apply the rolling hash approach
            if i < n-m:
                hash_text = ((hash_text - ord(self.text[i]) * h) * self.d + ord(self.text[i + m])) % self.q

                # we might get negative value so we have to make sure the hash is positive
                if hash_text < 0:
                    hash_text += self.q
            



if __name__ == '__main__':

    algorithm = RabinKarp('test', 'this is a test')
    algorithm.search()



