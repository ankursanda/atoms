from django.http import JsonResponse
import json
import joblib
import os
from .spiders import Runner as rnr
# Load the model from the file
current_dir = os.path.abspath(os.path.dirname(__file__))
# Load the model from the file
final_model = os.path.join(current_dir, "final_model.sav")
model = joblib.load(final_model)
def predict_category(s, model=model):
    pred = model.predict([s])
    target_names = model.named_steps['multinomialnb'].classes_
    return target_names[pred[0]]

li = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']
global in_list 
in_list= []
temp = []
def input_list(data):
    #in_list
    in_list.extend(data)
    # if temp != []:
    #     in_list = temp
    print("Attempt 1 prrinting:",in_list)
    return


def process_data(request):
    #global in_list
    if request.method == 'GET':
        rnr.Scrape()
        print("inside the final list",in_list)
        processed_data = li[predict_category("god")]
        return JsonResponse({'processed_data': processed_data})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
