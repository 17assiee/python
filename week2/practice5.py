#1
word="forest: mushrooms. trees, grass, forest fairy, sunbeam."
letter = "f"
count=0
x=word.split()
for i in x:
    if(i.find(letter)!=-1):
        count+=1
print("words count : " + str(count))

#2
word2="forest: mushrooms. trees, grass, forest fairy, sunbeam."
print("replacement(:,%): ",word2.replace(':','%'))
count1=0
for i in word2:
      if i==':': count1+=1
print("count of replacements: " + str(count1))


#3
word2="forest: mushrooms. trees, grass, forest fairy, sunbeam."
print("delete (.): ",word2.replace('.',''))
count1=0
for i in word2:
      if i=='.': count1+=1
print("count of delete: " + str(count1))

#4
word2="forest: mushrooms. trees, grass, forest fairy, sunbeam."
print("delete (.): ",word2.replace('a','o'))
count1=0
for i in word2:
      if i=='a': count1+=1 
print("count of delete: " + str(count1))
print("count of characters: " +str(len(word2)))

#5
word2="Forest: mushrooms. trees, grass, forest fairy, sunbeam."
print("upper to lower: " +str(word2.lower()))

#6
word2="forest: mushrooms. trees, grass, forest fairy, sunbeam."
print("delete (a): ",word2.replace('a',''))
count1=0
for i in word2:
      if i=='a': count1+=1
print("count of delete: " + str(count1))

#7
s="forest: mushrooms. trees, grass, forest fairy, sunbeam."
n = len(s)
s = s[:n // 2].replace('e', '*') + s[n // 2:]
print(s)

#8
word="forest: mushrooms. trees, grass, forest fairy, sunbeam."
result = len(word.split())

print("there are " + str(result) + " words.")

#9
word="forest: mushrooms. trees, grass, forest fairy, sunbeam."
text="trees"
print("frequency of " + text + " is ", word.count(text))

#10
word="forest: mushrooms. trees, grass, forest fairy, sunbeam."
print("capital letter: ", word.title())

#11
word="forest: mushrooms. lennn trees, grass, forest fairy, sunbeam."
count = 0
max_count = 0

for letter in word:
    if letter == 'n':
        count += 1
        max_count = max(count, max_count)
    else:
        count = 0

print("consecutive letters 'n': ", max_count)

#12
word="forest: mushrooms. leni barni trees, grass, forest fairy, sunbeam."
print(*(i for i in word.split() if i.endswith('i')))

#13
word="forest: mushrooms. (trees, grass) forest fairy, sunbeam."
print("oprning and closing brackets: ", word.split("(")[-1].split(")")[0])

#14
str="forest: mushrooms. trees, apple bani grass, forest fairy, sunbeam."
for w in str.split():
    if(w.startswith("a") or w.endswith("i")): 
        print("start with 'a' and end with 'i': ", w)

#15
text="toilet table toys"
print("count of 't': ", text.count('t'))
