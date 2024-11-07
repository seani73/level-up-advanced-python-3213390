import re

patternItalics = re.compile(r'<\/?em>')
patternSpaces = re.compile(r'\s+')
patternParas = re.compile(r'<\/?p>')
patternURLs = re.compile(r'<a href="(.+?)">(.+?)</a>')

#<a href="https://www.example.com">Visit Example</a>
#[Visit Example](https://www.example.com)

def html2markdown(html):
    '''Take in html text as input and return markdown'''

    markdown = re.sub(patternItalics, '*', html)
    markdown = re.sub(patternSpaces, ' ', markdown)
    markdown = re.sub(patternParas, '\n', markdown)
    markdown = re.sub(patternURLs, r'[\2](\1)', markdown)

    return markdown.strip()