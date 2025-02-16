from loguru import logger
from parser import Parser


def main():
    # https://www.52shuku.vip/yanqing/am/h2QX.html
    logger.add('file.log',
               format='{time:YYYY-MM-DD at HH:mm:} | {level} | {message}',
               rotation='3 days',
               backtrace=True,
               diagnose=True)

    title = input("Введите название новелы:")
    url = input("Введите ссылку:")
    pars = Parser(title, url)
    print(pars.get_webpage(url))


if name == 'main':
    main()