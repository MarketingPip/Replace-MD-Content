Template = """
1. ❗️ Opened issue [#11](https://github.com/) in [Meow](https://github.com)
2. ❗️ Closed issue [#9](https://github.com/) in [Meow](https://github.com)
3. 🎉 Merged PR [#10](https://github.com/) in [Meow](https://github.com)
4. 💪 Opened PR [#10](https://github.com/) in [Meow](https://github.com)
5. ❗️ Opened issue [#9](https://github.com/) in [Meow](https://github.com)

"""


with open('README.md', 'r') as f:
    contents = f.read()
    starting_text = '<!---START OF CONTENT --->'
    ending_text = '<!---END OF CONTENT --->'
    to_replace = contents[contents.find(starting_text)+len(starting_text):contents.rfind(ending_text)]
    contents = contents.replace(to_replace, Template)
    
with open('README.md', 'w') as f:
    f.write(contents)   
    
