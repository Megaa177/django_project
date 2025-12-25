from django.shortcuts import render
from .models import Patient

def patients_table(request):
    # Filter patients with no mental health condition
    patients = Patient.objects.filter(mental_health_condition__isnull=True)

    # Convert queryset to list of dicts
    data = list(patients.values())

    # Get column names
    columns = data[0].keys() if data else []

    return render(request, "mental_app/patients_tables.html", {
        "columns": columns,
        "data": data,
    })

# mental_app/views.py
from django.shortcuts import render
from .forms import PredictionForm
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from .models import Patient

# Load model once
rf = joblib.load('mental_app/rf_model.pkl')
model_columns = joblib.load('mental_app/model_columns.pkl')


def predict_view(request):
    prediction = None
    charts = {}

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Convert form to dataframe with same columns as model
            df_input = pd.DataFrame([form.cleaned_data])
            df_input = pd.get_dummies(df_input)
            # Add missing columns with 0
            for col in model_columns:
                if col not in df_input.columns:
                    df_input[col] = 0
            df_input = df_input[model_columns]  # reorder

            # Predict
            prediction = rf.predict(df_input)[0]

    else:
        form = PredictionForm()

    # Generate charts
    df = pd.DataFrame(Patient.objects.all().values())
    if not df.empty:
        for col in df.columns:
            if col != 'mental_health_condition' and df[col].dtype != 'object':
                plt.figure(figsize=(4,3))
                sns.barplot(x=col, y='mental_health_condition', data=df)
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                charts[col] = base64.b64encode(buf.getvalue()).decode('utf-8')
                plt.close()

    return render(request, 'mental_app/predict.html', {'form': form, 'prediction': prediction, 'charts': charts})
