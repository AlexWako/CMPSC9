from Stack import Stack

def solveMaze(maze, startX, startY):
    stepTaken = Stack()
    
    # Intializing the first position
    position = 1
    stepTaken.push([startX, startY])
    X = stepTaken.peek()[0]
    Y = stepTaken.peek()[1]
    maze[X][Y] = position

    # Navigating through the maze
    while stepTaken.isEmpty() == False: 
        # Checks to see if any of the surrounding is open
        if maze[X - 1][Y] == ' ':
            stepTaken.push([X - 1, Y])
        elif maze[X][Y - 1] == ' ':
            stepTaken.push([X , Y - 1])
        elif maze[X + 1][Y] == ' ':
            stepTaken.push([X + 1, Y])
        elif maze[X][Y + 1] == ' ':
            stepTaken.push([X, Y + 1])
        # Checks to see if any of the surrounding is a G
        elif maze[X - 1][Y] == 'G':
            return True
        elif maze[X][Y - 1] == 'G':
            return True
        elif maze[X + 1][Y] == 'G':
            return True
        elif maze[X][Y + 1] == 'G':
            return True
        elif stepTaken.size() > 1:
            stepTaken.pop()
            X = stepTaken.peek()[0]
            Y = stepTaken.peek()[1]
            continue
        else:
            break

        # Changes the position 
        position += 1
        X = stepTaken.peek()[0]
        Y = stepTaken.peek()[1]
        maze[X][Y] = position

    # No possible paths
    return False


