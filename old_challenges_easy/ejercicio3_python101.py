# *********** Ejecicio 3 **************
#Encontrar dentro de una string, aquella palabra con la mayor cantidad de letras.

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis facilisis molestie. In sed elit ut mauris iaculis porttitor. Vestibulum ac justo lobortis, rhoncus eros sed, feugiat ante. Nunc interdum, nunc at pellentesque facilisis, urna libero venenatis purus, sed dignissim orci diam id urna. Aenean placerat leo eget felis efficitur."

#Expected ==> La palabra más grande es: pellentesque con 12 letras

words_list = lorem.split()
longest_word = ''

for word in words_list:
    if len(word) > len(longest_word):
        longest_word = word
    
print(f'The longest word is {longest_word} with {len(longest_word)} letters')




#lorem_split = lorem.split()
#max(lorem_split)

#lorem_list = lorem.split

#print(len(lorem_list))

#longest = len(lorem)
#print(longest)

#print(longest)

