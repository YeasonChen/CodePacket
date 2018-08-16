# import skipper
#
# a = skipper.febonaqie()
# print(a)
#
# print(next(a))
# print(next(a))
#
# a.send('yeason')


def wraper_args(arg):
    print('1')

    def wraper(func):
        print('2')

        def wraper_in(*args, **kwargs):
            if arg == 'yeason':
                print('Do some thing in the wraper_in arg = %s' % arg)
                result = func(*args, **kwargs)
            else:
                print('get out from here arg = %s' % arg)
                result = func(*args, **kwargs) + func(*args, **kwargs)
            return result
        return wraper_in
    return wraper


@wraper_args('fuck')
def test1(name, **kwargs):
    print('this is the compeletion in the test1 %s' % name)
    print(kwargs)
    return name


re = test1('yeason', ja='jack', na='nancy')
print(re)
