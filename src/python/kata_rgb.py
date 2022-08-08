"""
RGB To Hex Conversion

The rgb function is incomplete. Complete it so that passing in RGB decimal
values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255. Any values that fall out of that
range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand w
ith 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

"""


def rgb(red: int, green: int, blue: int) -> str:
    "Returns the rgb color in hexadecimal form."

    def pad(color: str) -> str:
        while len(color) < 2:
            color = "0" + color
        return color

    def cap(color: int) -> int:
        if color > 255:
            return min(color, 255)

        return max(color, 0)

    return (
        pad(hex(cap(red)).replace("0x", ""))
        + pad(hex(cap(green)).replace("0x", ""))
        + pad(hex(cap(blue)).replace("0x", ""))
    ).upper()
