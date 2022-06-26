with open('README.md', 'r') as f:
    contents = f.read()
    starting_text = '<---START OF CONTENT --->'
    ending_text = '<---END OF CONTENT --->'
    to_replace = contents[contents.find(starting_text)+len(starting_text):contents.rfind(ending_text)]
    contents = contents.replace(to_replace, 'whatever you want to replace it with')
    
with open('README.md', 'w') as f:
    f.write(contents)   
    
