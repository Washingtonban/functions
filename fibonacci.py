def fibonacci(limite:int = 100) -> list:
    '''
    Função que retorna uma lista de fibonate até determinado limite
    :param limite: int
    :return: list
    '''

    proximo = 0
    anterior = 0
    fibonacci_list = []
    while (proximo < limite):
        fibonacci_list.append(proximo)
        proximo = proximo + anterior
        anterior = proximo - anterior
        if(proximo == 0):
            proximo += 1
    return fibonacci_list