# Jojos-Bizarre-API

Gonna make an NLP model that'll respond to API calls. Maybe make it into a Twitter bot too or something.. idk

## To Do:

### Get all Jojo script data<br>

[x] get scripts<br>
[] get better formatted scripts for NLP<br>
[] get manga data<br>

<blockquote>
Show: https://transcripts.foreverdreaming.org/viewforum.phpf=1721 <br>
https://en.wikiquote.org/wiki/JoJo%27s_Bizarre_Adventure <br>
Manga: picture-to-text scanner maybe? <br>
Manga: https://mangadex.org/title/136/jojo-s-bizarre-adventure-part-1-phantom-blood <br>
</blockquote>

### The API itself

[x] Make REST API that will call model when prompted and return quote when unprompted <br>
[] Flask is fucking slow so Rust...? <br>

### Learn about NLPs

[x] Understand NLP basics<br>
[x] Train jojo-gpt2<br>
[] Train a better one<br>

<blockquote>
Understand tokenization, stemming, and lemmatization <br>
Apply/practice concepts<br>
</blockquote>

### Hosting

<blockquote>
Domain: https://instantdomains.com/search?q=jojosbizarreapi <b>ITS MINE</b><br>
<s>https://www.heroku.com/</s> <br>
https://www.pythonanywhere.com/ <br>
https://www.digitalocean.com/ <br>
<s>https://www.shuttle.rs/</s><br>
AWS Lambda? <br>

Digital Ocean Web App 👎BOO tomato tomato tomato <br>
Digital Ocean [Droplet](https://i.kym-cdn.com/entries/icons/original/000/030/423/cover5.jpg)<br>
now I just need to containerize my api and deploy it.... hopefully the ssh and droplet resources will be enough to serve the model 🙃 <br>
</blockquote>

### Running Development Server

Flask: <br>
python flask_api.py

Axum: <br>
If you want to use pytorch instead of libtorch, you may need to follow these instructions: <br>
pip install torch torchvision torchaudio <br>
python -m venv C:\Users\Rybeardawg1\AppData\Local\Programs\Python\Python39\Lib\venv <br>
set LIBTORCH_USE_PYTORCH=1 <br>
As of now, tch version 0.14.0 crate supports up to PyTorch 2.1.0. If you need to downgrade, use pip install torch==2.1.0<br>

If you want to use libtorch, download here:https://pytorch.org/ and you may need to follow these instructions: <br>
set LIBTORCH_USE_PYTORCH=0 <br>
set LIBTORCH_BYPASS_VERSION_CHECK=0<br>

cargo build <br>
cargo run <br>
