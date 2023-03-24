from html.entities import html5
import html
snowman = '\u2603'
print(snowman.encode('utf-8'))
print(snowman.encode('ascii', 'backslashreplace'))
print(snowman.encode('ascii', 'xmlcharrefreplace'))

cafe = 'caf\u00e9'
print(cafe)
cafe_bytes = cafe.encode('utf-8')
print(cafe_bytes)
print(cafe_bytes.decode('utf-8'))
# print(cafe_bytes.decode('ascii'))
print(cafe_bytes.decode('latin-1'))
print(cafe_bytes.decode('windows-1252'))
print(html5['egrave;'])

char = '\u00e9'
dec_value = ord(char)
print(char, dec_value)
print(html.entities.codepoint2name[dec_value])
byte_value = cafe.encode('ascii', 'xmlcharrefreplace')
print(byte_value, byte_value.decode())
