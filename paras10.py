import hashlib

pass_found = 0
i_hash = input("Enter the hashed form of password: ")
p_doc = input("Enter the password file name including path: ")

with open(p_doc, "r") as p_file:
    for word in p_file:
        word = word.strip()
        enc_word = word.encode("UTF-8")
        hash_word = hashlib.md5(enc_word)
        digest = hash_word.hexdigest()
        if digest == i_hash:
            print("Your Password:", word)
            pass_found = 1
            break

if not pass_found:
    print("Password not found")
