# Gothic Novels Dataset Creation and GPT-2 Fine-Tuning

This project involves creating a dataset of Gothic novels from Project Gutenberg and fine-tuning a GPT-2 model using the dataset. The fine-tuned model is then used to generate text based on a given prompt.

## Dataset Creation

The script downloads texts from Project Gutenberg and processes them to create a dataset. The texts are cleaned and combined into a single file for training.

## Requirements

- Python 3.x
- `requests`
- `torch`
- `transformers`
- `datasets`
- `matplotlib`
- `kaggle`

## Setup

1. **Kaggle API Configuration**:
   - Ensure you have a Kaggle account and create an API token from your Kaggle account settings.
   - Place the `kaggle.json` file in the `~/.kaggle` directory on your system.

2. **Install Required Libraries**:
   ```bash
   pip install requests torch transformers datasets matplotlib kaggle
   ```

## Steps

1. **Download Gothic Novels from Project Gutenberg**:
   - The script `download_gothic_novels.py` downloads texts of Gothic novels from Project Gutenberg and saves them in a structured directory.

2. **Combine and Clean Texts**:
   - The texts are cleaned to remove Project Gutenberg headers and footers.
   - The cleaned texts are combined into a single file `gothic_novels_combined.txt`.

3. **Fine-Tune GPT-2 Model**:
   - The GPT-2 model is fine-tuned on the combined Gothic novels dataset using the `transformers` library.
   - The fine-tuning process utilizes the LoRA (Low-Rank Adaptation) technique to adapt the model parameters efficiently.

4. **Generate Text with Fine-Tuned Model**:
   - The fine-tuned model can be used to generate text based on a given prompt.

## Additional Information

- **Gothic Novels**: This project focuses on Gothic novels, a genre characterized by elements of horror, mystery, and romanticism.
- **Project Gutenberg**: A digital library offering free access to a vast collection of public domain books.
- **LoRA**: Low-Rank Adaptation, a technique to efficiently adapt the parameters of a pre-trained model.
- **GPT-2**: A transformer-based model for natural language processing tasks developed by OpenAI.

