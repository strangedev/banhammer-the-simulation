# Simulation of score based moderation for chat groups

Simulates a running "naughtiness" score for users. Bad actions raise the score.
The score decays naturally over time.
People with a score larger than 1 are penalized.

#### Requirements

- Python3
- TK (Install via distro package manager, e.g. pacman, yum)
- Imagination


#### Running

`./main.py/`

Make sure to `chmod +x`.

You can parameterize the simulation in `main.py`. Take a look at the `RANDOM_EVENTS` and `SCHEDULED_EVENTS`.

##### Pretty Pictures

Green icons are decay events, blue are minor wrongdoings, red are major ones. 

![alt-text](https://github.com/strangedev/banhammer-the-simulation/blob/master/banhammer.png)
