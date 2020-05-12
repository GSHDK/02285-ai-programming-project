# 02285-ai-programming-project
Programming project for DTU course 02285 Artificial Intelligence and Multi-Agent Systems


To run the program use the following code in the correct dir:

java -jar ./server.jar -l ./levels/MABlinky.lvl -c "python3 main.py"

A print statement should look like this:

print(f'Done with loading data', file=sys.stderr, flush=True)

and will print to the terminal where the command is executed


### Planning categories 
Initial logic. Agents will always help others and discard own assignments


* No task - 1
* Move out of way - 2
* Goal assigner - location 3
* Goal assigner - box 4
* Awaiting help - 5  
* Solving help task - 6
* Moving out of way for othr agent - 7


