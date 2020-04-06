from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS 
# import matplotlib.pyplot as plt
from random import random
import os

def wordcloud(file):
    
    text_data = file.readlines()
    text_data = [x.decode("utf-8") for x in text_data]
    
    tokenized_text_data = [x.split(' ') for x in text_data]
    name_freq_dict = {}

    for lines in tokenized_text_data[1:]:
        if "-" in lines:
            key_index = lines.index("-")
            name = lines[key_index + 1]

            if name not in name_freq_dict:
                name_freq_dict[name] = 1
            else:
                name_freq_dict[name] += 1

    for people in list(name_freq_dict):
        if name_freq_dict[people] < 3:
            del name_freq_dict[people]


    text_file = ""
    for lines in tokenized_text_data:
        if "-" in lines:
            key = lines.index("-")
            name = lines[key + 1]

            text_file += name + " "


    love_img_arr = np.array(Image.open("love.jpg"))


    wordcloud = WordCloud(width = 1000, height = 1000, 
                background_color ='white', 
                stopwords = STOPWORDS, 
                max_words = 1200,
                max_font_size = 50,
                repeat = False,
                mask = love_img_arr,
                min_font_size = 10).generate(text_file) 

    foldername = "to_save" + str(int(random() * 10000000000))
    filename = "generated_wordcloud" + str(int(random() * 10000000000)) + ".png"

    os.mkdir(foldername)
    wordcloud.to_file(foldername + '/' + filename)



    return foldername, filename