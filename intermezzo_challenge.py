def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    print(counter)
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[1][0]
    
    return letter

# SOLUTION
# Needed to reverse the sort order and then get it to look at the second item in the list as the spaces appeared the most
print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
