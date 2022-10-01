import os


with open('chapters.tex', 'w') as file:
    for chapter in os.listdir('chapters'):
        file.write('\input{chapters/' + chapter + '}')
