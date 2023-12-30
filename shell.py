from rply import LexerGenerator


class shell():
 #  method is a special method that gets automatically called when you create a new object (instance) of the class
 # it's like a constructor in other programming language
 def __init__(self):
    self.lexer = LexerGenerator()