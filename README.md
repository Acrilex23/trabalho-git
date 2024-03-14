
# trabalho-git
Diogo Cunha

1- Fiz fork no repositório do trabalho 

2- Fiz git clone do repositório
	Comando: git clone https://github.com/HungerBalls/trabalho-git

3- Fiz uma nova Branch
	Comando: git checkout -b cu

4- Fiz alterações nos ficheiros 
	Comando: nano simple.py

5- Adicionei as alterações 
	Comando: git add . 

6- Fiz commit 
	Comando: git commit -m "Added New Coding Lines in simple.py"

7- Fiz o git merge para evitar conflitos e unir as alterações	
	Comando: git checkout main, git merge cu
		 git checkout cu, git merge main

8- Fiz o rebase 
	Comando: git rebase cu
		 git checkout main
		 git rebase main

9- Fiz o cherry pick 
	Comando: git log
		 git cherry-pick 67ee5214f1e250b6fd7d42998efc587afa0b4fdd		 

10- Fiz o TAG 
	Comando: git tag -a v1.0 -m "Version 1.0"
		 git push  --tags  
			
=======
# Objetivos:

1. **Experiência prática com operações essenciais do Git/GitHub:**
  - Clone
  - Branch
  - Commit
  - Merge
  - Rebase
  - Cherry-pick
  - Tags
  - Pulls
  - Pull requests
  - Resolução de conflitos

2. **Colaboração em grupo:**
  - Colaborar em um projeto real que requer aplicação das técnicas mencionadas.

3. **Configurações iniciais:**
  - Cada participante deve ter uma conta no GitHub.
  - Git deve estar instalado localmente.

4. **Criação ou seleção de um repositório:**
  - Opção A: Criar um novo repositório no GitHub.
  - Opção B: Escolher um repositório público existente que aceite contribuições via pull requests.

5. **Clone local:**
  - Cada membro deve clonar o repositório escolhido para sua máquina local.
  - Atualizar o clone local com `git pull` sempre que houver modificações no servidor remoto.

6. **Distribuição de tarefas:**
  - Dividir tarefas entre os membros do grupo.
  - Garantir que todos tenham contribuições claras, como adicionar funcionalidades, corrigir bugs ou melhorar a documentação.

7. **Utilização de Branches e Commits:**
  - Criar branches para trabalhar nas tarefas designadas.
  - Fazer commits com mensagens claras e descritivas.

8. **Merges, Rebase, e Cherry-Picks:**
  - Decidir como integrar as contribuições ao branch principal.
  - Utilizar merges diretos, rebase para uma história linear ou cherry-picks para commits específicos.

9. **Tags:**
  - Utilizar tags para marcar releases significativas do projeto.

10. **Pull Requests:**
  - Enviar contribuições ao repositório original via pull requests.
  - Incluir descrições claras do que cada contribuição adiciona ou modifica.

11. **Resolução de Conflitos:**
  - Trabalhar em conjunto para resolver conflitos manualmente ou com ferramentas do Git.

12. **Documentação no README.md:**
  - Documentar o projeto final em um arquivo README.md no repositório.
  - Todos os membros do grupo devem contribuir para o arquivo com commits.
  - Incluir descrição do projeto, objetivos, detalhes de cada passo realizado, e reflexões sobre o processo de colaboração e aprendizagem.

13. **Entrega e Avaliação:**
  - Além do código e contribuições no repositório, a avaliação será baseada na documentação no README.md.
  - Demonstrar compreensão e aplicação das práticas do Git e GitHub.
  - Avaliar a qualidade das contribuições e a eficácia na resolução de conflitos.

# Martim Aroeira

# Contéudos
- [Repository](#repository)
- [Python File](#Python-File)
- [Branch](#branch)
- [Merge](#merge)
- [Rebase](#rebase)
- [Cherry-Pick](#cherrypick)
- [TAG](#tag)

## Repository:

-    No GitHub, ir para "Your repositories."

-    Clique em "New" e preencha o "Repository name"

-    Abra o terminal e clone o repositório:

```bash
git clone https://github.com/Acrilex23/trabalho-git.git
echo "# trabalho-git" >> README.md
git add README.md
git commit -m "First commit"
git push
```
### Explicação: 
```bash
git clone https://github.com/Acrilex23/trabalho-git.git
```
  - Neste comando, um clone do repositório trabalho-git hospedado no GitHub é criado. 
  - O URL fornecido é o endereço do repositório remoto.

```bash
echo "# trabalho-git" >> README.md
```

  - Este comando adiciona um título ao arquivo README.md recém-criado. 
  - O echo é utilizado para imprimir o texto ("# trabalho-git") e >> é usado para redirecionar esse texto ao final do arquivo README.md.
  
```bash
git add README.md
```

  - Adiciona as modificações realizadas no README.md ao staging area, preparando-as para serem incluídas no próximo commit.
  - Staging area é uma área intermediária onde seleciona as alterações específicas que deseja incluir no próximo commit.
  
```bash
git commit -m "First commit"
```

  - Realiza o commit das alterações feitas no README.md. 
  - O argumento -m é utilizado para adicionar uma mensagem de commit diretamente na linha de comando, e "First commit" é a mensagem associada a este commit.
  
```bash
git push
```
  - Envia as alterações realizadas para o repositório remoto no GitHub. 
  - Isso atualiza o branch padrão (normalmente o main ou master) com as alterações feitas localmente.

## Python File:
```bash
touch simple.py
git add simple.py
git commit -m "Adicionado simple.py"
git push
```
### Explicação: 

```bash
touch simple.py
```
  - Este comando cria um novo arquivo chamado simple.py. 

```bash
git add simple.py
```

  - Adiciona o arquivo simple.py ao staging area. 
  
```bash
git commit -m "Adicionado simple.py"
```

  - Realiza um commit com uma mensagem descritiva indicando o propósito das alterações. 
  - Neste caso, o commit registra a adição do arquivo simple.py ao projeto.
  
```bash
git push
```

  - Envia as alterações (o novo commit) para o repositório remoto no GitHub. 

## Branch:

```bash
git checkout -b aro
```
### Explicação: 
```bash
git checkout
```

  - Este comando é usado para alternar entre branches no repositório. 
  - Quando utilizado com a opção -b, também é capaz de criar uma nova branch.

## Merge:
```bash
git checkout main
git merge aro
git add simple.py
git commit -m "Resolved problems"
git merge aro
```

### Explicação: 
```bash
git checkout main
```
  - Muda para o branch principal, neste caso, chamado "main.".

```bash
git merge aro
```
  - Realiza um merge das alterações do branch "aro" para o branch atual (main).
   
:warning: **Warning**
  - Durante esse processo, o Git tentará automaticamente combinar as alterações, mas podem ocorrer conflitos.
  
```bash
git add simple.py
```
  - Adiciona o arquivo "simple.py" ao staged area, preparando-o para o próximo commit.

```bash
git commit -m "Resolved problems"
```
  - Realiza um commit para registrar as alterações e resolver os problemas (conflitos) que podem ter ocorrido durante o merge.
  
```bash
git merge aro
```

  - Novamente, realiza um merge do branch "aro" no branch atual (main).
   
:memo: **Note**
  - Isso pode ser necessário se houver conflitos resolvidos durante o commit anterior ou se novas alterações foram feitas no branch "aro" após o primeiro merge.

## Rebase:
```bash
git checkout aro
git add simple.py
git commit -m "Added more 3 lines to the file simple.py"
git checkout main
git rebase aro
```

### Explicação:     

```bash
git checkout aro
```
 
  - Este comando muda o branch atual para "aro". Todos os comandos subsequentes serão aplicados a este branch.

```bash
git add simple.py
```
    
  - Adiciona as alterações feitas no arquivo "simple.py" ao índice, para o próximo commit.

```bash
git commit -m "Added more 3 lines to the file simple.py"
```
 
  - Cria um novo commit no branch "aro" com uma mensagem de commit.

```bash
git checkout main
```
    
  - Retorna ao branch principal, "main".

```bash
git rebase aro   
```
    
  - Realiza o rebase do branch "aro" no branch atual, que é "main". 
  - Durante o rebase, o Git aplica os commits do branch "aro" sobre o branch "main", recriando cada commit  individualmente. 
  - Isso resulta em uma história linear e pode ajudar a manter uma linha do tempo mais limpa.

## Cherry-Pick:
```bash
git checkout aro
git add simple.py
git commit -m "Added one more line to the file simple.py"
git log
git checkout main
git cherry-pick e8a49317567ad4332406dc8af39f53341b1adf58
git cherry-pick --continue
```

### Explicação: 

```bash
git checkout aro
```
 
  - Altera para o branch chamado "aro".
  - Prepara-se para adicionar uma nova linha ao arquivo no contexto desse branch.

```bash
git add simple.py
```
  - Adiciona as alterações feitas no arquivo "simple.py" ao staging area, preparando-as para o próximo commit.

```bash
git commit -m "Added one more line to the file simple.py"
```

  - Realiza um commit com uma mensagem descritiva informando que uma nova linha foi adicionada ao arquivo "simple.py".

```bash
git log
```
    
  - Exibe o histórico de commits no branch atual ("aro"). O objetivo é obter a identificação única (hash) do commit mais recente.

```bash
git checkout main
```
    
  - Altera para o branch principal chamado "main" para realizar o cherry-pick nesse branch.

```bash
git cherry-pick e8a49317567ad4332406dc8af39f53341b1adf58
```

  - Aplica o commit identificado pela hash "e8a4931..." do branch "aro" ao branch atual ("main").
  - Pode ocorrer um conflito durante esse processo, e é necessário resolvê-lo manualmente antes de continuar.
  
:warning: **Warning** 
  - Durante o cherry-pick, o Git pode criar marcações (<<<<<<<, =======, >>>>>>>) indicando áreas conflitantes no código. 

:bulb: **Tip** 
```bash
git cherry-pick --continue
```
    
  - Continua o processo de cherry-pick após a resolução manual de conflitos. Isso confirma que as alterações foram tratadas e estão prontas para serem commitadas.

## TAG:
```bash
git tag -a v1.0 -m "Versão 1.0"
git push --tags
```

### Explicação: 

```bash
git tag -a v1.0 -m "Versão 1.0"
```
    
  - Neste comando, estamos criando uma tag (etiqueta) no repositório Git. 
  - A opção -a indica que queremos criar uma tag anotada, que é uma versão mais detalhada da tag contendo informações adicionais, como o nome do autor e a data de criação. 
  - v1.0 é o nome da tag, representando a versão 1.0 do projeto. 
  - O argumento -m é utilizado para adicionar uma mensagem descritiva que geralmente contém informações sobre a versão.

```bash
git push --tags
```
    
  - Este comando é usado para enviar (push) as tags para o repositório remoto no GitHub. 
  - As tags, assim como os branches, não são enviadas automaticamente com git push. 
  - Portanto, é necessário especificar --tags para garantir que as tags também sejam enviadas para o repositório remoto.

:memo: **Note**
  - Resumindo, esses dois comandos são usados para criar uma tag anotada chamada v1.0 e enviá-la para o repositório remoto, marcando uma versão específica do projeto. 
  - Essas tags são frequentemente usadas para marcar releases significativas ou pontos de referência no histórico do projeto.


