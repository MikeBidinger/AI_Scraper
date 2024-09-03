# AI Scraper

A Python application that is able to scrape a website and query the contents 
with the use of a LLM.

This Python application uses multiple different assets to be able to scrape a
website and query the content of this page by using natural language.

Used assets:

-   [Anaconda](https://www.anaconda.com/ "Anaconda"): Environment & package manager
-   [Streamlit](https://streamlit.io/ "Streamlit"): Frontend
-   [Selenium](https://pypi.org/project/selenium/ "Selenium"): Web scraper
-   [BeautifulSoup](https://pypi.org/project/beautifulsoup4/ "BeautifulSoup"): HTML parser
-   [LangChain](https://pypi.org/project/langchain/ "LangChain"): Chain interface
-   [Ollama](https://ollama.com/ "Ollama"): LLM (Large Language Model)

## Create the virtual environment

To create a virtual environment we're able to run a single command with the
package manager
[Anaconda](https://github.com/MikeBidinger/Python_Anaconda "More info about Anaconda").

By using the following command to create the Conda environment from the
[environment.yml](environment.yml) file:

```console
conda env create -f environment.yml
```

## Activate the virtual environment

After the Conda environment is created the following command can be used to
activate the environment:

```console
conda activate AI_Scraper
```

## Install Ollama

Ollama is a LLM that can be run locally and completely for free.
First Ollama has to be downloaded and installed to be able to use the LLM.
Go to the [Ollama download page](https://ollama.com/download) and select the 
appropriate OS and download it.
After downloading, install the Ollama application.
When successfully installed, the following command can be used:

```console
ollama
```

If the application is installed properly, it should get an correct response.

<details>
    <summary>View example result</summary>

    Usage:
      ollama [flags]
      ollama [command]
    
    Available Commands:
      serve       Start ollama
      create      Create a model from a Modelfile
      show        Show information for a model
      run         Run a model
      pull        Pull a model from a registry
      push        Push a model to a registry
      list        List models
      ps          List running models
      cp          Copy a model
      rm          Remove a model
      help        Help about any command
    
    Flags:
      -h, --help      help for ollama
      -v, --version   Show version information
    
    Use "ollama [command] --help" for more information about a command.

</details>

Now a Ollama model can be pulled with te following command (for this specific 
example application, we use the model `llama3`):

```console
ollama pull llama3
```

> [!NOTE]
> Check the [Ollama GitHub](https://github.com/ollama/ollama "Ollama GitHub") 
> documentation for more information about the different models and there 
> requirements.

We're also able to run the model directly within our command window to interact 
with the LLM by using the following command:

```console
ollama run llama3
```

## Run the application

To run the application, the following command can be used:

```console
streamlit run main.py
```
