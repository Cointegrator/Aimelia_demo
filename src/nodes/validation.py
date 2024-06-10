"""
Validation node

Validators use validation nodes to verify the results of
each game in an objective manner. Similarly, validators can
delegate the work to validation nodes or can do the
validation work themselves manually. Creators can also use validation node
to automcatically announce the outcome of the game, but it
is on his/her own risk of doing it.

Function:

AI or humans to check the correctness or consensus
of conclusions. Validation nodes help validators to verify
the results in the network. The reward is distributed
if there is a high discrepancy between the claimed results
and the results verified by validators.
"""

from src.nodes.base import Node


class ValidationNode(Node):

    def __init__(self) -> None:
        pass
