from collections import Counter

#numbers.txt
#digit more frequent in text
def frequency_digital():
    #add numbers.txt in list use .strip to remove space
    text = [line.strip() for line in open("numbers.txt","r")]#list comprehension to avoid repetition with loop
    #print(text)
    #join list in a single string removing space
    value = ''.join(text)
    #print(value)
    #divide string in single letter/number
    all_digit = [x for x in value]
    #most_common sequence of most frequent n
    frequency = Counter(all_digit).most_common()
    #print(frequency[0]) #1st set of value and frequency
    print("The digit {} appear the most, exactly {} times.".format(frequency[0][0],frequency[0][1]))
frequency_digital()


#numbers.txt
#which number is missing
def missing_value():
    #add value from txt file to list .strip instead of append to remove \n (space)
    text = [line.strip() for line in open("numbers.txt","r")] #list comprehension to avoid repetition with loop
    #convert string numbers in integer numbers to check missing value
    text = [int(i) for i in text]
    #text.sort() - used to check if missing number is correct
    #print(text)
    for x in range(1, 1564): #compare sequence range (1 to 1564) with text list to determine missing value from text list
        if x not in text:
            #print(x) - missing number value
            print("The missing number is {}.".format(x))
missing_value()






#colours.txt
#most and least appearing words in the file
def frequency_words():
    a = ','
    b = '\n'
    c = '.'
    d = '-'
    #list comprehension to move file value to a list
    #remove next line, coma, any grammar punctuation and replace it with white space to have separate words
    text = [line.replace(a, ' ').replace(b, ' ').replace(c, ' ').replace(d, ' ') for line in open("colours.txt", "r")]
    #join list into a long string to split every single words
    text = ' '.join(text)
    #separate every single words into a list with split since default separator is whitespace
    text = text.split()
    #use most common method to calculate frequency of every words
    frequency = Counter(text).most_common()
    #frequency of each word appearing in the file
    #print(frequency)
    print("The colour {} appear the most, exactly {} times.".format(frequency[0][0], frequency[0][1]))
    print("The colour {} appear the least in the whole file, exactly {} times.".format(frequency[-1][0], frequency[-1][1]))

frequency_words()



#colours.txt
#line with green but not blue
def green_no_blue():
    with open("colours.txt", "r") as fp:
        lines = fp.readlines()
        #text = [x for x in lines]
        #print(text)
        word = ["GREEN"]
        word_1 = ["BLUE"]
        text = []
        # Process to check if each strings line from file contains elements from lists word
        ###################-Process to check green and blue- ########################
        #for x in lines:
            #if any(substring.lower() in x.lower() for substring in word):
                #if any(substring.lower() not in x.lower() for substring in word_1):
                    #print(x)
        ############################################################################
        #abbrevation process to check green and blue with list comprehension
        text = [x for x in lines if any(substring.lower() in x.lower() for substring in word) if
                any(substring.lower() not in x.lower() for substring in word_1)]
        #print(len(text)) number of line containing green but not blue
        print("The number of lines that contains 'GREEN' but not 'BLUE' are {}.".format(len(text)))
green_no_blue()







#colours.txt
#line with same colour
def three_times_words():
    f = open("colours.txt", "r")
    text = f.read()
    #print(text) check how many value per line. this case 3 value per line
    a = ','
    b = '\n'
    c = '.'
    d = '-'
    text = [line.replace(a, ' ').replace(b, ' ').replace(c, ' ').replace(d, ' ') for line in open("colours.txt", "r")]
    text = ' '.join(text)
    text = text.split()
    count = 0
    for i in range(0, len(text), 3):
        new_list = []
        new_list.append(text[i: i + 3])
        # print(new_list[0][0],new_list[0][1],new_list[0][2])
        if new_list[0][0] == new_list[0][1] == new_list[0][2]:
            ls = [y for x in new_list for y in x]
            #print(ls) # triplet of same colours
            count += 1
            #print(count) counter inside loop
    #print(count) #out of loop for final count
    print("The number of lines that contains same colour are {}.".format(count))

three_times_words()






#colours.txt
#line with different colour
def different_words():
    f = open("colours.txt", "r")
    text = f.read()
    # print(text) check how many value per line. this case 3 value per line
    a = ','
    b = '\n'
    c = '.'
    d = '-'
    text = [line.replace(a, ' ').replace(b, ' ').replace(c, ' ').replace(d, ' ') for line in open("colours.txt", "r")]
    text = ' '.join(text)
    text = text.split()
    count = 0
    for i in range(0, len(text), 3):
        new_list = []
        new_list.append(text[i: i + 3])
        #print(new_list[0][0],new_list[0][1],new_list[0][2])
        if new_list[0][0] != new_list[0][1] != new_list[0][2]:
            #print(new_list)
            ls = [y for x in new_list for y in x]
            #print(ls) # triplet of different colours
            count += 1
            #print(count) counter inside loop
    #print(count) #out of loop for final count
    print("The number of lines that contains different colours are {}.".format(count))
different_words()










