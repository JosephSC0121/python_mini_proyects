import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def main(var, fun, sup, inf):
    # Variable de integración
    variable = sp.Symbol(var)
    # Definición de la función
    funcion = sp.sympify(fun)
    # Tipo de funcion
    funcion_tipo = input('Es una funcion trigonometrica?: ')
    if funcion_tipo == 'si':
        # Intervalo de integración
        a = inf*sp.pi  # Límite inferior del intervalo
        b = sup*sp.pi # Límite superior del intervalo
    else :
        a = inf
        b = sup
    # Cálculo del área utilizando la función de SymPy
    area = sp.integrate(funcion, (variable, a, b))

    # Graficar la curva y el área bajo la curva
    x_vals = np.linspace(0, 10, 100)
    f = sp.lambdify(variable, funcion, modules='numpy')
    y_vals = f(x_vals)
    

    plt.plot(x_vals, y_vals, 'b', linewidth=1)
    plt.fill_between(x_vals, y_vals, where=((x_vals >= a) & (x_vals <= b)), color='black')
    plt.title('Area bajo la curva')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    print(f'El área bajo la curva es: {area}')
    # Mostrar la gráfica
    plt.show()

if __name__ == "__main__":
    var = input('Digite la variable: ')
    fun = input('Digite la función: ')
    inf = int(input('Digite el valor del limite inferior: '))
    sup = int(input('Digite el valor del limite superior: '))
    main(var, fun, sup, inf)

