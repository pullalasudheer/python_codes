def div(a,b):
    print(a/b)


    def smart_div(func):
        def div1(a,b):
            if a>b:
                a,b =b,a
            return func(a,b)
        return div1

div(2,5)