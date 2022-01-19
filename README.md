# Advent-of-Code-2022
Great practice instead of leetcode for someone who has too much time

I would like to thank Jonathon Paulson and anthonywritescode for their very helpful solutions when I couldn't solve the problems :DD
* Also credit to Peedee for the first few days, your solutions were really elegant at times and much better cleaned up than mine!
* lastly credit to William Y Feng for the solution to day 24 which was super super elegant 🈸

I needed solutions on:
* day 16, day 19, day 22, day 24
and maybe more I'm forgetting about, but notice these days may have aspects of the above code written in it.

Hope you have fun reading my really really really inefficient solutions :') trying to get better 

Here, I'll keep a list of things I've learnt throughout the whole process.
* Overall, **how to use git on local** because the UNSW SSH servers keep crashing
* Day 25: The best way to create a copy of a 2d array is to use **list comprehension**. I tried copy() which didn't actually work to my frustration. Watching the pros do it made me realise that you could just keep a list of coordinates where there were slugs and just go off there. Much simpler!
    - Could've also used modulus to wrap around
* Day 23 and 24: Sometimes, hand-solving is the way to go. Solving it via a computer would've taken hours as there were 10^14 possible numbers. Maybe at that stage, you should have been looking for some alternate solution.
* Day 22: Using zip to store **intersections** as new cubes. Alternative solution, add a count dictionary :) 
* Day 21: Using dp properly: how to attain a score, at a certain player position. Since dual, use (score, pos, score2, pos2)
* Day 20: Store lit points as a set. Calculate before range and after range.
* Day 19: Two sets of good and bad. Using a **default dictionary** e.g. defaultdict(int). For every bad scanner, for every good scanner, for every permutation, try a position of a scanner and vote on it. Wow!
* Day 18: String manipulation > binary trees. isinstance(..., int) very helpful :)
* Day 17: literally a brute force solution
* Day 16: Digestable, but keep track of a function that returns an index of a global string.
* Day 15: A 4-way Dijkstra's Algorithm with Heap Q. Use heapq.heapify(pq). Coders love using d, e.g. dx, dy or dr, dc... Then have a dictionary with stored Dijkstra values.
* Day 14: The **counter class**. Couldn't realllly do this problem with not many hints.
* Day 12: Kinda overcomplicated the solution. But a standard DFS, keeping a visited array. DFS has to **backtrack** and remove one from visited at the end. Honestly you don't need recursion for this if you just have a suitable queue.
* Day 11: Didn't need to simultaneous update. Do an update later at the end. Keep track of which octopi have already flashed. G.append([int x for x in line.strip()]) easy way to parse files with integer arrays. **global** keyword at the start of a function allows you to access it. Directly updating the array wasn't a big problem as long as you could keep track of what had been updated or not. G[r][c] == -1 for example with three for loops and recursive flash function. 
* Day 9: DR = [-1, 0, 1, 0] , DC = [0, 1, 0, -1]. cc = c + DC[i], rr = r + DC[i]. If 0 <= cc < C (where C = len(grid)) fastest way. list.sort() easy sort. Could've done it many ways, or you can search from different low points (probably better).
* Day 8: itertools.permutation for all possible permutations.
* Day 7: median is the fastest for crab moving. med = X[len(X) // 2]
* Day 6: counter class.
* Day 5: min, max for easy direction handling. flatten() and transpose() are two useful numpy functions!
* Day 4: 3D array for boards and Board classes in Python :0 
* Day 3: list comprehension best way. Use the filter function if needed
* Day 1: list comprehension directly from input: [int(x) for x in inputList]

Will keep these techniques in mind for Competitions ;) 
