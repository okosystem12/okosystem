import random

try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    import warnings

    warnings.warn('A secure pseudo-random number generator is not available '
                  'on your system. Falling back to Mersenne Twister.')
    using_sysrandom = False


# Клас рандомизатор
class SetRandom:
    # Числовой (int) рандомизатор с указанием количества символов
    def int_random(self=5, allowed_chars='0123456789'):
        return int(''.join(random.choice(allowed_chars) for i in range(self)))

    # Строковый рандомизатор с указанием количества символов
    def text_random(self=44, allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                           'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
        if not using_sysrandom:
            random.seed(
                hashlib.sha256(
                    ("%s%s" % (
                        random.getstate(),
                        time.time())).encode('utf-8')
                ).digest())
        return ''.join(random.choice(allowed_chars) for i in range(self))
