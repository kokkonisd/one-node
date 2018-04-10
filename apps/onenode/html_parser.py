import re
from enum import Enum


"""
-------------------WIP------------------

html_parser is a tool to modify html files according to the python context.
To insert variables or expression, one should insert {{ variable here }} into the html file.
To insert conditions, follow the template : {% if CONDITION || HTML || elif CONDITION || HTML || else || HTML %}
The if test is the only one mandatory and there could be any number of elif.
"""

def render_html(template_name, context):
    """Replace the script in the template with values in the given context"""
    f = open(template_name, "r")
    template = f.read()
    f.close()

    parsed_html = parse_html(template, context)

    return parsed_html


def parse_html(html, context):
    """Replace variable inside template by they current value in the context.
    Variable are identified by the following syntax {{MyVariable}} which will by remplaced by its value.
    """

    # Setup
    pattern = re.compile("((?:{{)|(?:}})|(?:{%)|(?:%}))")  # Regex

    parsed_html = ""

    blocks = pattern.split(html)

    print("")
    print("  >----------------------------<")
    print("")
    print(blocks)
    print("")

    i = 0
    while i < len(blocks):
        if blocks[i] == "{{":
            # A variable or expression
            i += 1
            parsed_html += eval(blocks[i], {}, context)
            i += 1
        elif blocks[i] == "{%":
            script = ""
            nb_script_nested = 0
            while True:
                if blocks[i] == "{%":
                    nb_script_nested += 1
                elif blocks[i] == "%}":
                    nb_script_nested -= 1

                script += blocks[i]
                if i + 1 == len(blocks) or nb_script_nested == 0:
                    break
                i += 1
            print("for")
            parsed_html += run_script(script, context)
        else:
            print("html")
            parsed_html += blocks[i]

        i += 1

    return parsed_html


def run_script(script, context):
    """Parse script. A script should have the following format : {% if X || instruction || else || other instruction %}
    or {% for i in XXX || instruction %}"""

    result = ""
    parsed_script = script[2:-2].split("||")
    header = parsed_script[0].split(None, 1)

    #print("Parsed script : ")
    # print(parsed_script)

    # The header should be either if or for
    if header[0] == "if":
        html = ""
        i = 0
        cursor = 0  # if the cursor is even, then the current block should be if, elif or else
        while i < len(parsed_script):
            if cursor % 2 == 0:
                nb_script_nested = 0
                instruction = parsed_script[i].split(None, 1)
                # If one condition is fulfilled
                if instruction[0] == "else" or ((instruction[0] == "if" or instruction[0] == "elif") and eval(instruction[1], {}, context)):
                    i += 1
                    while True:
                        nb_script_nested += parsed_script[i].count("{%")
                        nb_script_nested -= parsed_script[i].count("%}")
                        html += parsed_script[i]

                        if nb_script_nested == 0:
                            break

                        html += "||"
                        i += 1
                    return parse_html(html, context)
            else:
                nb_script_nested = 0
                while True:
                    nb_script_nested += parsed_script[i].count("{%")
                    nb_script_nested -= parsed_script[i].count("%}")

                    if nb_script_nested == 0:
                        break
                    i += 1
            i += 1
            cursor += 1

    elif header[0] == "for":
        pass

    return result


cont = {"test": "Success", "a": 6, "c": 8, "arr": [1, 2, 3]}
test = open("result.html", "w")
test.write(render_html("test.html", cont))
test.close()


"""
{% for i in arr || 
    <li>et {{i}}!</li>
%}
"""