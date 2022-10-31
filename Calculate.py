def check_scope():
    def do_local():
        test = "local test"

    def do_non_local():
        nonlocal test
        test = "non local test"

    def do_global():
        global test
        test = "global"

    test = "default"
    do_local()
    print("After local" + test)
    do_non_local()
    print("after non local :"+test)
    do_global()
    print("after global :"+test)

check_scope()
print("main test"+test)
