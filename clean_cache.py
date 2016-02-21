"""
Eliminar cache:
"""


def clean_cache():
    import os

    # Limpiamos Dropbox:
    os.system('rm -R ~/Dropbox/.dropbox.cache/*')
    print('Dropbox cleaned')

    # Limpiamos Firefox:
    os.system('rm -R ~/.cache/mozilla/*')
    print('Mozilla cleaned')

    # #Limpiamos thunderbird:
    # os.system('rm -R ~/.cache/mozilla/*')
    # print('Mozilla cleaned')

    # Limpiamos Chrome:
    os.system('rm -R ~/.cache/google-chrome')
    print('Chrome cleaned')

if __name__ == "__main__":
    clean_cache()
