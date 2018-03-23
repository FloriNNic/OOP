class Partitions():
    def __init__(self):
        self.x = [0 for i in range(1, 10)]

    def generatePartitions(self, i, s): # a recursive method to generate the strict partitions of n
        for j in range(self.x[i - 1] + 1, s + 1):
            self.x[i] = j
            if self.x[i] == s:
                for k in range(1, i):
                    print(self.x[k], '+', end=' ')
                print(self.x[i])
            else: self.generatePartitions(i + 1, s - self.x[i])

class Palindrome():
    def isPalindrome(self, i): # returns true if a number is a palindrome, false otherwise
        inv = 0                # this time i didn't convert the number into a string
        aux = i
        while aux != 0:
            inv = inv * 10 + aux % 10
            aux = aux // 10

        if inv == i:
            return True
        else:
            return False

    def findPalindrome(self, n): # finds the n-th palindrome number
        number = 1
        i = 1
        while number <= n:
            if self.isPalindrome(i):
                number = number + 1
            i = i + 1
        return i - 1

class Subsets():
    def __init__(self, number):
        self.result = []
        self.number = number

    def generateSubsets(self, number):
        result = []
        a = [0 for i in range(number + 1)]
        k = 1
        a[1] = number
        while k != 0:
            x = a[k - 1] + 1
            y = a[k] - 1
            k = k - 1
            while x < y:
                a[k] = x
                y = y - x
                k += 1
            a[k] = x + y
            ok = 1
            for i in range(0, k):
                for j in range(i + 1, k + 1):
                    if a[i] == a[j]:
                        ok = 0

            if ok == 1:
                result.append(a[:k + 1])
        return result

class Display():
    def displayTriangle(self,n):
        for i in range (0,n):
            for j in range (0,i):
                print(n,end=' ')
            print('\n')