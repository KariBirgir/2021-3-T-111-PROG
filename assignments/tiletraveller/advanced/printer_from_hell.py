def rotate_text_clockwise(text):
    """ Rotates text 90 degrees clockwise, adding spaces as needed for multi-line strings """
    lines = text.splitlines()
    max_length = 0
    for line in lines:
        if len(line) > max_length:
            max_length = len(line)
    rotated_text = ""
    for character_index in range(max_length):
        for line in reversed(lines):
            if len(line) > character_index:
                character_to_add = line[character_index]
            else:
                character_to_add = " "
            rotated_text += character_to_add
        rotated_text += "\n"
    return rotated_text.rstrip("\n")
