from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    t = True
    arr=[]
    if any(elements) != 0:
        arr.append(elements[0])
        for i in elements:
            if arr[0] == i:
                t = True
            else:
                return False
    return True

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
