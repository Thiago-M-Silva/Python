import requests

# url = 'https://aczgdesafio.rj.r.appspot.com/passo1'
# response = requests.get(url)
# print(response.content) 

# url2 = 'https://aczgdesafio.rj.r.appspot.com/passo2'
# data = {"cpf": "072.304.161-08"}
# response2 = requests.post(url2, json=data)
# print(response2.text)

# url3 = 'https://aczgdesafio.rj.r.appspot.com/passo3'
# data = {"cpf": "072.304.161-08", "respostaQuestaoObjetiva": "7"}
# response2 = requests.post(url3, json=data)
# print(response2.text)

# url4 = 'https://aczgdesafio.rj.r.appspot.com/passo4'
# data = {"cpf": "072.304.161-08", "token": "0eb0a446e680355585c41f8f95e05bd5d6710b4d"}
# response2 = requests.get(url4, params=data)
# print(response2.text)

def identificaTriangulo(l1, l2, l3):
    if(l1 != l2 and l2 != l3 and l1 != l3):
        print("triangulo escaleno")
    elif(l1 == l2 and l1 == l3):
        print("triangulo equilatero")
    else:
        print("triangulo isosceles")
#testes
identificaTriangulo(3,4,5) #escaleno
identificaTriangulo(6,10,10) #isosceles
identificaTriangulo(20,20,20) #equilatero

