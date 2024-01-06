from shell import Shell


shell_instance = Shell
shell_instance.build
code = "x === 10 + 5 || y <= 20"
shell_instance.lexer.input(code)
while True:
    token = shell_instance.lexer.token()
    if not token:
        break
    print(token)
