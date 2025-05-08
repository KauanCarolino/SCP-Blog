# Tutorial para Desvendar os Segredos SCP com Django

## Introdução
Bem-vindo, agente da Fundação SCP, ao tutorial que o guiará pela criação de uma instância do Projeto SCP utilizando o poderoso framework Django. Prepare-se para mergulhar nos mistérios do código e explorar os segredos ocultos do universo SCP.

## Passo 1: Fork do Repositório
  1. Faça um fork do repositório SCP-RPG para sua própria conta no GitHub. 
     Isso criará uma cópia do repositório em seu perfil.
       
  2. No seu repositório fork, clique no botão "Code" e copie o URL do repositório.


## Passo 2: Clone do Repositório
  1. Abra o terminal na sua estação de trabalho.
  2. Navegue até o diretório onde você deseja clonar o repositório.
  3. Execute o seguinte comando para clonar o repositório para sua estação de trabalho:
     
      ```bash
      git clone <https://github.com/KauanCarolino/SCP-Blog.git>
      ```
      
## Passo 3: Configuração do Ambiente Virtual

  1. Navegue até o diretório do projeto:
      ```bash
      cd SCP-RPG
      ```
  2. Crie um ambiente virtual:
      ```bash
      python -m venv venv
      ```
  3. Ative o ambiente virtual:
      • No Windows:
        ```
        venv\Scripts\activate
        ```
      • No Linux/Mac:
        ```
        source venv/bin/activate
        ```
        
## Passo 4: Instalação das Dependências
  1. Com o ambiente virtual ativado, instale as dependências do projeto:
  ```bash
    pip install -r requirements.txt
  ```

## Passo 5: Migrações e Criação do Banco de Dados
  1. Execute o makemigration para criar as models do seu banco:
  ```
    python manage.py makemigration blog
  ```
  2. Execute as migrações para criar o banco de dados:
  ```
    python manage.py migrate
  ```
## Passo 6: Criação de Superusuário
  1. Crie um superusuário para acessar a interface de administração:
  ```
    python manage.py createsuperuser
  ```
## Passo 7: Executar o Servidor de Desenvolvimento
  1. Inicie o servidor de desenvolvimento:
  ```
    python manage.py runserver
  ```
## Passo 8: Configuração do Tailwind
  1. baixe o Node JS e o npm:
      • No Windows:
        ```
           Acesse o [site oficial do Node.js](https://nodejs.org) e baixe a versão LTS (Long Term Support).
        ```
      • No Linux/Mac:
        ```bash
          sudo apt update
          sudo apt install nodejs npm
        ```
  2. Verifique a instalação:
     ```bash
        node -v
        npm -v
     ```
        
Acesse http://127.0.0.1:8000/ em seu navegador para ver a aplicação em ação.

## Passo 8: Contribuindo com Descobertas
  1. Explore as diferentes branches para encontrar áreas de contribuição.
  2. Para contribuir, crie uma branch a partir da branch principal:
  ```
    git checkout -b minha-contribuicao
  ```
  3. Faça suas alterações, adicione, commite e push para o seu fork.
  4. Abra um Pull Request para a branch principal e compartilhe suas descobertas com outros agentes.

# Pronto, agente! Você está agora preparado para desvendar os segredos do universo SCP através do poder do Django. Boa sorte em suas missões e que a contenção esteja sempre sob controle! 🔒
