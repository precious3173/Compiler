import re
import ply.lex as lex


class shell:
 
  tokens = (
  'NUMBER',
  'PLUS',
  'MINUS',
  'TIMES',
  'DIVIDE',
  'LPAREN',
  'RPAREN',
  'OR',
  'AND',
  'EQUALITY',
  'INEQUALITY',
  'GREATER',
  'LESS'
  )

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_OR = r'\|\|'
t_AND = r'\&\&'
t_EQUALITY = r'(===|==)'
t_INEQUALITY = r'(!==|!= )'
t_GREATER = r'(>=|>)'
t_SMALLER = r'(<=|<)'

# Define a rule to match numbers
#\d is a regular expression, this means matches any digit (0-9)
#+ are operators, this causes the resulting RE to match 1 or more repetitions of the preceding RE. 
# ab+ will match 'a' followed by any non-zero number of 'b'; it will not match just 'a'
# the 'r' before a string literal in python denotes a "raw" string. In Python, a backslash ('\') is an escape character.
# When an 'r' is placed before the string laterial, it signifies that backslashes should be treated as literal characters rather than escape characters
# in the context of regular expressions, the use of raw strings ('r') is common because regular expressions often contain backslashes, which are used as escape characters in regular python strings
# Using a raw string helps avoid unintended interpretation of escape sequences. It ensures that the backslashes are treated as literal characters within the regular expression pattern
def t_NUMBER(self, t):        
        r'\d+'
        t.value = int(t.value)
        return t

  # Define a rule to track line numbers
def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
