# Water Color Sort Solver (Brute Force)
Using a Brute Force method of randomized attempts on solving a water color sorter game configuration

This little script is written in a way to simulate a water color sorter game session. It can attempt to solve the session in a given configuration by brute force. So long as there is a solution it should eventually solve the puzzle and print out the solution steps.

# How To Use

1) encode the session colors as integers ( e.g. red: 1, green: 2, blue: 3 ect.). The numbers assigned to the colors are irrelevant but empty regions must have a value of -1. 
2) prepare a [config file](example_config.txt) with the encoded integers for the given session and current configuration of colors.
3) run the [solver python program](water_sort_puzzle_solver.py). certain parameters such as number of tries and path to the config file will be asked throgh the text interface once the program is running.
4) program terminates when the solution is found, in which case the solution steps would be printed from the current configuration to solution or the number of tries limitation is reached, in which case "there doesn't seem to be a solution so far" is printed.

program should perform properly for any configuration which has greater than 2 vials and 1 depth.

# Online Implementation

The online implementations of the script will be deployed in the near future

# Future Plans
- A numpy version of the script will be implemented.
- A genetic algorithm can be applied to the script to optimize performance and number of iterations to reach a solution.
- A function can be added which takes a config file with strings (such as `[empty,blue,red,red]`) and converts it into number encoded colors automatically.
- A module which takes images as input and outputs the encoded config file could be implemented in the future.
