from selenium import webdriver 
import pandas

#abrindo o navegador 
navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br/?hl=pt-BR")

#lendo a tabela
tabela = pandas.read_excel("commodities.xlsx")

#selecionando a linha da tabela, fazendo a busca e adicionando a informação
for linha in tabela.index:

    produto = tabela.loc[linha,'Produto']
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    link = link.replace('é', 'e').replace('ã', 'a').replace('á', 'a').replace('ç','c').replace('ú','u').replace('ó','o')
    navegador.get(link)
    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace('.', '').replace(',', '.')
    cotacao = float(cotacao)

    tabela.loc[linha, "Preço Atual"] = cotacao
#comparando
tabela["Comprar"] = tabela["Preço Ideal"] > tabela["Preço Atual"]
print(tabela)
navegador.quit()

#criando um arquivo com a nova tabela
tabela.to_html("newtabela.html")



