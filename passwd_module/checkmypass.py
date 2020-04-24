import requests
import hashlib
import sys


def request_api_data(query_char):
    """ Api retorna resposta OK apenas quando enviamos um tipo hash com as cinco primeiras letras"""
    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Resposta: {res.status_code}, teste a API e tente novamente")
    return res


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    """Checa se a senha existe na resposta da API.
    Caso exista hashs na respostas, ele virão sem os cinco primeiros caracteres que foram enviados"""
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)

    return get_password_leak_count(response, tail)


def main(args):
    if len(args) <= 0:
        print("Nenhum argumento fornecido")

    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} foi achado {count} nos data sets do pwnedpasswords")
        else:
            print(f"{password} não foi achado")

#Refatorar para não utilizar argumentos da linha de comando por questão de segurança, por exemplo de um arquivo.txt
if __name__ = "__main__":
    sys.exit(main(sys.argv[1:]))
