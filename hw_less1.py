def palindrom(p):
    status = True
    for i in range(len(p)):
        if p[i-1] != p[-i]:
            status = False
    print(status)
palindrom('лепсспел')
palindrom('helloworld')
palindrom('abcba')
palindrom('искатьтакси')