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