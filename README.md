# Border Scrutiny

"Border Scrutiny" is a game in which you play as a border guard, checking and making sure to accept or refuse people based on sensitive intel.

View the live site: [Border Scrutiny](https://border-scrutiny-32912c92d278.herokuapp.com)

![Home screen image of Border Scrutiny](./docs/features/home_screen.PNG)

## CONTENTS

* [Design](#design)
  * [Colours](#Colours)
  * [Art](#Art)
  * [Typography](#Typography)
  * [Flowchart](#Flowchart)

* [Features](#features)

## Design

### Colours

Colours used were done using ANSI code for which instructions can be found in the following link: [Colors](https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python)

### Art

To add some flare, ASCII Art was imported and used for introduction and end screen. [ASCII Art](https://pypi.org/project/art/)

<img src="./docs/features/home_screen.PNG" alt ="home screen" width="60%">

### Typography

Font family Russo One was used for heading, offering a more rugged look.


### Flowchart

The flowchart follows the logic of the game, how each process interacts with data.

The flowchart helps with manually testing game functionality.

<img src="./docs/flowchart/flowchart.png" alt ="flowchart">


## Features

We will go trough the features of the game now.

 * Intro Section.

    * An introduction of 'Border Scrutiny'.
    * Gives title of the game and starts the game.

        <img src="./docs/features/home_screen.PNG">

 * Name Section.

    * Continuation of the intro.
    * Gives you the input for player name, repeats it and sets up the story.

        <img src="./docs/features/name.PNG">

 * Start Section.

    * Start the game.
    * Gives you the yes or no choice to continue the game.

        <img src="./docs/features/start.PNG">   
     
 * Start End Section.

    * Start or end game.
    * Makes sure you either type yes or no to the question, if the answer is twice no, the game closes.

        <img src="./docs/features/start_end.PNG">  
    
 * Random Person Today Section.

    * Rules which have to be followed.
    * Gives you the list of randomized values on which you must keep an eye on in the next section. You must avoid letting anyone in with any of these values.

        <img src="./docs/features/random_today.PNG"> 

 * Documents section.

    * A person who has to be compared with forbidden values.
    * Pulls the random values from lists, creates a person.

        <img src="./docs/features/random_person.PNG">

 * Decision section.

    * Deicide which person fits the criteria and deicide their fate.
    * Depending on the values, the program prints if you got it right or not and either adds or removes money from saved data.

    * Basic Good Decision
        <img src="./docs/features/good_decision.PNG">
    * Basic Bad Decision
        <img src="./docs/features/bad_decision.PNG">
    * Caught a potential spy
        <img src="./docs/features/good_forbidden.PNG">
    * Missed a potential spy
        <img src="./docs/features/bad_forbidden.PNG">   

  * End section.

    * End screen with a retry option.
    * Prints total earned money, gives yes/no input to go again.

        <img src="./docs/features/money_repeat.PNG">

 * Game Over section.

    * Game Over section.
    * Prints out Game Over in ASCII.

        <img src="./docs/features/random_person.PNG">
