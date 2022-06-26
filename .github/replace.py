
## Replace content in-between two lines in your MD file(s).

## The content you want to add to your README / Replace in between two sections (JSON values etc)
# Note: Do not forget to add a line break (empty line) at the top and bottom
Template = """
1. ❗️ Opened issue [#11](https://github.com/) in [Meow](https://github.com)
2. ❗️ Closed issue [#9](https://github.com/) in [Meow](https://github.com)
3. 🎉 Merged PR [#10](https://github.com/) in [Meow](https://github.com)
4. 💪 Opened PR [#10](https://github.com/) in [Meow](https://github.com)
5. ❗️ Opened issue [#9](https://github.com/) in [Meow](https://github.com)

"""
# Define the filename here you want to replace content in
FileName = "README.md"

with open(FileName, 'r') as f:
    contents = f.read()
    # Define the first line where your content will be replaced / added 
    starting_text = '<!---START OF CONTENT --->'
    # Define the second line where your content will be replaced / added 
    ending_text = '<!---END OF CONTENT --->'
    to_replace = contents[contents.find(starting_text)+starting_text:contents.rfind(ending_text)]
    contents = contents.replace(to_replace, Template)
    
with open(FileName, 'w') as f:
    f.write(contents)   
    
