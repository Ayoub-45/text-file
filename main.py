# Step 1: Create a text file with user-provided words
def create_file(filename):
    print("Enter words line by line. Type 'DONE' to stop.")
    with open(filename, 'w') as file:
        while True:
            word = input("Enter a word: ")
            if word.strip().upper() == "DONE":
                break
            file.write(word + '\n')
    print(f"{filename} created successfully!")

# Step 2: Read the file and build a list of words
def read_file_to_list(filename):
    with open(filename, 'r') as file:
        words = [line.strip() for line in file.readlines()]
    print("Words loaded into a list.")
    return words

# Step 3: Verify if the list is sorted
def is_sorted(word_list):
    return word_list == sorted(word_list)

# Step 4: Search for a word in the list
def search_word(word_list, word):
    try:
        position = word_list.index(word)
        print(f"Word '{word}' found at position {position}.")
        return position
    except ValueError:
        print(f"Word '{word}' not found.")
        return -1

# Step 5: Merge sort implementation
def merge_sort(word_list):
    if len(word_list) > 1:
        mid = len(word_list) // 2
        left_half = word_list[:mid]
        right_half = word_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                word_list[k] = left_half[i]
                i += 1
            else:
                word_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            word_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            word_list[k] = right_half[j]
            j += 1
            k += 1

# Step 6: Save sorted list back to the file
def save_list_to_file(word_list, filename):
    with open(filename, 'w') as file:
        for word in word_list:
            file.write(word + '\n')
    print(f"Sorted words saved back to {filename}.")

# Step 7: Binary search
def binary_search(word_list, word):
    low, high = 0, len(word_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if word_list[mid] == word:
            print(f"Word '{word}' found at position {mid}.")
            return mid
        elif word_list[mid] < word:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Word '{word}' not found.")
    return -1

# Step 8 & 9: Worst-case costs
def search_costs():
    print("Worst-case cost of non-binary search: O(n)")
    print("Worst-case cost of binary search: O(log n)")

# Main execution
filename = "words.txt"
create_file(filename)
word_list = read_file_to_list(filename)

if is_sorted(word_list):
    print("The list is already sorted.")
else:
    print("The list is not sorted. Sorting now...")
    merge_sort(word_list)
    save_list_to_file(word_list, filename)

word_to_search = input("Enter a word to search: ")
search_word(word_list, word_to_search)
binary_search(word_list, word_to_search)
search_costs()
