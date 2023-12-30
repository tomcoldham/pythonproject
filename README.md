# Battleships game!

Welcome to my version of the infamous battleships game that i made using Python. It is a single player game against the computer where users will have to guess
the location of the battleships and sink them all before they run out of shots.

## Features

- The Premise of the game is simple, all you have to do is destroy all of the ships by correctly guessing the coordinates before you run out of shots.

- Certain precautions have been implemented into the game to make it consistent, for example an equation has been used so that the ammount of ships will be roughly 1/3 of the total number of squares. This consistency also translates to the ammount of shots each player has also depending on the difficulty.
  
- Users can choose their own map grid from 4-9 sqaures for a different experience, they also have the option to increase the difficulty from a choice of 3 different options. Beginner difficulty will have about 90% of the sqaures available as shots, intermediate will be 70% and then advanced will be 50%. The more shots a player has then the more chances they have at guesssing all the ship locations correctly thus winning the game.

- To give users feedback on the game, the total number of ships that need to be sunk is shown at the start of the game and the ammount of shots they have left is also shown each time they take a shot.

![ships](https://github.com/tomcoldham/pythonproject/blob/main/assets/pythongrid.PNG)

- Further user experience has been added with a live grid of the ships they have sunk, 'X' will display a location with a sunk ship. 'O' will be displayed with the location of a coordinate that was fired at but no ship was hit.

![shiphit](https://github.com/tomcoldham/pythonproject/blob/main/assets/pythonhit.PNG)

![shipmiss](https://github.com/tomcoldham/pythonproject/blob/main/assets/pythonmiss.PNG)

- The difference between the difficulty is the number of shots each player has. The more shots a player has then the more chances they have at guesssing all the ship locations correctly thus winning the game.

- A menu has also been implemented at the start of the game which gives players clear instructions on how to play the game also gives them the option to start the game or quit. Players can also quit out at any time during the game if they wish to do so.

![Menu](https://github.com/tomcoldham/pythonproject/blob/main/assets/pythonmenu.PNG)

## Testing

- Extensive testing has been done to make sure that the player cannot cause the game to crash or bug out, this has been done by making the input selective through out all of the project and also displaying helpful error messages when a player enters a command in wrong, for example entering a letter when a number is required for the coordinate of their guess.

![Input](https://github.com/tomcoldham/pythonproject/blob/main/assets/pythonerror.PNG)

- Additional input parameters have been added so that the player cannot guess the same coordinate, or cannot guess a number that isn't in the grid. 

![Repeat](https://github.com/tomcoldham/pythonproject/blob/main/assets/pythonrepeat.PNG)

- The game is functioning as intended and completes when it should for example when the player hits all the ships or if they run out of ammo.

![end](https://github.com/tomcoldham/pythonproject/blob/main/assets/pythonfail.PNG)

### Validator Testing

Code has been validated and no errors have been found, also found the code when deployed in heroku performs as expected.


![Testing](https://github.com/tomcoldham/pythonproject/blob/main/assets/validation.PNG)


### Unfixed Bugs

- No unfixed bugs were found in this project.

## Deployment

- The site was deployed to GitHub pages. And then launched from heroku The steps to deploy are as follows:
  - First i pushed everything to github.
  - Then i linked my github account to heroku.
  - I created a new app in Heroku and under 'deployment' i used 'connect to github'.
  - I searched for the name of the repository from github.
  - heroku then deployed a live version of my project.
  
The live link can be found here - https://tomc-codeinstitute-project3-8eca0d08e62e.herokuapp.com/

## Credits

### Content
- Some code has been inspired from other battleship games found online.
Though i have tried my upmost to keep the code original 
and add my own features into the game.

### Media

- No media was used for this project.
