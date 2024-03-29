# Jojos-Bizarre-API

<p align="center">
    <a href="https://jojosbizarreapi.com/">
        <Image src="JojosbizarreAPI.png" > </Image>
    </a>
</p>

Gonna make an NLP model that'll respond to API calls. Maybe make it into a Twitter bot too or something.. idk

## To Do:

### Get all Jojo script data<br>

- [x] get scripts<br>
- [x] get better formatted scripts for NLP<br>

<blockquote>
Show: https://transcripts.foreverdreaming.org/viewforum.phpf=1721 <br>
Important quotes: https://en.wikiquote.org/wiki/JoJo%27s_Bizarre_Adventure <br>
Manga: picture-to-text scanner maybe? <br>
Manga: https://mangadex.org/title/136/jojo-s-bizarre-adventure-part-1-phantom-blood <br>
</blockquote>

### The API itself

- [x] Make REST API that will call model when prompted and return quote when unprompted <br>
- [x] Flask is lame, learn Rust and use Axum? <br>
- [ ] Fix output not rendering newlines <br>
- [ ] Figure out how to use Jojo-GPT2 in Rust <br>

### Learn about NLPs

- [x] Understand NLP basics<br>
- [x] Train jojo-gpt2<br>
- [x] Train a better one<br>
- [ ] Test different models Llama 2, GPT-NeoX, GPT-J, Vicuna-13B, XGen-7B<br>

- [x] Understand tokenization, stemming, and lemmatization <br>
- [x] Apply/practice concepts<br>

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

- [x] Build and containerize the API <br>
- [x] Create CI/CD pipeline with GitHub Actions <br>
- [x] Deploy API and use domain <br>
- [x] HTTPS <br>
- [ ] Manually upload model through SSH or store on Google Drive lol
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

If you want to use libtorch, download here:https://pytorch.org/ and you may need to set these env variables: <br>
set LIBTORCH_USE_PYTORCH=0 <br>
set LIBTORCH_BYPASS_VERSION_CHECK=0<br>
cargo build <br>
cargo run <br>
