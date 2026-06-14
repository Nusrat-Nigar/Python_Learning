# f = open('nusrat.txt', 'r')
# content = f.read()
# print(content)

# f.close()



with open('nusrat.txt','r') as f:  # Context manager
    content = f.read()
    print(content)

    # No need to write f.close() because file is already closed by default when using with syntex.It automatically close the file even if errors occur