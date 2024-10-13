import pandas as pd

# Caminho para o arquivo Excel
arquivo_excel = 'C:\Users\hgcca\OneDrive\Documentos\FINANÇAS\Contas.xlsx'

# Lendo a planilha do Excel (use a aba por nome ou índice)
df = pd.read_excel(arquivo_excel)  # ou use o número da aba: sheet_name=0

# Exibe as primeiras linhas do DataFrame
print(df.head())

# Exemplo de manipulação - substituindo valores vazios por 0
df.fillna(0, inplace=True)

# Salvando as mudanças de volta no arquivo Excel
df.to_excel('caminho_para_o_arquivo_modificado.xlsx', index=False)