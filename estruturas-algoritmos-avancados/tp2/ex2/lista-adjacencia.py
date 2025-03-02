grafo = {
    'Centro': ['Gonzalés', 'Grajaú', 'Humberto Antunes'],
    'Gonzalés': ['Centro', 'Santa Rita', 'Tupinambá'],
    'Humberto Antunes': ['Centro', 'Morro do Mathias'],
    'Morro do Mathias': ['Humberto Antunes'],
    'Santa Rita': ['Gonzalés'],
    'Tupinambá': ['Gonzalés'],
    'Grajaú': ['Centro', 'Bela Vista'],
    'Bela Vista': ['Grajaú', 'Independência'],
    'Independência': ['Bela Vista']
}


for bairro, conexoes in grafo.items():
    print(f"{bairro} -> {', '.join(conexoes)}")
