def hello_func(greeting,name='You'):
    return '{},{}'.formate(greeting,name)
#print(hello_func(Hi,nmae='Anil'))
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
courses = ['Math','CompSci']
info = {'name':'John','age':22}
student_info(*courses,**info)
