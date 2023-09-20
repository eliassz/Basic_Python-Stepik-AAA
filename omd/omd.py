# Guido van Rossum <guido@python.org>
def step2_umbrella():
    print('Утка-маляр 🦆 взяла зонтик ☂️ и пошла в бар.')
    print('*звуки довольной утки, идущей под зонтиком*')


def step2_no_umbrella():
    print('Утка-маляр 🦆 решила не брать зонтик ☂️ и пошла в бар под дождем.')
    print('*звуки довольной утки, идущей без зонтика*')
    print('вопрос к читателю: а зачем ей зонтик, если утки не мокнту?')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
