from transformers import AutoModelForTokenClassification, AutoTokenizer

def load_ner_model(model_name="bert-base-cased", num_labels=9):
    model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=num_labels)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer
