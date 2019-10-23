from parameterized import parameterized


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


def greet_me(**kwargs):
    lista = kwargs.items()
    print(lista)
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


@parameterized(
    [("teste1", "segunda"),
    ("teste2", "terca"),
    ("teste3", "quinta")]
)
def test_function(self, **kwargs):
    lista = kwargs.items()
    print(lista)
    for i in kwargs.items():
        print("{0}".format(i))
    
if __name__ == "__main__":
    # unittest.main()
    #greet_me(name="yasoob", id="kalie", teste="talvex")
    test_function()