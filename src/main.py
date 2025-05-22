from ner.train import train_model
from ner.evaluate import evaluate_model
from config import load_config

def main():
    config = load_config()
    print("Training started...")
    train_model(config)
    print("Evaluation started...")
    evaluate_model(config)

if __name__ == "__main__":
    main()
