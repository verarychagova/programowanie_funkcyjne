global_variable = 10


def function(local_variable):
    return local_variable + global_variable


loc_var = 5
print(function(loc_var))
