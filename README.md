# Alquist random dialogue generator
Utility for Alquist dialogue manager (https://github.com/AlquistManager/alquist). This utlity generates YAML files containing 
random dialogue for the ALquist dialogue manager. The purpose of this utility is to test proper functionality of the Alquist dialogue
manager on a gialogue of larger number of states.

## Installation
Install Python 3.

Run the application running main.py script. The application doesnt require any input parameters. 

    py -3 main.py

## How to use

The app creates random net of nodes based on quantnties obtained from config file.
There are 7 types of nodes: text, random text, conditional equal, conditional exists, user input match, user input default and context input
Each node is composed of the primary state correspondin to the node type as well as one to three secondary message_text states, handling the output.

Output of each node are designed in order to easily recognise if the application follows the state flow properly or if there is a problem somewhere inside the code.

For the input nodes, the application expects values 0 or 1 in order to pass. In order to simulate user giving wrong input please enter
random word or string instead.

For the appropriate NLP response when testing the alquist manager on generated dialogue please use following wit.ai server access token:

    4GHEIUDP772M6K6GHEEJQYH3D3QTBI5D

## Test
You can test random net of nodes by ``main_test.py`` in ``test_script`` folder. How to do it is described in https://github.com/AlquistManager/alquist-random-dialogue-generator/blob/master/test_script/README.md