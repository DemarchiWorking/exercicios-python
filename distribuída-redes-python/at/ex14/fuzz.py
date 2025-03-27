import requests

# Lista de entradas para fuzzing (endpoints e parâmetros)
fuzz_inputs = [
    "/", "/admin", "/login", "/test", "/vulnerable", "/config",
    "?id=1", "?user=admin", "?debug=true", "?param=<script>alert('XSS')</script>"
]


# Função de fuzzing
def fuzzing(server_url):
    for input_path in fuzz_inputs:
        try:
            url = server_url + input_path
            response = requests.get(url)

            print(f"Testando: {url} | Status: {response.status_code}")

            if response.status_code == 200:
                print("-> Possível endpoint válido encontrado!")
            elif response.status_code == 500:
                print("-> Vulnerabilidade potencial detectada (500 - Erro do Servidor).")
        except Exception as e:
            print(f"Erro ao testar {url}: {e}")


# Executando fuzzing
server_url = input("Digite o URL do servidor (exemplo: http://localhost): ")
fuzzing(server_url)
