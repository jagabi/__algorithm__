def solution(phone_book):
    hashmap = {}
    for num in phone_book:
        hashmap[num] = 1
    for nums in phone_book:
        tmp = ""
        for num in nums:
            tmp += num
            if tmp in hashmap and tmp != nums:
                return False
    return True