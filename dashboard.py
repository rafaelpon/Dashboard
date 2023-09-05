from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Importação do arquivo 'app.py' 
from app import *
# Importação do tema COSMO e SUPERHERO do Dash Bootstrap
from dash_bootstrap_templates import ThemeSwitchAIO

# Definição dos URLs dos temas e dos nomes dos temas
url_theme1 = dbc.themes.COSMO
url_theme2 = dbc.themes.SUPERHERO
template_theme1 = 'cosmo'
template_theme2 = 'superhero'

# Carregamento do DataFrame a partir de um arquivo CSV
df = pd.read_csv(r'XXXXXXXXXXXXXXXX\dados_tratados.csv')

# Filtragem dos maiores salários para cada título de cargo
max_salaries = df.groupby('job_title')['salary_in_usd'].max().reset_index()

# Função para criar o gráfico inicial
def create_graph(data, toggle):
    templates = template_theme1 if toggle else template_theme2
    fig = px.bar(data, x="job_title", y="salary_in_usd", color="experience_level", barmode="group", template=templates)
    fig.update_layout(
        xaxis_title="Título do Trabalho",
        yaxis_title="Montante de Salário (USD)",
        legend_title="Nível de Experiência",
        
    )
    return fig

# Função para criar o gráfico de comparação de maiores salários
def create_comparison_graph(data, toggle):
    templates = template_theme1 if toggle else template_theme2
    fig = px.bar(data, x="job_title", y="salary_in_usd", barmode="group", template=templates)
    fig.update_layout(
        xaxis_title="Título do Trabalho",
        yaxis_title="Maior Montante de Salário (USD)"
    )
    return fig

# Layout da aplicação
app.layout = html.Div(style={'margin': '40px','margin-left': '300px', 'margin-right': '300px'}, children=[
    ThemeSwitchAIO(aio_id='theme', themes=[url_theme1, url_theme2]),
    html.H1(children='Projeto Dashboard'),
    html.H2(children='Gráfico do Montante de Salário de acordo com o nível de experiência'),
    html.Div(children='''
        Obs: Para verificar os maiores salários, aproxime o mouse.
    '''),

    dcc.Dropdown(options=[
        {"label": title, "value": title} for title in df['job_title'].unique()
    ], value=[df['job_title'].iloc[0]], multi=True, id='job_title_selector'),

    dcc.Graph(
        id='grafico_salario_experiencia'
    ),

    html.Div(style={'height': '50px'}),  # Espaço entre os gráficos

    html.H2(children='Comparação de Maiores Salários por Cargo'),
    dcc.Dropdown(options=[
        {"label": title, "value": title} for title in df['job_title'].unique()
    ], value=[df['job_title'].iloc[0]], multi=True, id='comparison_job_title_selector'),

    dcc.Graph(
        id='grafico_comparacao_maiores_salarios'
    ),

    html.Div(style={'height': '50px'}),  # Espaço entre os gráficos

    html.H2(children='Gráfico de Boxplot para um Cargo'),

    # Organize os gráficos de boxplot lado a lado usando o layout das colunas
    html.Div([
        html.Div([
            dcc.Dropdown(options=[
                {"label": title, "value": title} for title in df['job_title'].unique()
            ], value=df['job_title'].iloc[0], id='boxplot_job_title_selector_1'),  # Seleção única

            dcc.Graph(
                id='grafico_boxplot_1'
            ),
        ], className='col'),  # Define a largura da coluna

        html.Div([
            dcc.Dropdown(options=[
                {"label": title, "value": title} for title in df['job_title'].unique()
            ], value=df['job_title'].iloc[0], id='boxplot_job_title_selector_2'),  # Seleção única

            dcc.Graph(
                id='grafico_boxplot_2'
            ),
        ], className='col'),  # Define a largura da coluna
    ], className='row'),  # Define uma linha para os gráficos

])

# Callback para atualizar o gráfico de montante de salário de acordo com o nível de experiência
@app.callback(
    Output('grafico_salario_experiencia', 'figure'),
    Input('job_title_selector', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def update_output(selected_titles, toggle):
    filtered_data = df[df['job_title'].isin(selected_titles)]
    fig = create_graph(filtered_data, toggle) 
    return fig

# Callback para atualizar o gráfico de comparação de maiores salários
@app.callback(
    Output('grafico_comparacao_maiores_salarios', 'figure'),
    Input('comparison_job_title_selector', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def update_comparison_output(selected_titles, toggle):
    filtered_data = max_salaries[max_salaries['job_title'].isin(selected_titles)]
    comparison_fig = create_comparison_graph(filtered_data, toggle)
    return comparison_fig


# Callback para atualizar o gráfico de boxplot para um cargo (primeiro gráfico)
@app.callback(
    Output('grafico_boxplot_1', 'figure'),  # Alterado para 'grafico_boxplot_1'
    Input('boxplot_job_title_selector_1', 'value'),  # Alterado para 'boxplot_job_title_selector_1'
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def update_boxplot_1(selected_title, toggle):
    templates = template_theme1 if toggle else template_theme2

    filtered_data = df[df['job_title'] == selected_title]
    boxplot_fig = px.box(filtered_data, x='salary_in_usd', points='all', template=templates)
    
    return boxplot_fig

# Callback para atualizar o gráfico de boxplot para um cargo (segundo gráfico)
@app.callback(
    Output('grafico_boxplot_2', 'figure'),
    Input('boxplot_job_title_selector_2', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def update_boxplot_2(selected_title, toggle):
    templates = template_theme1 if toggle else template_theme2

    filtered_data = df[df['job_title'] == selected_title]
    boxplot_fig = px.box(filtered_data, x='salary_in_usd', points='all', template=templates)
    
    return boxplot_fig

# Execução da aplicação
if __name__ == '__main__':
    app.run_server(debug=True)

