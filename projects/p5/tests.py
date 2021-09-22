import hex_decimal as hd

assert hd.hex_str_to_decimal('D') ==  13
assert hd.hex_str_to_decimal('2F') == 47
assert hd.hex_str_to_decimal('A4E') == 2638
assert hd.hex_str_to_decimal('XYZ') == None

assert hd.decimal_to_hex_str(15) == 'F'
assert hd.decimal_to_hex_str(184) == 'B8'
assert hd.decimal_to_hex_str(6871) == '1AD7'

assert hd.hex_chr_to_decimal('D') == 13
assert hd.hex_chr_to_decimal('7') == 7
assert hd.hex_chr_to_decimal('X') == None

assert hd.decimal_to_hex_chr(15) == 'F'
assert hd.decimal_to_hex_chr(11) == 'B'
assert hd.decimal_to_hex_chr(5) == '5'


