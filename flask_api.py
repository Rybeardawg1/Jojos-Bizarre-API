from flask import Flask, jsonify, send_from_directory
from flask_restful import Resource, Api
import random
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)
api = Api(app)

model = TFGPT2LMHeadModel.from_pretrained("./jojo-gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("./jojo-gpt2")
print("model and tokenizer loaded")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        app.root_path, "JojosbizarreAPI.png", mimetype="image/vnd.microsoft.icon"
    )

class CreateResponse(Resource):
    def get(self, input):
        input_ids = tokenizer.encode(input, return_tensors="pt")

        print("generating output")
        output = model.generate(
            input_ids, 
            max_length=30,
            num_beams=1,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.99,
            num_return_sequences=1,
            do_sample=True,
            temperature=1,
        )

        print("output generated")
        output = tokenizer.decode(output[0], skip_special_tokens=True)

        period = output.rfind(".")
        question_mark = output.rfind("?")
        exclamation_mark = output.rfind("!")
        if period > question_mark and period > exclamation_mark:
            output = output[: output.rfind(".") + 1]
        elif question_mark > period and question_mark > exclamation_mark:
            output = output[: output.rfind("?") + 1]
        elif exclamation_mark > period and exclamation_mark > question_mark:
            output = output[: output.rfind("!") + 1]
        output = output.replace("\n", " ")

        return jsonify({"Jojo-GPT2": output})


class GetCatchPhrase(Resource):
    catchphrases_file = "catchphrases.txt"

    def get_catchphrases(self):
        with open(self.catchphrases_file, "r") as f:
            return [line.strip() for line in f]

    def get(self):
        catchphrases = self.get_catchphrases()

        hint = {
            "Directions": "Add an input to the URL",
            "Example": "jojosbizarreapi.com/What's 5+5? Response: I don't know but I bet my stand is stronger than that.",
            "Repo": "https://github.com/Rybeardawg1/Jojos-Bizarre-API/",
        }

        if catchphrases:
            random_catchphrase = random.choice(catchphrases)
            return jsonify({"Catchphrase": random_catchphrase, "Hint": hint})
        else:
            return (
                jsonify({"message": "Catchphrases not found", "Hint": hint}),
                404,
            )


api.add_resource(GetCatchPhrase, "/")
api.add_resource(CreateResponse, "/<string:input>")

if __name__ == "__main__":
    app.run(debug=True)
