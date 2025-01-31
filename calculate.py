import sys
import math

def calculate(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "<p>Error: All values must be numeric</p>"

    if a < 1:
        return "<p>Error: Value of 'a' is too small (must be greater than 1)</p>"

    if b == 0:
        b_message =  "<p>Error: Value of 'b' is zero and not affect the result</p>"
    else:
        b_message = ""

    if c < 0:
        return "<p>Error: 'c' cannot be negative.</p>"


    c_cubed = c ** 3

    if c_cubed > 1000:
        result = math.sqrt(c_cubed) * 10
    else:
        result = math.sqrt(c_cubed) / a

    result += b

    return f""" {b_message}
    <p>c^3 = {c_cubed}</p>
    <p>Final result: {result}</p>"""

if __name__ == "__main__":

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        print(calculate(a, b, c))
    except Exception as e:
        print(f"<p>Error: {str(e)}</p>")