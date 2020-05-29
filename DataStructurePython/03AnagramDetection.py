# Whether two Strings are anagrams, when reversed they are the same


class Main:

    def detection(str1, str2):
        ls = []
        for x in str1:
            ls.append(x)
        ls.reverse()
        temp = "".join(ls)
        print(temp)
        if temp == str2:
            return True
        else:
            return False

    if __name__ == "__main__":
        str1 = input("Enter a string:")
        str2 = input("Enter another string:")
        print(detection(str1, str2))
