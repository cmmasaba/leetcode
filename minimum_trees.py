def solution(trees: list) -> int:
    n = len(trees)
    min_trees = 0

    for i in range(n):
        left = i - 1
        right = i + 1
        sum_with_neighbours = (trees[i] + trees[left] if i > 0 else 0
                              + trees[right] if i < n - 1 else 0)
        
        if sum_with_neighbours < 0:
            if i > 0 and trees[left] + trees[i] < 0:
                min_trees += abs(trees[left] + trees[i])
                trees[left] += abs(trees[left] + trees[i])
            
            if i < n - 1 and trees[right] + trees[i] < 0:
                min_trees += abs(trees[right] + trees[i])
                trees[right] += abs(trees[right] + trees[i])
    
    print(trees)  
    return min_trees

def main():
    neighbourhoods = [[1, -3, 2], [-3, 2, 4, -5, 3], [-2, 1, -3, 1]]
    for item in neighbourhoods:
        print(solution(item))


if __name__ == '__main__':
    main()