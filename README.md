Genetic driven artificial neural network playing Flappy Bird
============================================================
A clone of *Flappy Bird*, using Pygame, cloned from [https://github.com/TimoWilken/flappy-bird-pygame](https://github.com/TimoWilken/flappy-bird-pygame). ``annflappy.py`` is a version using genetic
algorithm to evolve an artificial neural network through successive runs of
the game. The genome is responsible for setting the weights and thresholds of
the artificial neurons, so this is not *NEAT*. The best fit genome is saved to 
``best_fit.genome``. The current saved genome is pretty good at playing the
game. If you want to start the learning from scratch delete ``best_fit.genome``.

The code is not pretty, and ANN might be a little over sized for the task. This 
is mostly just something that I had been wanting to try for a long time (since before Flappy Bird). [https://www.reddit.com/r/learnprogramming/comments/3a3rmy/python_trying_to_create_a_neural_net_with_a/](https://www.reddit.com/r/learnprogramming/comments/3a3rmy/python_trying_to_create_a_neural_net_with_a/) kicked me in the right direction, at last.

*Ohh and press ``ESC`` to exit.*

