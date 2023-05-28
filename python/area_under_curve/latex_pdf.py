import os
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from pylatex import Document, Section, Subsection, Math, Command, Figure

def main(var, fun, sup, inf):
    # Variable de integración
    variable = sp.Symbol(var)
    # Definición de la función
    funcion = sp.sympify(fun)
    # Tipo de función
    funcion_tipo = input('Es una función trigonométrica?: ')
    if funcion_tipo == 'si':
        # Intervalo de integración
        a = inf*sp.pi  # Límite inferior del intervalo
        b = sup*sp.pi # Límite superior del intervalo
    else:
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

    # Obtener la ruta del script actual
    script_path = os.path.dirname(os.path.abspath(__file__))

    # Guardar la figura como imagen en la ruta del script
    plot_path = os.path.join(script_path, 'plot.png')
    plt.savefig(plot_path)

    # Crear el documento LaTeX en la ruta del script
    doc_path = os.path.join(script_path, 'resultado.tex')
    doc = Document(doc_path)

    # Agregar sección
    with doc.create(Section('Resultado')):
        # Agregar expresión LaTeX renderizada
        doc.append('Expresión:')
        doc.append(Math(data=sp.latex(funcion), escape=False))
        doc.append('Resultado:')
        doc.append(Math(data=sp.latex(area), escape=False))

        # Agregar figura al documento
        with doc.create(Subsection('Gráfica')):
            with doc.create(Figure(position='htbp')) as plot:
                plot.add_image(plot_path, width='300px')
                plot.add_caption('Gráfica de la curva')

    # Guardar el PDF en la ruta del script
    pdf_path = os.path.join(script_path, 'resultado.pdf')
    doc.generate_pdf(pdf_path, clean_tex=False)

    # Mostrar el área calculada
    print(f'El área bajo la curva es: {area}')

    # Mostrar la ruta del archivo PDF
    print(f'PDF guardado en: {pdf_path}')

if __name__ == "__main__":
    sp.init_printing()
    var = input('Digite la variable: ')
    fun = input('Digite la función: ')
    inf = int(input('Digite el valor del límite inferior: '))
    sup = int(input('Digite el valor del límite superior: '))
    main(var, fun, sup, inf)
