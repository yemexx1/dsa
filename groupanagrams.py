class Solution(object):
    def groupAnagrams(self, strs):
        alphabet_dicto = {'a': 2, 'c': 5, 'b': 3, 'e': 11, 'd': 7, 'g': 17, 'f': 13, 'i': 23, 'h': 19, 'k': 31, 'j': 29,
                          'm': 41,
                          'l': 37, 'o': 47, 'n': 43, 'q': 59, 'p': 53, 's': 67, 'r': 61, 'u': 73, 't': 71, 'w': 83,
                          'v': 79, 'y': 97,
                          'x': 89, 'z': 101}

        output_dict = {}
        for string in strs:
            j = 0
            product = 1
            while j < len(string):
                product *= alphabet_dicto[string[j]]
                j += 1
            if not output_dict.has_key(product):
                output_dict[product] = [string]
            else:
                output_dict[product].append(string)

        return output_dict.values()

    def generateDicto(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        primes = [2, 3, 5, 7]
        for i in range(10, 102):
            if len(primes) == len(alphabet):
                break

            is_prime = True
            for prime in primes:
                if i % prime == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(i)

        alphabet_dicto = {}
        i = 0
        for prime in primes:
            alphabet_dicto[alphabet[i]] = prime
            i += 1
        return alphabet_dicto


solution = Solution()
print solution.groupAnagrams(["has","rod","tom","hum","him","yon","met","dye"])
