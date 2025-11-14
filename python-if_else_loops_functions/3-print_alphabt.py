#!/usr/bin/python3
print("{}".format("".join(chr(i) for i in range(ord('a'), ord('z') + 1)
                                   if chr(i) != 'q' and chr(i) != 'e')), end="")
