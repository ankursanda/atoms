import joblib

# Load the model from the file
final_model = "final_model.sav"
model = joblib.load(final_model)

def predict_category(s, model=model):
    pred = model.predict([s])
    target_names = model.named_steps['multinomialnb'].classes_
    return target_names[pred[0]]

li = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']

category = predict_category("There is a launch today")
print("Predicted category:", li[category])