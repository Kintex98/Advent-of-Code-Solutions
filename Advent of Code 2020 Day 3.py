forest = open('Advent of Code 2020 Day 3.txt')
forest = forest.read()
forest = forest.replace('\n', '')
# Flattens the forest

forest_rows = [forest[k:k+31] for k in range (0, len(forest), 31)]
# Separates the forest in its many rows

def driving(x_slope, y_slope):
    trees = 0
    x = 0
    y = 0
    for point in forest_rows:
        if forest_rows.index(forest_rows[y]) % y_slope == 0:
            if x >= 31:
                x = x -31
            if point[x] == '.':
                x += x_slope
                y += 1
            elif point[x] == '#':
                x += x_slope
                y += 1
                trees += 1
        else:
            y += 1
    print(trees)

driving(3,1)
driving(1,1)
driving(5,1)
driving(7,1)
driving(1,2)
print(66*200*76*81*46)