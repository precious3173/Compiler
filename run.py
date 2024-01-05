import shell

shell_instance = shell
shell_instance.build
code = "x === 10 + 5 || y <= 20"
shell_instance.lexer.input(code)
while True:
    text = shell_instance.lexer.token()
    if not text:
        break
    print(text)
