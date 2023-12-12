# input + print
def main():
    text=input("insert text:")
    print(convert(text))
    #print(convert(input("insert text:")))

# convert :) ->🙂
# convert :( ->🙁
def convert(text):
    if ":)" in text or ":(" in text: #a single true condition is sufficient
        return text.replace(":)","🙂").replace(":(","🙁") 

main()

# for future uses

#if __name__=="__main":
#    main()
    
    