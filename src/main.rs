use axum::{ routing::get, response::Json, Router };
use rand::seq::SliceRandom;
use tokio::fs;

#[tokio::main]
async fn main() {
    let app = Router::new().route("/", get(get_catchphrase));
    // Start the server
    axum::Server
        ::bind(&"0.0.0.0:3000".parse().unwrap())
        .serve(app.into_make_service()).await
        .unwrap();
}

// Get random catchphrase
async fn get_catchphrase() -> Json<String> {
    let catchphrases = read_catchphrases().await;

    let hint =
        r#"
        Directions: "Add an input to the URL,
        Example: jojosbizarreapi.com/What's 5+5? Response: I don't know but I bet my stand is stronger than that.,
        Repo: https://github.com/Rybeardawg1/Jojos-Bizarre-API/
        "#;

    if let Some(random_catchphrase) = catchphrases.choose(&mut rand::thread_rng()) {
        let json_value = format!("Catchphrase: {random_catchphrase},\nHint: {hint}");
        print!("{}", json_value.to_string());
        Json(json_value)
    } else {
        let json_value = format!("Message: Catchphrases not found,\nHint: {hint}");
        Json(json_value)
    }
}

// Generate response based on input
// async fn create_response(path: axum::extract::Path<String>) -> Json<Value> {
//     let model = tch::CModule::load("jojo-gpt2/").expect("Failed to load model");
//     let tokenizer = tch::CModule::load("jojo-gpt2/").expect("Failed to load tokenizer");

//     let input = path.as_str().to_string();
//     let input_ids = tokenizer.encode(&input, false).to_device(tch::Device::cuda_if_available());

//     println!("Generating output");
//     let output = model.forward_ts(&[input_ids], false).unwrap().to_device(tch::Device::Cpu);
//     let output = output.argmax(-1, false);

//     println!("Output generated");
//     let output = tokenizer.decode(&output, false);
//     let output = cleanup_output(output);

//     Json(json!({
//         "Jojo-GPT2": output
//     }))
// }

// Read catchphrases from file
async fn read_catchphrases() -> Vec<String> {
    fs::read_to_string("catchphrases.txt").await
        .map(|content| content.lines().map(String::from).collect())
        .unwrap_or_else(|_| Vec::new())
}

// Clean up generated output
// fn cleanup_output(output: String) -> String {
//     let period = output.rfind('.');
//     let question_mark = output.rfind('?');
//     let exclamation_mark = output.rfind('!');

//     if let Some(period) = period {
//         if period > question_mark.unwrap_or(0) && period > exclamation_mark.unwrap_or(0) {
//             return output[..=period].to_string();
//         }
//     }

//     if let Some(question_mark) = question_mark {
//         if question_mark > period.unwrap_or(0) && question_mark > exclamation_mark.unwrap_or(0) {
//             return output[..=question_mark].to_string();
//         }
//     }

//     if let Some(exclamation_mark) = exclamation_mark {
//         if exclamation_mark > period.unwrap_or(0) && exclamation_mark > question_mark.unwrap_or(0) {
//             return output[..=exclamation_mark].to_string();
//         }
//     }

//     output.replace('\n', " ")
// }
