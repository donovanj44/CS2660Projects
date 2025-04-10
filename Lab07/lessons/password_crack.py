import hashlib
import os


def hash_pw(plain_text) -> str:
    """
     Generate hash of plain text. Here we allow for passing in a salt
     explicitly. This is so you can tinker and see the results.

     Python's Hashlib provides all we need here. Documentation is at
     https://docs.python.org/3/library/hashlib.html.

     Here we use SHA-1. (Weak!) For stronger encryption, see: bcrypt,
     scrypt, or Argon2. Nevertheless, this code should suffice for an
     introduction to some important concepts and practices.

     A few things to note.

     If we supply a fixed salt (or don't use a salt at all), then the
     output of the hash function becomes predictable -- for a given
     algorithm, the same password will always produce the same result.

     If we allow our algorithm to generate a salt from a pseudorandom
     input (e.g., using os.urandom(60)) then the same password will
     produce different results. All we know is the length of the combined
     salt and password.

     If we wish to be able to authenticate, then we must store the salt
     with the hash. We facilitate this by prepending the salt to the hash.

     :param plain_text: str (user-supplied password)
     :return: str (ASCII-encoded salt + hash)
     """
    salt = os.urandom(20).hex()
    
    hashable = (salt + plain_text).encode('utf-8')
    this_hash = hashlib.sha1(hashable).hexdigest()  # hash w/ SHA-1 and hexdigest
    return salt + this_hash  # prepend hash and return


def authenticate(stored, plain_text) -> bool:
    """
    Authenticate user by comparing stored and computed hashes.
    
    :param stored: str (stored salt + hash)
    :param plain_text: str (user-supplied password)
    :return: bool
    """
    salt = stored[:40]
    stored_hash = stored[40:]
    
    hashable = (salt + plain_text).encode('utf-8')
    this_hash = hashlib.sha1(hashable).hexdigest()
    return this_hash == stored_hash