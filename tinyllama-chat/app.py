from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import logging
import warnings

# Filter out specific warnings
warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the TinyLlama model
logger.info("Loading model...")
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

try:
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    logger.info("Model loaded successfully!")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    raise

def generate_response(input_text):
    try:
        # Format the input following TinyLlama's chat template
        prompt = f"<|system|>You are a helpful AI assistant.</s><|user|>{input_text}</s><|assistant|>"
        
        # Tokenize the input
        inputs = tokenizer(prompt, return_tensors="pt", padding=True)
        
        # Move inputs to the same device as the model
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
        
        # Generate response
        with torch.no_grad():  # Add this line for efficiency
            outputs = model.generate(
                input_ids=inputs['input_ids'],  # Changed this line
                attention_mask=inputs['attention_mask'],  # Added this line
                max_length=200,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id,
                top_p=0.9,
                top_k=50
            )
        
        # Decode the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract only the assistant's response
        try:
            response = response.split("<|assistant|>")[-1].strip()
        except:
            response = response.strip()
            
        return response
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        return f"Error generating response: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    try:
        input_text = request.json["input"]
        response = generate_response(input_text)
        return jsonify({"response": response})
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

