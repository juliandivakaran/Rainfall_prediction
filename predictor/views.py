import joblib
import numpy as np
import os

# Define the path to the model (update as necessary)
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'rainfall_model.pkl')

# Load the trained model
try:
    model = joblib.load(model_path)
except ValueError as e:
    # Handle specific errors related to model loading
    raise ValueError(f"Error loading the model: {e}")

def predict_rainfall(request):
    if request.method == 'POST':
        try:
            # Retrieve data from POST request
            year = int(request.POST.get('year'))
            jan = float(request.POST.get('jan'))
            feb = float(request.POST.get('feb'))
            mar = float(request.POST.get('mar'))
            apr = float(request.POST.get('apr'))
            may = float(request.POST.get('may'))
            jun = float(request.POST.get('jun'))
            jul = float(request.POST.get('jul'))
            aug = float(request.POST.get('aug'))
            sep = float(request.POST.get('sep'))
            oct = float(request.POST.get('oct'))
            nov = float(request.POST.get('nov'))
            dec = float(request.POST.get('dec'))

            # Predict rainfall
            prediction = model.predict(np.array([[year, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]]))[0]

            # Prepare context to pass to template
            context = {
                'year': year,
                'prediction': prediction
            }

            # Render the result template with the context
            return render(request, 'predictor/result.html', context)
        
        except Exception as e:
            # If an error occurs during prediction or data processing, render the form template with an error message
            return render(request, 'predictor/form.html', {'error_message': str(e)})
    
    # If it's a GET request (initial page load), render the form template
    return render(request, 'predictor/form.html')

