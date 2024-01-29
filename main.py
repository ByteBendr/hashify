# Imports
import hashlib
import argon2
import base64
from click import pause
import os
import colorama
from colorama import init, Style, Fore

# Color Constants
RED = Fore.LIGHTRED_EX + Style.BRIGHT
GREEN = Fore.LIGHTGREEN_EX + Style.BRIGHT
BLUE = Fore.LIGHTBLUE_EX + Style.BRIGHT
YELLOW = Fore.LIGHTYELLOW_EX + Style.BRIGHT
CYAN = Fore.LIGHTCYAN_EX + Style.BRIGHT
MAGENTA = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
WHITE = Fore.LIGHTWHITE_EX + Style.BRIGHT
RESET = Style.RESET_ALL


# Main Function

os.system('cls')

def main():
    
    print(f'''{CYAN}

██╗  ██╗ █████╗ ███████╗██╗  ██╗██╗███████╗██╗   ██╗
██║  ██║██╔══██╗██╔════╝██║  ██║██║██╔════╝╚██╗ ██╔╝
███████║███████║███████╗███████║██║█████╗   ╚████╔╝ 
██╔══██║██╔══██║╚════██║██╔══██║██║██╔══╝    ╚██╔╝  
██║  ██║██║  ██║███████║██║  ██║██║██║        ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝{RESET} {RED}by ByteBendr{RESET}
================================================================\n''')


    text = input(f"{WHITE}> Input your message: {RESET}")
    
    #MD5
    md5hash = hashlib.md5()
    md5hash.update(text.encode())
    md5 = md5hash.hexdigest()
    
    #SHA1
    sha1hash = hashlib.sha1()
    sha1hash.update(text.encode())
    sha1 = sha1hash.hexdigest()
    
    #SHA256
    sha256hash = hashlib.sha256()
    sha256hash.update(text.encode())
    sha256 = sha256hash.hexdigest()
    
    #SHA384
    sha384hash = hashlib.sha256()
    sha384hash.update(text.encode())
    sha384 = sha384hash.hexdigest()
    
    #SHA512
    sha512hash = hashlib.sha512()
    sha512hash.update(text.encode())
    sha512 = sha512hash.hexdigest()
    
    #BLAKE2b
    blake2bhash = hashlib.blake2b()
    blake2bhash.update(text.encode())
    blake2b = blake2bhash.hexdigest()
    
    #BLAKE2s
    blake2shash = hashlib.blake2s()
    blake2shash.update(text.encode())
    blake2s = blake2shash.hexdigest()
    
    #RIPEMD-160
    ripemd160hash = hashlib.new("ripemd160")
    ripemd160hash.update(text.encode())
    ripemd160 = ripemd160hash.hexdigest()
    
    #ARGON2
    argon2hash = argon2.PasswordHasher().hash(text)
    
    #BASE64
    base64encoded = base64.b64encode(text.encode()).decode()
    
    #Printing hashed results
    print("\n==============================================================================================================================================")
    print(f'> {WHITE} MD5 (cannot be decoded) = {RESET} {GREEN}{md5}{RESET}')
    print(f'> {WHITE} SHA1 (cannot be decoded) = {RESET} {GREEN}{sha1}{RESET}')
    print(f'> {WHITE} SHA256 (cannot be decoded) = {RESET} {GREEN}{sha256}{RESET}')
    print(f'> {WHITE} SHA384 (cannot be decoded) = {RESET} {GREEN}{sha384}{RESET}')
    print(f'> {WHITE} SHA512 (cannot be decoded) = {RESET} {GREEN}{sha512}{RESET}')
    print(f'> {WHITE} BLAKE2b (cannot be decoded) = {RESET} {GREEN}{blake2b}{RESET}')
    print(f'> {WHITE} BLAKE2s (cannot be decoded) = {RESET} {GREEN}{blake2s}{RESET}')
    print(f'> {WHITE} RIPEMD-160 (cannot be decoded) = {RESET} {GREEN}{ripemd160}{RESET}')
    print(f'> {WHITE} ARGON2 (cannot be decoded) = {RESET} {GREEN}{argon2hash}{RESET}')
    print(f'> {WHITE} BASE64 (can be decoded) = {RESET} {GREEN}{base64encoded}{RESET}')
    print("==============================================================================================================================================\n")
    
    # Await for input to quit
    pause(f"> {RED}Press any key to exit...{RESET}")
    

# Execute Main Function
if __name__ == "__main__":
    main()