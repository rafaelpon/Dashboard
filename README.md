# Dashboard
Projeto de Desenvolvimento de Dashboard

Objetivo do Projeto:
O objetivo deste projeto é permitir que os alunos apliquem seus conhecimentos de Estatística e comecem a entrar na área de Data Science, utilizando a biblioteca Pandas para análise de dados e a biblioteca Dash para criar um dashboard interativo. Os alunos selecionarão um conjunto de dados do Kaggle, realizarão análises exploratórias, aplicarão tratamentos de dados e, por fim, criarão um dashboard que apresente visualizações significativas dos dados.

Passo 1: Instalação de Pacotes
Certifique-se de que você já instalou os pacotes necessários. Você pode instalar os pacotes usando o seguinte comando:
pip install dash dash-bootstrap-templates plotly pandas

Passo 2: Importação de Bibliotecas
from dash import Dash, html, dcc, Input, Output import plotly.express as px import pandas as pd from app import * from dash_bootstrap_templates import ThemeSwitchAIO 

Passo 3: Carregamento dos Dados
Neste exemplo, um DataFrame é carregado a partir de um arquivo CSV. Certifique-se de ter um arquivo CSV válido e defina o caminho correto para o seu arquivo. Substitua r'X:\XXXXX\XXXXX \SUAPASTA\SEUSDADOS.csv' pelo caminho do seu arquivo CSV.
Dados utilizados:https://www.kaggle.com/datasets/inductiveanks/employee-salaries-for-different-job-roles

Passo 4: Definição das Funções de Gráfico
O código contém duas funções para criar gráficos: create_graph e create_comparison_graph. Você pode personalizar essas funções para ajustar o estilo, os rótulos e outros atributos dos gráficos de acordo com suas necessidades.

Passo 5: Criação da Aplicação Dash

Passo 6: Definição do Layout da Aplicação
O layout da aplicação é definido usando objetos HTML e componentes Dash. Você pode personalizar esse layout para atender às suas preferências de design.

Passo 7: Callbacks
O código define três callbacks para atualizar os gráficos quando os valores dos seletores são alterados. Os callbacks são definidos usando a anotação @app.callback e especificam as entradas e saídas de cada função de callback.
update_output: Atualiza o gráfico de montante de salário de acordo com o nível de experiência.
update_comparison_output: Atualiza o gráfico de comparação de maiores salários.
update_boxplot: Atualiza o gráfico de boxplot para um cargo específico.
Você pode personalizar essas funções de callback para ajustar o comportamento dos gráficos de acordo com suas necessidades.

Passo 8: Execução da Aplicação
Por fim, a aplicação é executada usando o seguinte trecho de código:
if __name__ == '__main__': app.run_server(debug=True) 
Quando você executa este código, a aplicação Dash será iniciada e você poderá acessá-la em seu navegador. Certifique-se de ter o arquivo app.py referenciado corretamente ou substitua-o pelo nome do seu arquivo principal, se necessário.
