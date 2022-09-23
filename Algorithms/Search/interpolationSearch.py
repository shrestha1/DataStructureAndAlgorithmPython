def interpolationSearch(list:list, n:int or float):
    found = False
    idx0 = 0
    idxn = len(list)-1
    #using the concept of interpolation
    # mid - x0 = (x1 - x0)/(y1 - y0)*(n - y0)
    while idx0 <= idxn:
        mid = idx0 + int(((idxn - idx0)/(list[idxn] - list[idx0])) * (n - list[idx0]))
        if list[mid] == n:
            return True
        if list[mid] < n:
            idx0 = mid + 1
    return False


if __name__ == '__main__':
    list = [1, 2 , 3, 4, 5, 6, 7,8]
    print(interpolationSearch(list, 3))
