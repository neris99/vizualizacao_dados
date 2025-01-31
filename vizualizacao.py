import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head().to_string())

# Gráfico de Histograma
plt.hist(df['Nota'])
plt.xlabel('Nota')
plt.show()

# Gráfico de dispersão
sns.jointplot(x='Nota', y='N_Avaliações', data=df, kind='scatter')
plt.show()

# Mapa de calor
calor = df[['Nota', 'Desconto']].corr()
plt.subplot(2,2,1)
sns.heatmap(calor, annot=True, cmap='coolwarm')
plt.title('Correlação Nota e Desconto')
plt.tight_layout()
plt.show()

# Gráfico de barra
plt.figure(figsize=(10,8))
df['Qtd_Vendidos'].value_counts().plot(kind='bar', color='#DAA520')
plt.title('Dispersão quantidade vendido')
plt.xlabel('Faixa valor vendido')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()


# Gráfico de pizza
plt.figure(figsize=(10,6))  # Parêntese corrigido
plt.pie(df['Gênero'].value_counts().values,
        labels=df['Gênero'].value_counts().index,
        autopct='%.2f%%',
        startangle=90)
plt.title('Distribuição dos Gêneros')
plt.show()


df = df.dropna(subset=['Nota'])
# Gráfico de densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['Nota'], fill=True, color='#FF7F50')
plt.title('Densidade da Nota')
plt.xlabel('Nota')
plt.ylabel('Densidade')
plt.show()


df = df.dropna(subset=['Desconto'])
# Gráfico de Regressão
sns.regplot(x='Nota', y='Desconto', data=df, color='#EEE8AA', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Nota e Desconto')
plt.xlabel('Nota')
plt.ylabel('Desconto')
plt.show()
