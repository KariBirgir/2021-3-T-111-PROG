PROMPT = "Enter option: "
HEX_LETTERS = 'ABCDEF'
DEC_TO_HEX_OPTION = 'd'
HEX_TO_DEC_OPTION = 'h'
EXIT_OPTION = 'x'
MENU_STR = f"\n{DEC_TO_HEX_OPTION}. Decimal to hex\n{HEX_TO_DEC_OPTION}. Hex to decimal\n{EXIT_OPTION}. Exit\n"

def main():
    '''Displays menu, gets input from user and displays result'''    
    display_menu()
    option = input(PROMPT)
    
    while option != EXIT_OPTION:
        
        if option == DEC_TO_HEX_OPTION:
            dec_int = int(input("Decimal number: "))
            print('The hex is {}'.format(decimal_to_hex_str(dec_int)))
            
        elif option == HEX_TO_DEC_OPTION:
            hex_str = input("Hex number: ")
            print('The decimal is {}'.format(hex_str_to_decimal(hex_str)))
            
        else:
            print("Invalid option!")
        
        display_menu()   
        option = input(PROMPT)

def display_menu():
    '''Shows menu options to the user'''
    print(MENU_STR)

def decimal_to_hex_str(dec_int):
    '''Return the hex string corresponding to the given decimal number'''
    hex_str = ""
    while dec_int > 0:
        hex_str += decimal_to_hex_chr(dec_int % 16)
        dec_int = dec_int // 16
    return hex_str[::-1]    # reverses the string

def decimal_to_hex_chr(dec_int):
    '''Returns the hex char corresponding to the given decimal, or None if invalid'''
    if 0 <= dec_int <= 9:
        return str(dec_int)
    elif 10 <= dec_int <= 15:
        return chr(55 + dec_int)     # 'A' is chr(65) 
    return None # Not valid

def hex_str_to_decimal(hex_str):
    '''Returns the decimal corresponding to the given hex string.
    Return None if the hex string is invalid'''
    dec_sum = 0
    hex_len = len(hex_str)
    for index, hex_chr in enumerate(hex_str):
        dec_value = hex_chr_to_decimal(hex_chr)
        if dec_value is None:
            return None
        dec_sum += dec_value * (16 ** (hex_len - index - 1))
    return dec_sum
    
def hex_chr_to_decimal(hex_chr):
    '''Returns the decimal corresponding to the given hexadecimal character or None if invalid'''
    hex_chr = hex_chr.upper()
    if hex_chr.isdigit():
        return int(hex_chr)
    elif hex_chr in HEX_LETTERS:
        return ord(hex_chr) - 55   # ord('A') is 65 and 'A' is 10 in decimal
    else:
        return None # Not valid

# Main program starts here
if __name__ == "__main__":
    main()
