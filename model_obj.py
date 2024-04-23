from utils.openai_utils import *
class ModelObj:
    def __init__(self, model_name, model_local, access_key):
        self.model = model_name
        self.local = model_local
        self.access_key = access_key

    def create_model_obj(self) -> dict:
        return {"model": self.model, "local": self.local, "access_key": self.access_key}

def run_method(model_obj, input_str) -> dict:
    """
    Run embedding method based on the location specified in model_obj.
    """
    embedding = None  # Initialize to None to handle cases where condition does not meet
    if model_obj.local == "openai":
        embedding = embed_with_openai(input_str, model=model_obj.model, access_key=model_obj.access_key)
    
    return {"modelObj": model_obj.create_model_obj(), "embedding": embedding}

# Usage example
if __name__ == '__main__':
    model = ModelObj("text-embedding-3-small", "openai", os.getenv("OPENAI_API_KEY"))
    text_embedding = run_method(model, "This is a test text.")
    print(text_embedding)
