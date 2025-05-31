import gradio as gr
import pandas as pd
import numpy as np
import joblib

# Daten laden
model = joblib.load("model/car_price_model.pkl")
feature_names = joblib.load("model/car_model_features.pkl")

# Ursprüngliche Daten laden
df = pd.read_csv("data/car_data_merged.csv")
df = df[['year', 'odometer', 'Engine HP', 'manufacturer', 'model', 'transmission', 'type']].dropna()

# Modell-Mapping: Hersteller → Modelle
model_map = df.groupby('manufacturer')['model'].unique().to_dict()
manufacturers = sorted(model_map.keys())
transmissions = sorted(df['transmission'].unique())

# Modell-Dropdown aktualisieren bei Herstellerauswahl
def update_model_dropdown(manufacturer):
    models = sorted(model_map.get(manufacturer, []))
    return gr.update(choices=models, value=models[0] if models else None)

# Fahrzeugtyp automatisch bestimmen
def retrieve_car_type(manufacturer, model_name, year):
    filtered = df[
        (df['manufacturer'] == manufacturer) &
        (df['model'] == model_name) &
        (df['year'] == year)
    ]
    if not filtered.empty:
        return filtered.iloc[0]['type']
    else:
        return "other"

def predict_price(year, odometer, engine_hp, manufacturer, model_name, transmission):
    try:
        car_type = retrieve_car_type(manufacturer, model_name, year)

        input_dict = {
            'year': [year],
            'odometer': [odometer],
            'Engine HP': [engine_hp],
            'manufacturer': [manufacturer],
            'model': [model_name],
            'transmission': [transmission],
            'type': [car_type]
        }
        input_df = pd.DataFrame(input_dict)

        # Feature Engineering: Altersgruppe
        input_df['age'] = 2025 - input_df['year']

        labels = ['neu', 'mittel', 'alt', 'sehr alt']
        input_df["age_cat"] = pd.cut(input_df.age, bins=[0, 3, 7, 12, 100], labels=labels)
        input_df['age_cat_encoded'] = input_df['age_cat'].map({
            'neu': 0,
            'mittel': 1,
            'alt': 2,
            'sehr alt': 3
        })
        input_df = input_df.drop(columns=['age', 'age_cat'])

        # Dummy-Codierung
        input_encoded = pd.get_dummies(input_df)

        # Fehlende Spalten ergänzen
        for col in feature_names:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_final = input_encoded[feature_names]

        # Vorhersage
        prediction = model.predict(input_final)[0]
        return f"{int(prediction):,} USD"
    except Exception as e:
        return f"Fehler: {e}"
    
# Test prediction call before launching the app
test_prediction = predict_price(
    year=2015,
    odometer=80000,
    engine_hp=180,
    manufacturer=manufacturers[0],
    model_name=model_map[manufacturers[0]][0],
    transmission=transmissions[0]
)
print("Test prediction:", test_prediction)


# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## Auto-Preis-Vorhersage")

    with gr.Row():
        with gr.Column():
            manufacturer_input = gr.Dropdown(choices=manufacturers, label="Hersteller")
            model_input = gr.Dropdown(choices=[], label="Modell")
            year_input = gr.Number(label="Baujahr", value=2015)
            odometer_input = gr.Number(label="Kilometerstand", value=80000)
            engine_hp_input = gr.Number(label="Motorleistung (HP)", value=180)
            transmission_input = gr.Dropdown(choices=transmissions, label="Getriebeart")

        with gr.Column():
            predict_button = gr.Button("Preis vorhersagen")
            output = gr.Text(label="Vorhergesagter Preis")

    # Modell aktualisieren
    manufacturer_input.change(fn=update_model_dropdown, inputs=manufacturer_input, outputs=model_input)

    # Vorhersage auslösen
    predict_button.click(
        fn=lambda mfr, mdl, yr, odo, hp, tr: predict_price(yr, odo, hp, mfr, mdl, tr),
        inputs=[manufacturer_input, model_input, year_input, odometer_input, engine_hp_input, transmission_input],
        outputs=output
    )

demo.launch()
