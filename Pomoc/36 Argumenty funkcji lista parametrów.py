def funkcja(arg1,arg2 = 'World', *args, **kwargs):
    print(arg1, arg2, args,len(args), kwargs)

    for i in args:
        print(i)

    for i in kwargs.values():
        print(i)

funkcja('Hello')
funkcja('Hi', 'Youtube')
funkcja('hi', 'youtube', '!', ';)', autor= 'Marcin', rok= 2022)
