from Action import A1ction
from person import Human
class Rest(A1ction):
    def __init__(self, name, health, mud, money):
        A1ction.__init__(self, name, health, mud, money)