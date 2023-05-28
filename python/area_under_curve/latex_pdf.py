import sympy as sp
from pylatex import Document, Section, Subsection, Math, Command

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

    # Crear el documento LaTeX
    doc = Document()

    # Agregar sección
    with doc.create(Section('Resultado')):
        # Agregar expresión LaTeX renderizada
        doc.append('Expresión:')
        doc.append(Math(data=sp.latex(funcion), escape=False))
        doc.append('Resultado:')
        doc.append(Math(data=sp.latex(area), escape=False))

    # Guardar el PDF
    doc.generate_tex()
    doc.generate_pdf('resultado', clean_tex=False)

    # Mostrar el área calculada
    print(f'El área bajo la curva es: {area}')

    # Mostrar el nombre del archivo PDF
    print('PDF guardado como "resultado.pdf"')

if __name__ == "__main__":
    sp.init_printing()
    var = input('Digite la variable: ')
    fun = input('Digite la función: ')
    inf = int(input('Digite el valor del límite inferior: '))
    sup = int(input('Digite el valor del límite superior: '))
    main(var, fun, sup, inf)

