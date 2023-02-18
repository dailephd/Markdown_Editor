textlist = []


class MarkdownEditor:

    def __init__(self):
        self.inp = input("Choose a formatter:")

    @staticmethod
    def help():
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")

    @staticmethod
    def done():
        with open("output.md", "w") as f:
            text = "".join(textlist)
            f.write(text)
        exit()

    def header(self):
        check = False
        while check == False:
            self.level = int(input("Level:"))
            if self.level in range(1, 7):
                check = True
            else:
                print("The level should be within the range of 1 to 6")
        text = input("Text:")
        text = "#" * self.level + " " + text + "\n"
        textlist.append(text)
        print("".join(textlist))

    def plain(self):
        text = input("Text:")
        textlist.append(text)
        print("".join(textlist))

    def bold(self):
        text = input("Text:")
        text = "**" + text + "**"
        textlist.append(text)
        print("".join(textlist))

    def italic(self):
        text = input("Text:")
        text = "*" + text + "*"
        textlist.append(text)
        print("".join(textlist))

    def inline_code(self):
        text = input("Text:")
        text = "`" + text + "`"
        textlist.append(text)
        print("".join(textlist))

    def new_line(self):
        text = "\n"
        textlist.append(text)
        print("".join(textlist))

    def link(self):
        self.label = input("Label:")
        self.url = input("URL:")
        text = "[" + self.label + "]" + "(" + self.url + ")"
        textlist.append(text)
        print("".join(textlist))

    def ordered_list(self):
        check = False
        while check == False:
            self.rows = int(input("Number of rows:"))
            if self.rows > 0:
                check = True
            else:
                print("The number of rows should be greater than zero")
        i = 0
        while i < self.rows:
            text = input(f"Row #{i+1}:")
            text = f'{i+1}. ' + text + '\n'
            textlist.append(text)
            i += 1
        print("".join(textlist))

    def unordered_list(self):
        check = False
        while check == False:
            self.rows = int(input("Number of rows:"))
            if self.rows > 0:
                check = True
            else:
                print("The number of rows should be greater than zero")
        i = 0
        while i < self.rows:
            text = input(f"Row #{i+1}:")
            text = f'* {text} \n'
            textlist.append(text)
            i += 1
        print("".join(textlist))

    def run(self):
        s = self.inp
        if s == "!help":
            self.help()
        elif s == '!done':
            self.done()
        elif s == "header":
            self.header()
        elif s == "plain":
            self.plain()
        elif s == "bold":
            self.bold()
        elif s == "italic":
            self.italic()
        elif s == "link":
            self.link()
        elif s == "inline-code":
            self.inline_code()
        elif s == "ordered-list":
            self.ordered_list()
        elif s == "unordered-list":
            self.unordered_list()
        elif s == "new-line":
            self.new_line()
        else:
            print("Unknown formatting type or command")
            pass


if __name__ == "__main__":
    while True:
        MarkdownEditor().run()