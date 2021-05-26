

def spiral_copy(inputMatrix):
    left = 0
    right = len(inputMatrix[0])-1
    low = 0
    high = len(inputMatrix)-1
    direction = 0  # 0->right, 1->down, 2->left, 3->up
    result = []
    while high >= low and left <= right:
        if direction == 0:
            # right
            result.extend(inputMatrix[low][left:right+1])
            low += 1
            direction = (direction+1) % 4
        elif direction == 1:
            # down
            for i in range(low, high+1):
                result.append(inputMatrix[i][right])
            # result.extend(inputMatrix[low:high][right])
            right -= 1
            direction = (direction+1) % 4
        elif direction == 2:
            # left
            result.extend(inputMatrix[high][right:left:-1])
            direction = (direction+1) % 4
        elif direction == 3:
            # up
            for i in range(high, low-1, -1):
                result.append(inputMatrix[i][left])
            # result.extend(inputMatrix[high:low-1:-1][left])
            high -= 1
            left += 1
            direction = (direction+1) % 4
    return result


# [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
inputMatrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
print spiral_copy(inputMatrix)
