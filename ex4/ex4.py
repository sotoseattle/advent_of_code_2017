def has_duplo(passphrase):
    words = passphrase.split(' ')
    return len(set(words)) != len(words)

def is_anagram(passphrase):
    words = passphrase.split(' ')
    zen = len(words)

    for i in range(0, zen):
        w1 = sorted(list(words[i])) 
        for j in range(i+1, zen):
            if w1 == sorted(list(words[j])):
                return True
    return False 

def valid_passphrases(inputo, func):
    phrases = inputo.splitlines()
    return len(phrases) - sum([func(l) for l in phrases])

