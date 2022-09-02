def writing_tokens(vk, ya):
    with open("Tokens.txt", 'a') as file:
        file.write(f'{vk}\n')
        file.write(ya)

