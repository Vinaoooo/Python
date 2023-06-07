import pandas as pd

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)

##print (tabela_vendas)

# faturamento por loja 
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# quantidade de produtos vendidos por loja 
qnt_prod = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(qnt_prod)

# ticket medio por produto em cada loja
ticket = (faturamento['Valor Final'] / qnt_prod['Quantidade']).to_frame()
ticket = ticket.rename(columns={0: 'Ticket Medio'})
print(ticket)

#enviar um email com o relatorio
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'vinicius250703@outlook.com'
mail.Subject = 'Relatorio'
mail.HTMLBody = f'''

<p>Segue relatório de vendas .</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade vendida:</p>
{qnt_prod.to_html()}

<p>Ticket medio dos produtos por loja:</p>
{ticket.to_html(formatters={'Ticket Medio': 'R${:,.2f}'.format})}
'''
mail.Send()

print('Email enviado')

