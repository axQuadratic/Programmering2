import math
import termcolor as tc

class InfoBox:
    def __init__(self, border_color, char_width, line_count, title, lines):
        self.border_color = border_color
        self.char_width = char_width
        self.line_count = line_count
        self.title = title
        self.lines = lines

def draw_message_box(box_data):
    lines = ["" for i in range(10)]
    for box in box_data:
        lines[0] += "".join([tc.colored("=", box.border_color) for i in range(math.floor((box.char_width - len(box.title)) / 2))]) + box.title + "".join([tc.colored("=", box.border_color) for i in range(math.ceil((box.char_width - len(box.title)) / 2))]) + " "

        if len(box.lines) < box.line_count:
            while len(box.lines) < box.line_count:
                box.lines.append("")

        i = 1
        for line in box.lines:
            lines[i] += tc.colored("|", box.border_color) + line + "".join(" " for i in range(box.char_width - len(line) - 2)) + tc.colored("|", box.border_color) + " "

            i += 1
        
        lines[i] += "".join([tc.colored("=", box.border_color) for i in range(box.char_width)]) + " "

    for line in lines:
        if line != "": print(line)

def create_health_bar(color, char_length, current_health, max_health):
    bar_data = []
    for segment in range(char_length):
        if current_health / max_health > segment / char_length:
            bar_data.append(tc.colored("#", color))
        else:
            bar_data.append(" ")
    return f"[{''.join(bar_data)}]"