# wrd = 'one'
# sec_wrd = 'toe'
# def unique_letters(x):
#     output =[]
#     for char in x:
#         if char not in output and char != " ":
#             output.append(char)
#     return output
#
# final_output = (unique_letters(wrd) + unique_letters(sec_wrd))
#
# print(sorted(final_output))

# wrd = 'one'
# sec_wrd = 'toe'
# wrd = set(wrd)
# sec_wrd = set(sec_wrd)
# print(''.join(sorted(wrd.intersection(sec_wrd))))


# def commonCharacterCount(s1, s2):
#     count = 0
#     l1 = sorted(list(s1))
#     l2 = sorted(list(s2))
#     for i in range(len(l1)):
#         if l1[0] in l2:
#             count += 1
#         del l1[0]
#         del l2[0]
#
#     return count
# print(commonCharacterCount('aabcc','adcaa'))

def commonCharacterCount(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)
print(commonCharacterCount('aabcc','adcaa'))