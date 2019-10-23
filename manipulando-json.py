import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ],
  "itens": [
  	{"nome": "item 1", "preco": "12.30"},
  	{"nome": "item 2", "preco": "3.30"}
  ]
}

print(json.dumps(x) + "\n") # transforma o objeto em string corrida


print("Mostra um campo especifico: " + x['name'])

print("Mostra a lista de carros: " + str(x['cars']))

# Seleciona o 1 carro (linha zero) e a coluna model
print("Mostra o acesso a lista: " + str(x['cars'][0]['model']))

# Seleciona o 1 item (linha zero) e a coluna nome
print("Mostra o acesso a lista: " + str(x['itens'][0]['nome']))

# Mostra todos os nomes e precos da lista de itens
for item in x['itens']:
	print(item['nome'] + " " + item['preco'])
