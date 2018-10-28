spam=['apples','bananas','tofu','cats']
def func(spam):
    spam[-1]='and'+' '+spam[-1]
    for i in range(len(spam)):
        print(spam[i],end=',')
func(spam)