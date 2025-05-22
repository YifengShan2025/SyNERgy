import pytest
from ner.model import load_ner_model

def test_load_ner_model():
    model, tokenizer = load_ner_model()
    assert model is not None
    assert tokenizer is not None
    assert hasattr(model, 'forward')
