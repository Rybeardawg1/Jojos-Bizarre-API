from flask import Flask, jsonify
from flask_restful import Resource, Api
import random
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)
api = Api(app)


class CreateResponse(Resource):
    def get(self, input):
        model = TFGPT2LMHeadModel.from_pretrained("./gpt2-fine-tuned")
        tokenizer = GPT2Tokenizer.from_pretrained("./gpt2-fine-tuned")

        input_ids = tokenizer.encode(input, return_tensors="pt")

        output = model.generate(
            input_ids,
            max_length=100,
            num_beams=5,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.95,
        )

        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        return jsonify({"Response": generated_text})


class GetCatchPhrase(Resource):
    catchphrases_file = "catchphrases.txt"

    def get_catchphrases(self):
        with open(self.catchphrases_file, "r") as f:
            return [line.strip() for line in f]

    def get(self):
        catchphrases = self.get_catchphrases()

        if catchphrases:
            random_catchphrase = random.choice(catchphrases)
            return jsonify({"catchphrase": random_catchphrase})
        else:
            return jsonify({"message": "Catchphrases not found"}), 404


api.add_resource(GetCatchPhrase, "/")
api.add_resource(CreateResponse, "/<string:input>")

if __name__ == "__main__":
    app.run(debug=True)
