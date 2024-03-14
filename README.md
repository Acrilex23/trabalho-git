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
			

