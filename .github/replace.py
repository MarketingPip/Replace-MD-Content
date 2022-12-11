import re

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


def replace_between(file_name, start_string, end_string, new_string):
    with open(file_name, 'r') as f:
        content = f.read()
    content = re.sub(r'{}.*?{}'.format(start_string, end_string), new_string, content, flags=re.DOTALL)
    with open(file_name, 'w') as f:
        f.write(content)

    # Define the first line where your content will be replaced / added 
starting_text = '<!---START OF CONTENT --->'
    # Define the second line where your content will be replaced / added 
ending_text = '<!---END OF CONTENT --->'
    # Replace all matches with your template!
        
replace_between(FileName, starting_text, ending_text, Template)
 



    
