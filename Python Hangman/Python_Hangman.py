from pathlib import Path
import random
import os

absolute_path = os.path.dirname(__file__)
relative_path = "input/justwords.txt"
full_path = os.path.join(absolute_path, relative_path) # path for input file


# Returns partial set of words determined by chosen difficulty
def getPartial(partial,words,length,min,max):
    found_min = False
    found_max = False

    min_index = -1
    max_index = -1
    word_length = 0
    

    count = 0
    while found_min == False and count < length:
        word_length = len(words[count])
        if word_length == min:
            found_min = True
            min_index = count
        count = count + 1

    while found_max == False and count < length:
        word_length = len(words[count])
        if word_length > max:
            found_max = True
            # - 1 since endpoint
            max_index = count - 1
        elif count == length - 1:
            found_max = True
            max_index = count
        count = count + 1

    for i in range(min_index,max_index + 1):
        partial.append(words[i])




# merge subroutine for mergesort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if len(L[i]) <= len(R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 


def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
def displayNoose(attempts):

    print("c=======")
    print("||    :")
    print("||    :")
    print("||    :")

    if attempts == 0:
        print("||")
        print("||")
        print("||")
        print("||")
    elif attempts == 1:
        print("||    O")
        print("||")
        print("||")
        print("||")
    elif attempts == 2:
        print("||    O")
        print("||    |")
        print("||")
        print("||")
    elif attempts == 3:
        print("||    O")
        print("||   /|")
        print("||")
        print("||")
    elif attempts == 4:
        print("||    O")
        print("||   /|\\")
        print("||")
        print("||")
    elif attempts == 5:
        print("||    O")
        print("||   /|\\")
        print("||   / ")
        print("||")
    elif attempts == 6:
        print("||    O")
        print("||   /|\\")
        print("||   / \\")
        print("||")


words = []
partial = []
dif1 = "Easy"
dif2 = "Medium"
dif3 = "Hard"
print("Loading . . .\n")

with open(full_path,'r', encoding="ANSI") as dictFile:
    words = dictFile.read().splitlines()
dictFile.close()

length = len(words)

mergeSort(words, 0, length-1)

print("%s: 1 - 7"%dif1)
print("%s: 8 - 14"%dif2)
print("%s: 15 - 21"%dif3)

print ("Enter Difficulty (Easy, Medium, or Hard)")


valid = False

# Determining set of words to use based on diffuculty chosen
while valid == False:
    a_formatted = input().capitalize()
    if (a_formatted == dif1):
        getPartial(partial,words,length,1,7)
        valid = True
    elif (a_formatted == dif2):
        getPartial(partial,words,length,8,14)
        valid = True
    elif (a_formatted == dif3):
        getPartial(partial,words,length,15,21)
        valid = True
    else:
        print("Incorrect input!")


word = partial[random.randint(0, len(partial))]
word_length = len(word)
dashes = []
max_attempts = 6
attempts = 0

for x in range(word_length):
    dashes.append("-")

victory = False
try_bin = []

while victory != True and attempts < max_attempts:

    found_indices = []

    print("%s (%d)"%(''.join(dashes),word_length))
    displayNoose(attempts)
    print(' '.join(try_bin))

    guess = input()

    if guess == word:
        victory = True
    elif len(guess) == 1:
        try_bin.append(guess)
        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    found_indices.append(i)
            for x in found_indices:
                dashes[x] = guess
        else:
            attempts=attempts+1
    else:
        attempts = attempts + 1

print(word)
 





