from os import getlogin
login = getlogin()

try:
    carregaDicionario = open(f'C:/Users/{login}/Desktop/beto/infos.txt', 'r')
except:
    open(f'C:/Users/{login}/Desktop/beto/infos.txt', 'w').write('{}')
    carregaDicionario = open(f'C:/Users/{login}/Desktop/beto/infos.txt', 'r')

dicionario = dict(eval(carregaDicionario.read()))
carregaDicionario.close()

try:
    carregaBooks = open(f'C:/Users/{login}/Desktop/beto/books.txt', 'r')
except:
    open(f'C:/Users/{login}/Desktop/beto/books.txt', 'w').write('[]')
    carregaBooks = open(f'C:/Users/{login}/Desktop/beto/infos.txt', 'r')
books = list(eval(carregaBooks.read()))
carregaDicionario.close()
carregaBooks.close()
print('Bem-Vindo ao cadastrador de ligas do Beto!')
while True:
    liga = input('Insira a liga, ou 0 para parar: ')
    try:
        dicionarioURLs = dicionario[liga]['urls']
    except:
        dicionarioURLs = {}
    for book in books:
        if book not in dicionario[liga]['urls'].keys():
            url = input(f'Insira a URL dela em {book}, ou 0 para sair:  ')
            chaveURLBook = {book: url}
            dicionarioURLs.update(chaveURLBook)
    chave = {liga: {'urls': dicionarioURLs, 'mercados': {}}}
    mercado = input('Que mercado deseja cadastrar? (Pressione 0 para sair): ')
    try:
        dicionarioVisitante = dicionario[liga]['mercados'][mercado]['Visitante']
        dicionarioCasa = dicionario[liga]['mercados'][mercado]['Casa']
        dicionarioMercado = dicionario[liga]['mercados'][mercado]
    except:
        dicionarioVisitante = {}
        dicionarioCasa = {}
        dicionarioMercado = {mercado: {}}
    for book in books:
        if book not in list(dicionario[liga]['mercados'][mercado]['Visitante'].keys()):
            if book != 'BetWay':
                xpathVisitante = input(f'Insira o xpath da odd de {mercado} do time visitante em {book}: ')
                xpathCasa = input(f'Insira o xpath da odd de {mercado} do time de casa em {book}: ')
                dicionarioVisitante.update({book: xpathVisitante})
                dicionarioCasa.update({book: xpathCasa})
                dicionarioMercado.update({'Visitante': dicionarioVisitante})
                dicionarioMercado.update({'Casa': dicionarioCasa})
    chave[liga]['mercados'].update({mercado: dicionarioMercado})
    if input('Deseja continuar?\n[0] - Sim\n[1] - Não\n') == '1':
        break
salvaDicionario = open(f'C:/Users/{login}/Desktop/beto/infos.txt', 'w')
salvaDicionario.write(str(chave))
salvaDicionario.close()
print('Informações atualizadas!')
