import hashlib

def hash_password(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

senha = input("senha: ")
senha_hash = hash_password(senha)

print(senha_hash)
print(len(senha_hash))