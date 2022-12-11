import re as regex

## Replace content in-between two lines in your MD file(s).

## The content you want to add to your README / Replace in between two sections (JSON values etc)
# Note: Do not forget to add a line break (empty line) at the top and bottom
Template = """
<!---START OF CONTENT --->
1. ❗️ Opened issue [#11](https://github.com/) in [Meow](https://github.com)
2. ❗️ Closed issue [#9](https://github.com/) in [Meow](https://github.com)
3. 🎉 Merged PR [#10](https://github.com/) in [Meow](https://github.com)
4. 💪 Opened PR [#10](https://github.com/) in [Meow](https://github.com)
5. ❗️ Opened issue [#9](https://github.com/) in [Meow](https://github.com)
<!---END OF CONTENT --->
"""
# Define the filename here you want to replace content in
FileName = "README.md"


with open(FileName, 'r') as f:
    contents = f.read()
    # Define the first line where your content will be replaced / added 
    starting_text = '<!---START OF CONTENT --->'
    # Define the second line where your content will be replaced / added 
    ending_text = '<!---END OF CONTENT --->'
    # Replace all matches with your template!
    contents = replace_between_all_regex(contents, starting_text, ending_text, template)

    
def replace_between_all_regex(text, start, end, replacement):
    """
    Replace content between two strings
    :param text: Text to be processed
    :param start: Start string
    :param end: End string
    :param replacement: Replacement string
    :return: Processed text
    """
    # Compile regex
    regex = re.compile(start + "(.*?)" + end)

    # Replace text between start and end indexes
    return regex.sub(replacement, text)    

with open(FileName, 'w') as f:
    f.write(contents)   
    
