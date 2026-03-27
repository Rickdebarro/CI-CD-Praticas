# Introdução ao CI/CD

Repositório base para o desenvolvimento de um pipeline que execute testes unitários, testes de segurança (SAST) e simulação de um deploy com aprovação manual, no Gitlab.

O CI/CD (Continuous Integration/Continuous Deployment) é uma prática essencial no DevOps, visando acelerar o ciclo de desenvolvimento e entrega de software. A integração contínua (CI) permite a validação constante de alterações no código por meio de testes automatizados, enquanto a entrega contínua (CD) automatiza o deploy em diferentes ambientes, garantindo maior confiabilidade e agilidade no lançamento de novas funcionalidades. 
Estas práticas promovem a colaboração entre equipes, a redução de erros em produção e o aumento da eficiência no desenvolvimento de software.

# O Arquivo .gitlab-ci.yml

- Arquivo YAML (YAML Ain't Markup Language) que especifica as instruções para a execução da pipeline através do Gitlab Runner;
- O arquivo deve ser salvo na raiz do projeto sempre com o nome .gitlab-ci.yml;
- Possui uma série de palavras-chave para diversas situações de uso, como acionamento em branches especificas;
- A sintaxe completa do arquivo pode ser consultada na [documentação de referência](https://docs.gitlab.com/ee/ci/yaml/index.html) e seu preenchimento pode ser validado no [Editor de  Pipelines do Gitlab](https://docs.gitlab.com/ee/ci/pipeline_editor/index.html) ou através de uma extensão do [VSCode](https://marketplace.visualstudio.com/items?itemName=gitlab.gitlab-workflow).

Exemplo de arquivo .gitlab-ci.yml que executa um stage chamado “test-job” exibindo o valor informado a partir do comando “echo” dentro da interface gráfica do Gitlab (menu "Build" > "Pipelines"):

```
test-job:
    stage: test
    script:
        - echo "This job tests something"
```

## Exercícios Propostos

1. **Continuos Integration:**  
Alterar o arquivo .gitlab-ci.yml, contemplando: 
    - 1.1 Execução dos testes unitários, atingindo cobertura de 100%;
    - 1.2 Execução dos testes estáticos de segurança (SAST - Static Application Security Testing).

2. **Continuos Deployement:**  
Alterar o arquivo .gitlab-ci.yml, contemplando:
    - 2.1 Simular a implantação com aprovação manual em um stage de "deploy".

## Executando a aplicação

```
$ python app/app.py run
```

A aplicação responderá em duas rotas na web:

http://localhost:5000/health-check

http://localhost:5000/hello?name=guijac