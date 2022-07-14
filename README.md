# Sudoku-Solver
1. First of all checking of an empty space (or a ‘0’) is done ( empcheck( ) )
 2. The position of empty space is assigned to pos1 [ i , j ] 
 3. For that empty space , a test number is sent (=num)
 4. Now ‘num’ is checked for all three conditions of Sudoku.


[ A ] : Sudoku Conditions Satisfied

 1. If all the three conditions are satisfied, num is assigned to the found empty space.
 2. After the assignment, the new Grid is passed on to the ‘Solve’ function again ‘RECURSIVELY’. (The values of previous ’Solve’ functions remain preserved in the respective blocks) I.e. num, pos1
 3. Now the further operations take place on this new Grid in the Recursively called new solve function without the Termination of Previous solved function.
 4. When all the positions have been filled, ’True’ is returned and the control moves one by one starting from the last ‘Solve’ function block to the very first ‘Solve’ function block.
 5. Now the control exits the first solve block and the Sudoku gets printed.

[B] : Sudoku Conditions not satisfied

 1. If the conditions are not satisfied, num is incremented by 1 (via for loop) and all three ’Sudoku’ conditions are checked again for the new value of ‘num’.
 2. If no value of num (1-9) satisfies the Sudoku conditions for that empty space then the control moves back to the preceding solve block and initialises the value at that place to zero. (Backtracking)
 3. Now that the control has moved to the preceding solve block, the num’s  ‘for loop’  (which was left over due to recursive calling of solve function) continues from the value of num at which it left and the conditions are checked again.
