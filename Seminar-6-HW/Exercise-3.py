#3.Задача
#Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), 
# применив лямбды, filter, map, zip, enumerate, списочные выражения.

text_st = ' рилдфа абв олр аь абвордц абв йгшщриот'

# СТАРЫЙ КОД
# def find_text(text_x, text_find='абв'):
#     text_new = []
#     count = 0
#     for x in text_x:
#         if x.find(text_find) == -1:
#             text_new.append(x)
#         count += 1
    
#     return text_new

# УСОВЕРШЕНСТВОВАННЫЙ КОД
# добавлены: <lambda> и <filter>
def find_text(text_x, text_find='абв'):
    text_new = list(filter(lambda x: text_find not in x, text_x))
    return text_new

def text_print(text_pr):
    return " ".join(text_pr)

print(f'\nИсходный текст: {text_st}\n')
new_text = text_st.split()
find_char = 'абв'
text_del = find_text(new_text, find_char)
print(f'Текст без слов, содержащих "абв": {text_print(text_del)}\n')