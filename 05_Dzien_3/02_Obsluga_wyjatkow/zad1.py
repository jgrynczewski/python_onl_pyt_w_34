# # LBYL
# def safe_get(l, index):
#     if index >= len(l):
#         return None
#
#     return l[index]
#
#
# res = safe_get([1,2,3,4,5], 5)
# print(res)

# EAFP
def safe_get(l, index):
    try:
        return l[index]
    except IndexError:
        return None


res = safe_get([1,2,3,4,5], 9999)
print(res)
