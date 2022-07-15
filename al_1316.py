N = int(input())
words = ["" for i in range(N)]

for i in range(N):
    words[i] = input()
    
print(words)
   
def group_check(word):
    group_word_list = [] 
    for w in word:
        if w not in group_word_list:
            group_word_list.append(w)
        else:
            if w == group_word_list[-1]:
                pass
            else:
                return 0
    else:
        return 1
    
cnt = 0
    
for word in words:
    cnt = cnt + group_check(word)

print(cnt)
    