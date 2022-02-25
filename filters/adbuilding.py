"""
Class for maintain Advertisement
"""
#
# from profanity_filter import Filter
#
# bad_words_filter = Filter()


class Advert:
    def __init__(self, photo=None, adtype='', city='', forwarding='', bio='', price='', adtext=''):
        #при создании добавляем нулевое фото
        if photo is None:
            photo = []
        self.adtype = adtype
        self.city = city
        self.forwarding = forwarding
        self.photo = photo
        self.bio = bio
        self.price = price
        self.adtext = adtext

    # Генерируем ссылку на автора
    def createAuthorName(self, firstname='', lastname='', username='', userid=0):
        AuthorName  = f'Автор: [{firstname}'
        AuthorName += f' {lastname}' if lastname is not None else ''
        AuthorName += f', @{username}' if username is not None else ''
        AuthorName += f'](tg://user?id={userid})'
        return AuthorName

    def createADText(self, firstname='', lastname='', username='', userid=0):
        userlink = self.createAuthorName(firstname, lastname, username, userid)

        forwarding = ', #пересыл' if self.forwarding == 'Да' else ''

        # Убираем пробелы в хештегах и ограничиваем на длину 25 символов
        city = self.city.replace(" ", "")
        tcity = (city[:25]+'..') if len(city) > 25 else city
        tprice = (self.price[:25]+'..') if len(self.price) > 25 else self.price

        # Ограничиваем длину сообщения в 800 символов
        tbio = (self.bio[:800]+'..') if len(self.bio) > 800 else self.bio
        # Экранируем подчерки и звездочки для формата строки Markdown
        tbio = tbio.replace('_','\\_')
        tbio = tbio.replace('*','\\*')

        adtext = (f'#{self.adtype.replace(" ", "")}, '
                  f'#{tcity}'
                  f'{forwarding}\n'
                  f'{tbio}\n'
                  f'Цена: {tprice}\n\n'
                  f'{userlink}')

        # return bad_words_filter.clean(adtext)
