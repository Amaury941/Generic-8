import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n_classes = 7
x = pd.read_csv('a.csv')
data = {
  'Rondônia':0, 
  'Acre':0, 
  'Amazonas':0, 
  'Roraima':0, 
  'Pará':0, 
  'Amapá':0, 
  'Tocantins':0, 
  'Maranhão':0, 
  'Piauí':0,
  'Ceará':0, 
  'Rio Grande do Norte':0, 
  'Paraíba':0,
  'Pernambuco':0, 
  'Alagoas':0, 
  'Sergipe':0,
  'Bahia':0, 
  'Minas Gerais':0, 
  'Espírito Santo':0, 
  'Rio de Janeiro':0,
  'São Paulo':0, 
  'Panamá':0, 
  'Santa Catarina':0, 
  'Rio Grande do Sul':0, 
  'Mato Grosso do Sul':0,
  'Mato Grosso':0, 
  'Goiás':0, 
  'Distrito federal':0,
}
frequencias = [
  ['001-122',0,0],
  ['123-244',0,0],
  ['245-366',0,0],
  ['367-488',0,0],
  ['489-610',0,0],
  ['611-732',0,0],
  ['733-855',0,0]
]

def calcular_data (x,data):
  for n in x['estado']:
    data[str(n)] += 1
  return data

def calcular_lista (data):
  lista = [] 
  for n in data:
    lista.append(data[n])
  return lista

def calcular_amplitude (maior,menor,n_classes): return round((maior - menor)/n_classes)

def calcular_limites(menor,n_classes,amplitude_classe):
  limites = [menor]
  for i in range(n_classes):
    limites.append(limites[i]+amplitude_classe)
  return limites

def calcular_frequencia(frequencias,lista,limites_inf):
  for numero in lista:
    limites_index = 1
    zetr(numero,limites_inf,limites_index,frequencias)
  return frequencias

def zetr (numero,limites,limites_index,frequencias):
  if limites_index < len(limites):
    if numero < limites[limites_index]:
      frequencias[limites_index-1][1] += 1
      return frequencias
    limites_index += 1
    zetr (numero,limites,limites_index,frequencias)

def calcular_frequencia_relativa(lista,frequencias):
  for classe in frequencias:
    classe[2] = 100*(classe[1]/len(lista))
  return frequencias

def calcular_moda(data,temp='',temp0=0):
  for ds in data:
    if data[ds] > temp0:
      temp,temp0 = ds,data[ds]
  return temp 

def calcular_media(lista): return sum(lista)/len(lista)

def calcular_mediana(listaS):
    if len(listaS)%2 == 0:
      mediana = (listaS[int(len(listaS)/2-1)] + listaS[int(len(listaS)/2)])/2
    else:
      mediana = listaS[int(len(listaS)/2-1)]
    return mediana

def calcular_variancia(lista,var=0):
  media =calcular_media(lista)
  for numero in lista:
    var += (numero - media)**2
  var = var/len(lista)
  return var

def calcular_desvio_padrão(lista):
    return calcular_variancia(lista)**(1/2)

def mostrar_graficos (lista,data):

    plt.boxplot(lista)
    plt.title('Boxplot da Distribuição de cidades por unidade federativa')
    plt.xlabel('Número de cidades')
    plt.grid()

    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = np.arange(len(data.keys()))
    ax.barh(y_pos, lista, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(data.keys())
    ax.invert_yaxis()
    ax.set_xlabel('Número de cidades')
    ax.set_title('Distribuição de cidades por unidade federativa')
    plt.show()

def mostrar_frequencias(frequencias):
      print("\n|Classe |  Frequência  |")
      for classe in frequencias:
        print (
          "|%s| %2i (%s%s) |" % 
          (classe[0],classe[1],
          (("%2i"%classe[2])+
          (
            "%.3f"%(classe[2]-
            int("%2i"%classe[2])))[1:]
          ),
          "%")
        )

def quicksort(arr):
    if len(arr) <= 1: return arr
    m = arr[0]
    return quicksort([i for i in arr if i < m]) + \
        [i for i in arr if i == m] + \
        quicksort([i for i in arr if i > m])

def main (n_classes, x, data, frequencias):
    data             = calcular_data (x,data)
    lista            = calcular_lista (data)
    listaS           = quicksort(lista)
    maior            = max(lista)
    menor            = min(lista)
    amplitude_classe = calcular_amplitude (maior,menor,n_classes)
    limites          = calcular_limites(menor,n_classes,amplitude_classe)
    frequencias      = calcular_frequencia(frequencias,lista,limites)
    frequencias      = calcular_frequencia_relativa(lista,frequencias)

    q2 = (calcular_mediana(listaS))
    q1 = (calcular_mediana(listaS[0:listaS.index(q2)]))
    q3 = (calcular_mediana(listaS[listaS.index(q2):]))

    print (
      '\nMédia de cidades: %.2f\nMediana de cidades: %.2f\nModa de estados: %s\nVariância: %.2f\nDesvio padrão: %.2f' 
      %(
        calcular_media(lista),
        calcular_mediana(listaS),
        calcular_moda(data),
        calcular_variancia(lista),
        calcular_desvio_padrão(lista)
      )
    )
    print ('\n| Mínimo: %s | Q1: %s | Q2: %s | Q3: %s | Máximo: %s |' % (menor,q1,q2,q3,maior))
    mostrar_frequencias(frequencias)
    mostrar_graficos (lista,data)

main (n_classes, x, data, frequencias)
