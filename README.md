# Work In Progress

Follow these steps to set up and use the project:

1. Add the following line to your `~/.zshrc` or `~/.bash_profile` file to export your OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    ```

2. Source your profile file to load the new environment variable:
    ```bash
    source ~/.bash_profile  # or source ~/.zshrc
    ```

3. Run the `setup.sh` script to create the environment:
    ```bash
    bash setup.sh
    ```

4. Use the following command to run the main script:
    ```bash
    python3 main.py
    ```