Brief Description

“Jojo’s Bizarre Adventure: Heritage of the future” is a popular arcade style action fighting game in gaming consoles and has made its way to one of the most popular fighting games, with it’s games, Jojo’s bizarre adventure had also developed a very popular action-style show series. Jojo’s Bizarre Adventure was the last popular fighting game which had not switched to 3D style yet and kept its 2D fighting style unlike their competitors with high definition 3D graphics in the Playstation 3 era. I personally enjoy playing quick-paced fighting games and have memories of playing Jojo’s Bizarre Adventure in the old eras of the Playstation 2 and 3. 

In a typical fighting game (in story/single player mode), a player would be fighting a bot in a 1 versus 1 match and the last man/bot standing wins, the game i have attempted in making for this project suits that category and shares the same theory as that. For this game, I have tried to make my own small copy of Jojo’s Bizarre Adventure: Heritage Of The Future, the similarity they share are the characters and some attack moves of the characters. 

This game contains three attacks for the boss and three attacks for the player, whereas the player gets a special ultimate attack.




-
-
-
-
-
-
-


Use-Case Diagram:

![image](https://user-images.githubusercontent.com/114371673/213071100-e52c69ee-5efb-4284-bcb8-5c827de3e1a0.png)

When the user launches the game, they will see the start screen wherein they can move around the player sprite and click to play the game. Once they play the game, the outcome will be the only result to either the player or the bot reaching 0 HP, when that outcome happens, they will be directed to the game over screen where they will see a message on the screen, if mouse clicked: it will exit the program.

-
-
-
-
-
-
-
-
-

Activity Diagram:

![image](https://user-images.githubusercontent.com/114371673/213071191-5a345c60-6a52-47d0-97bd-3a8e9f82aa9e.png)

-
-
-
-
-
-
-
-
-
-
-

Class Diagram:

![image](https://user-images.githubusercontent.com/114371673/213071354-6e81deec-4168-4fcb-b0ea-397779cab3fc.png)

The Arrows Connecting Represents The “Belongs To” Factor. Ora, Attack1, Attack2 belongs to Boss & pygame. Bullet, muda, Knives belongs to Player and pygame. Whereas Boss and Player belongs to Pygame. In the pygame class diagram we can see all classes under pygame, and for the rest of the classes we can see the functions defined under them. For instance, the class “Player” have the functions of player_input, apply gravity, animation_state and update. 



-
-
-
-
-
-
-
-
-
Modules:

Pygame: 
			This module is the core of this 
			Game. Pygame is a module which
			Exists for providing multiple 
			Convenient libraries for 2D game 
			Creations. Pygame was used for
			Multiple things ranging from 
			Loading models to playing sound
			to making a whole window.

Random:
			This module serves the purpose of 
			Creating random integers in any
			way or form factor desired, this 
			Module was used for the move-
			ment mechanics and attacking
 			mechanics of the boss.

Sys: 
			This module was used for its 
			Function to exit the program using
			sys.exit(). This module might’ve 
			Been unnecessary since pygame
			May already have something 
			Similar, but i did use this out of 
			pure self-preference.





