# Manai 
#### Man ai is meant to be a man page the integrates OpenAI's ChatGPT. It will read the man pages and give the users a more comprehensive description of the man page. 

## Installation Guide

**Currently the app is terminal based for Unix systems**

Clone the repo 

```
gitclone https://github.com/Chopstix1210/Manai.git
```

Change the directory to clone 

```
cd ~/Manai
```

Run install.sh with sudo (sudo is needed to create the alias manai)

```
sudo ./install.sh
```

## How to use ManAI

A simple use of manai is `manai [command]`. Where [command] is any thing you'd like to have a manpage for. 

```
manai ls 
```

You can also use the `-m` to send a specific message. 

```
manai ls -m "How to send displayed contents to a file?"
```

## To-Do Tasks (backlog)

- [ ] Find faster way to use Pinecone DB
- [ ] Create an MYSQL db to store user data to have history chats
- [x] Create animation for loading 
- [ ] Create prompts that generate better results for man page 
- [ ] Find a way to decrease hallucinations 
- [ ] Add support for pip libraries
- [x] Add ChatGPT to read man page, assume prompt and generate message 
- [x] Locate and chunk man pages index to Pinecone DB
- [x] Integrate Pinecone DB to index man pages
- [x] Create help page with working args 
- [x] Integrate OpenAI to work with Terminal message 

## Check out the commits and Version Releases

View [commit change](https://github.com/Chopstix1210/Manai/commits/main)

### Version History

- 0.1.0
    - Initial work with `manai [command] [arg [message]]`
- 0.0.2 
    - Learning how LLM and LangChain work (Jupyter Notebooks)
- 0.0.1
    - Initial release

