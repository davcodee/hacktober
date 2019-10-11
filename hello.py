def suma(x,y):
  """Esta funcion hace una suma"""
  res=x+y
  return res

def resta(x,y):
  """Esta funcion hace una resta"""
  return x-y


def division(x,y):
  """Esta funcion hace una division"""
  div = x/y
  return div

def multiplicacion(x,y):
  """Esta funcion hace una multiplicacion"""
  m = x*y
  return m

def modulo(x,y):
  """Esta funcion hace una suma"""

def potencia(x,n):
	return x ** n

def factorial(n):
	if n == 1:
		return n

	else: 
		return  n * factorial(n-1)

print(potencia(5,2))
if __name__ == "__main__":
    print(division(10,5))
    print(factorial(5))
