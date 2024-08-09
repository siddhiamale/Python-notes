# WAP to check if the given strings are anagram or not

def strings(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("strings are anagram")
    else:
        print("strings are not anagram")

strings("listen","silent")    