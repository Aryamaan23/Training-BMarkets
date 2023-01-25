import test
def monkey_patch_func(self):
    print("Monkey patch function is called")

test.Test.func=monkey_patch_func
ob=test.Test()
ob.func()

