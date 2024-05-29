"""
Inference Node

Players employ inference nodes to make decisions. They can deposit
the money to the inference nodes and delegate the work entirely
to inference nodes to make decisions.

Function:

AI or humans draw conclusions from gathered knowledge
( which can be auditable on-chain) and learn from each other's
decision-making processes. Inference nodes are for
players to make better decisions.
"""
from src.nodes.base import Node

from typing import Optional, List

import requests
from bs4 import BeautifulSoup

class InferenceNode(Node):
    """
    Compiles all the document together
    to allow users / bots to make informed decisions
    """

    def __init__(self) -> None:
        pass


