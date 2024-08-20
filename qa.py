from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

def answer_question(context: str, question: str) -> str:
    # Tokenize the input
    inputs = tokenizer(question, context, return_tensors='pt')
    
    # Get the model outputs
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Extract the answer
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][answer_start:answer_end]))
    
    return answer


# Example usage 
context = "deepset/roberta-base-squad model is used in this code example"
question = "which model is used in this code example?"
output = answer_question(context, question)

print(output)