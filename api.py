from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el diccionario con el modelo, encoders y LDA
loaded_objects = joblib.load("modelo.pickle")

# Recuperar el modelo, encoders y LDA desde el diccionario
model = loaded_objects['model']
label_encoders = loaded_objects['label_encoders']
lda = loaded_objects['lda']

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos del JSON enviado
    data = request.get_json()

    # Crear un DataFrame con las características del nuevo registro
    nuevo_dato = pd.DataFrame(data['features'], index=[0])  # Asegurarse que 'features' es un diccionario de características

    # Aplicar LabelEncoder a las columnas categóricas
    for column, le in label_encoders.items():
        if column in nuevo_dato.columns:
            try:
                # Intentar transformar los valores directamente
                nuevo_dato[column] = le.transform(nuevo_dato[column])
            except ValueError:
                # Mapear los valores originales a sus índices numéricos si es necesario
                class_mapping = {original: index for index, original in enumerate(le.classes_)}
                nuevo_dato[column] = nuevo_dato[column].map(class_mapping)

    # Rellenar valores NaN
    nuevo_dato = nuevo_dato.fillna(0)

    # Asegurarse de que las columnas están en el mismo orden que durante el entrenamiento
    columnas_ordenadas = lda.feature_names_in_
    nuevo_dato = nuevo_dato[columnas_ordenadas]

    # Transformar los datos con LDA
    nuevo_dato_lda = lda.transform(nuevo_dato)

    # Realizar la predicción
    prediction = model.predict(nuevo_dato_lda)

    # Validar si 'TIPO_DELITO' está en label_encoders
    if 'TIPO_DELITO' in label_encoders:
        # Decodificar la predicción para mostrar la clase original
        prediccion_decodificada = label_encoders['TIPO_DELITO'].inverse_transform(prediction)
        return jsonify({'prediction': prediccion_decodificada[0]})
    else:
        # Si no está disponible, devolver la predicción numérica
        return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
