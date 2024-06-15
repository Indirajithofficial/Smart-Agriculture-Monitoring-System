from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

ENDPOINT = "https://<Your-Custom-Vision-Endpoint>.cognitiveservices.azure.com/"
prediction_key = "YourPredictionKey"
project_id = "YourProjectId"
model_name = "YourModelName"

credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, credentials)

def analyze_image(image_path):
    with open(image_path, "rb") as image_data:
        results = predictor.classify_image(project_id, model_name, image_data.read())
    for prediction in results.predictions:
        print(f"{prediction.tag_name}: {prediction.probability * 100:.2f}%")

analyze_image("path/to/your/image.jpg")
