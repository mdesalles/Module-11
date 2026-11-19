def main():
    word_list=["cat", "program", "canvas", "dog", "dashboard", "debug", "go", "red"]
    result=print_words(word_list)
    print(result)
def print_words(words):
    for i in words:
        if len(i)==3:
            print(i.title())
main()