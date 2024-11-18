import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests
import json

# Inicializa la app de Dash
app = dash.Dash(__name__)

# Layout de la página web con diseño moderno
app.layout = html.Div(
    style={
        'fontFamily': 'Arial, sans-serif', 
        'backgroundImage': 'url("https://client-setting-co-institucional-images.s3.amazonaws.com/1_nueva_reforma_policia_nacional_1_1f24b9704e.jpg")',  # Ruta de tu imagen de fondo
        'backgroundSize': 'cover',  # Asegura que la imagen cubra toda la pantalla
        'backgroundAttachment': 'fixed',  # Hace que la imagen quede fija cuando haces scroll
        'backgroundPosition': 'center',  # Centra la imagen
        'padding': '20px', 
        'height': '100vh'
    },
    
    children=[
        html.H1("Predicción de Crimen", style={'textAlign': 'center', 'color': 'white', 'fontWeight': '700', 'fontSize': '36px', 'marginBottom': '40px'}),

        # Diseño de entradas en tarjetas modernas
        html.Div([
            html.Div([  
                html.Label("Género:", style={'fontWeight': '600', 'color': '#4F4F4F', 'fontSize': '18px'}),
                dcc.Dropdown(
                    id='gender',
                    options=[
                        {'label': 'Masculino', 'value': 'MASCULINO'},
                        {'label': 'Femenino', 'value': 'FEMENINO'},
                        {'label': 'No Reportado', 'value': 'NO REPORTADO'}
                    ],
                    value='MASCULINO',
                    style={'width': '100%', 'padding': '12px', 'borderRadius': '10px', 'border': '1px solid #B8B8B8', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 'fontSize': '16px'}
                )
            ], style={'padding': '10px', 'backgroundColor': '#fff', 'borderRadius': '15px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px'}),

            html.Div([
                html.Label("Departamento:", style={'fontWeight': '600', 'color': '#4F4F4F', 'fontSize': '18px'}),
                dcc.Input(id='departamento', type='text', value='Boyacá', style={'width': '100%', 'padding': '12px', 'borderRadius': '10px', 'border': '1px solid #B8B8B8', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 'fontSize': '16px'})
            ], style={'padding': '10px', 'backgroundColor': '#fff', 'borderRadius': '15px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px'}),

            html.Div([
                html.Label("Municipio:", style={'fontWeight': '600', 'color': '#4F4F4F', 'fontSize': '18px'}),
                dcc.Input(id='municipio', type='text', value='Abejorral', style={'width': '100%', 'padding': '12px', 'borderRadius': '10px', 'border': '1px solid #B8B8B8', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 'fontSize': '16px'})
            ], style={'padding': '10px', 'backgroundColor': '#fff', 'borderRadius': '15px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px'}),

            html.Div([
                html.Label("Edad:", style={'fontWeight': '600', 'color': '#4F4F4F', 'fontSize': '18px'}),
                dcc.Input(id='edad', type='number', value=25, style={'width': '100%', 'padding': '12px', 'borderRadius': '10px', 'border': '1px solid #B8B8B8', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 'fontSize': '16px'})
            ], style={'padding': '10px', 'backgroundColor': '#fff', 'borderRadius': '15px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px'}),

            html.Div([
                html.Label("Arma:", style={'fontWeight': '600', 'color': '#4F4F4F', 'fontSize': '18px'}),
                dcc.Input(id='arma', type='text', value='ARMA DE FUEGO', style={'width': '100%', 'padding': '12px', 'borderRadius': '10px', 'border': '1px solid #B8B8B8', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 'fontSize': '16px'})
            ], style={'padding': '10px', 'backgroundColor': '#fff', 'borderRadius': '15px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px'}),

            html.Div([
                html.Label("Día de la semana:", style={'fontWeight': '600', 'color': '#4F4F4F', 'fontSize': '18px'}),
                dcc.Dropdown(
                    id='dia_semana',
                    options=[
                        {'label': 'Lunes', 'value': 'LUNES'},
                        {'label': 'Martes', 'value': 'MARTES'},
                        {'label': 'Miércoles', 'value': 'MIERCOLES'},
                        {'label': 'Jueves', 'value': 'JUEVES'},
                        {'label': 'Viernes', 'value': 'VIERNES'},
                        {'label': 'Sábado', 'value': 'SABADO'},
                        {'label': 'Domingo', 'value': 'DOMINGO'}
                    ],
                    value='VIERNES',
                    style={'width': '100%', 'padding': '12px', 'borderRadius': '10px', 'border': '1px solid #B8B8B8', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 'fontSize': '16px'}
                )
            ], style={'padding': '10px', 'backgroundColor': '#fff', 'borderRadius': '15px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px'}),

            html.Div([
                html.Label("Cantidad:", style={'fontWeight': '600', 'color': '#4F4F4F', 'fontSize': '18px'}),
                dcc.Input(id='cantidad', type='number', value=3, style={'width': '100%', 'padding': '12px', 'borderRadius': '10px', 'border': '1px solid #B8B8B8', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 'fontSize': '16px'})
            ], style={'padding': '10px', 'backgroundColor': '#fff', 'borderRadius': '15px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px'}),

            html.Div([
                html.Label("Código DANE:", style={'fontWeight': '600', 'color': '#4F4F4F', 'fontSize': '18px'}),
                dcc.Input(id='codigo_dane', type='number', value=15001, style={'width': '100%', 'padding': '12px', 'borderRadius': '10px', 'border': '1px solid #B8B8B8', 'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)', 'fontSize': '16px'})
            ], style={'padding': '10px', 'backgroundColor': '#fff', 'borderRadius': '15px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '40px'}),

            # Botón para predecir con un diseño moderno
            html.Button('Predecir', id='submit-button', n_clicks=0, style={
                'padding': '12px 24px', 'backgroundColor': '#4CAF50', 'border': 'none', 'color': 'white',
                'borderRadius': '10px',  'cursor': 'pointer', 'fontSize': '18px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 
                'transition': 'background-color 0.3s ease-in-out', 'width': '100%'  
            }),
        ], style={'maxWidth': '700px', 'margin': '0 auto', 'padding': '20px'}),

        # Caja para mostrar la predicción
        html.Div(id='prediction-output', style={
            'padding': '20px', 'backgroundColor': '#fff', 'borderRadius': '15px', 'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
            'textAlign': 'center', 'marginTop': '20px', 'color': '#333', 'fontSize': '20px', 'fontWeight': '600',
            'maxWidth': '700px', 'margin': '20px auto'
        })
    ]
)

# Función para llamar a la API de Flask y obtener la predicción
def get_prediction(data):
    url = 'https://crimenescolombia.onrender.com/predict'  # Asegúrate de que la URL sea correcta
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    # Imprimir la respuesta de la API para depuración
    print("Respuesta de la API:", response.json())
    
    return response.json()

# Callback para actualizar la predicción
@app.callback(
    Output('prediction-output', 'children'),
    [Input('submit-button', 'n_clicks')],  # Solo depende del clic del botón
    [Input('gender', 'value'),
     Input('departamento', 'value'),
     Input('municipio', 'value'),
     Input('edad', 'value'),
     Input('arma', 'value'),
     Input('dia_semana', 'value'),
     Input('cantidad', 'value'),
     Input('codigo_dane', 'value')]
)
def predict_crime(n_clicks, gender, departamento, municipio, edad, arma, dia_semana, cantidad, codigo_dane):
    if n_clicks > 0:
        # Datos a enviar a la API con las claves correctas
        data = {
            'features': {
                'GENERO': gender,
                'DEPARTAMENTO': departamento,
                'MUNICIPIO': municipio,
                'EDAD': edad,
                'ARMA': arma,
                'DIA_SEMANA': dia_semana,
                'CANTIDAD': cantidad,
                'CODIGO_DANE': codigo_dane
            }
        }
        prediction = get_prediction(data)
        
        # Verificar si la predicción contiene un error o la predicción real
        if 'error' in prediction:
            return f"Error: {prediction['error']}"
        elif 'prediction' in prediction:
            return f"Predicción del crimen: {prediction['prediction']}"
        else:
            return "Error al obtener la predicción. Intenta nuevamente."
    return ""

# Iniciar la app de Dash
if __name__ == '__main__':
    app.run_server(debug=True)
