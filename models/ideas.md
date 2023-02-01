Primarily focused in playing agent vs agent
For the first version of the model we will use as input:

* A hash mapping of every card to a single value 
We can avoid this if we only take into account the reward system
    * The amount of money the player has
* The actual bet at this point in the turn
* The action of the other player (0 if no other action then 1-4)

The model for all versions will output the same 4 variables:

* raise bet
* fold
* check
* call

Reward System

* Bet Lost = -10
* Bet Won = 10
* Lost all money = -20