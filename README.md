# Parcial-1-de-programacion-computacional-3
# Estudiantes:
# Justin Steven Franco Martinez
# Roobin Edgardo Sorto Hernández
#  ¿Qué ventajas tiene en comparación con poner todo el código en un solo archivo o utilizar módulos?

# Organización: al dividir el programa en partes (funciones, clases o módulos), el código es más fácil de entender y mantener. 
# Reutilización: si separás el código en módulos o clases, podés usarlos en otros proyectos sin tener que reescribir todo.

#  ¿Qué ventajas tiene en comparación con poner todo el código en un solo archivo o utilizar módulos?

# Usamos funciones (registrar_venta y mostrar_resumen) para separar responsabilidades.

# Facilita leer y entender qué hace cada parte.

# Permite reutilizar funciones (ejemplo: registrar_venta se puede llamar varias veces sin repetir lógica).

# Hace que sea más fácil modificar o ampliar el sistema (ejemplo: agregar una función que guarde las ventas en un archivo).


#  ¿Cómo aplicaron la Programación Orientada a Objetos en su solución? Describan el papel de las clases creadas

# El código que te pasé es funcional si lo llevamos a Programación Orientada a Objetos (POO), podríamos crear una clase como esta:

# class Venta:
#    def _init_(self, producto, precio, cantidad):
 #       self.producto = producto
  #      self.precio = precio
  #      self.cantidad = cantidad
    
   # def calcular_ingreso(self): return self.precio * self.cantidad
# Y luego otra clase para el sistema de ventas:

# class SistemaVentas:
   # def _init_(self): self.ventas = []
    
# def registrar_venta(self, producto, precio, cantidad):
# venta = Venta(producto, precio, cantidad) 
# self.ventas.append(venta)
    
   # def calcular_total(self):return sum(v.calcular_ingreso() for v in self.ventas)

# En este enfoque nos ayuda a presentarlas de forma individual

# La clase SistemaVentas organiza todas las ventas y calcula los totales.

# Esto aplica la POO al separar entidades y encapsular sus datos y comportamientos.

# ¿De qué manera el uso de GitHub facilitó el trabajo colaborativo en equipo? Den un ejemplo concreto
# Nos facilito en la ofrma de que es mas rapido el poder aser este trabajo ya que solo hay que poner un comid yel otro integrante solo tubo que poner pull y asi sincronizo de manera casi instantanea el codigo

