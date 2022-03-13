# Dart Calculator 

This small python project was given to a student to learn the basic of python! During the breaks we would often play a round of darts!
The only problem would be we all sucked in calculating the score,I therefore imagine an exercise where one should create a CLI tool to keep track of the score!

The tool should do all the calculation be able to sum and do the double and triple calculation. It should also keep track of the scores and not allow a player to exceed it. 
Furthermore it should be idiotproof should someone type something wrong! 

This is a quick code I create to demonstrate what I want to see in the end. Please note I didnt know one should end up with a double so this soft will not enforce it (And thanks got otherwise our game will never end!)

## How to use it ? 
### Launching game
first to launch it use the following command ; 
 > python3 darts.py

or for a more complete esthetics *(and an object oriented code)*
 > python3 Darts_object.py

### play
Answer the questions of the program.(number of player, game type etc.)  
To enter a score you can enter the computed score or just enter the position of each dart separate by a space for example 
> 12 20 15

you can announce double or triple with the letter D or T e.g.
> 12D T5 D10

should return 49 (12x2+3x5+2x10)
For Bull or even bull's eye you can use respectivly `BULL` and `EYE` key word (please note you cannot double or triple them) e.g.
>BULL EYE 10

returns 85 (25+50+2x10)