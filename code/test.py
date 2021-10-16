# import lib.config as config
#
# if __name__ == '__main__':
#     cfg = config.DebiConfig()
#     cfg.cmake()

def manys(n):
    def cache_upper(func):
        c =dict()
        def deco(sss):
            print('decoration')
            if not sss in c:
                print('cached')
                c[sss] = sss
            return c[sss] *n
        return deco
    return cache_upper

# @manys(3)
def myfunc(s:str) -> str:
    return s.upper()

print(myfunc('demo'))
print(myfunc('turbo'))
print(myfunc('demo'))
print(myfunc('save'))
print(myfunc('turbo'))
