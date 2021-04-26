# Controle remoto de robô por meio de Alexa, AWS e Raspberry Pi 3

- Instituto Federal de Santa Catarina - Câmpus Florianópolis
- Departamento Acadêmico de Eletrônica
- Curso de Engenharia Eletrônica
- Unidade curricular: Projeto Integrador III (PI3)
- Professores:
	- Daniel Lohmann
	- Robinson Pizzio
- Aluno: Vítor Faccio - vitorfaccio.ifsc@gmail.com
- Período de execução entre outubro de 2020 e abril de 2021

## Introdução

Este projeto foi desenvolvido como objeto de avaliação da unidade curricular PI3, compreendendo diversas etapas abordadas ao longo do semestre letivo 2020-2 do Instituto Federal de Santa Catarina (IFSC). 

A pandemia de Covid-19 iniciada em 2020 causou a proibição de aulas presenciais e o uso de laboratórios, acarretando em uma forte limitação do escopo desta atividade na questão de implementação e testes práticos. A unidade curricular PI3 tem o propósito de unir aprendizados de _software_ e _hardware_ dentro de um único projeto, porém para contornar a dependência de testes físicos complexos optou-se por um sistema mais virtual, com ênfase em comunicação e processamento em nuvem, e _hardware_ simplificado -- mas aberto a aprimoramentos futuros. 

Neste sentido surgiu a oportunidade de explorar a Amazon Web Services (AWS) e seu ambiente de desenvolvimento de robótica, o AWS RoboMaker, ainda pouco abordados no curso. A AWS é uma plataforma de desenvolvimento e computação em nuvem dos mais variados tipos de serviço, desde controle de frotas de robôs a instanciamento em larga escala de máquinas virtuais, ferramentas de _machine learning_ e análise de dados. Este aglomerado dá abertura a inúmeras possibilidades em empresas dentro e fora do ramo da tecnologia, visto que comunicação e automatização de processos com segurança digital são qualidades que podem afetar qualquer setor.

De maneira complementar, o sistema de reconhecimento de voz Alexa e uma placa Raspberry Pi foram cogitados como bons elementos para a integração de sistemas, constituindo o _frontend_ do _software_ e o _hardware_.

**Este repositório tem como função relatar os processos elaborados durante a unidade curricular mas também servir de tutorial para desenvolvedores. As etapas são descritas de forma a permitir a replicação do projeto, seguindo estratégias e _links_ disponíveis até o período de _push_, abril de 2021.**

## Proposta

-  Fazer o controle de um robô de forma remota, com comando por Alexa e acionamento elétrico em Raspberry Pi;
-   Utilização da plataforma Amazon Web Services (AWS) para comunicação entre os dispositivos;
- Executar ações de movimento do robô a partir do controle de motores elétricos ligados a rodas.  

## Arquitetura do projeto

O diagrama a seguir apresenta a arquitetura base do projeto proposto, retirada do tutorial [Build an Alexa controlled robot with AWS RoboMaker](https://aws.amazon.com/pt/blogs/robotics/build-alexa-controlled-robot/). A figura mostra os dois pontos a serem conectados nas extremidades laterais, o reconhecimento de voz por um dispositivo Alexa como o Amazon Echo e o acionamento de um robô. 

![enter image description here](https://d2908q01vomqb2.cloudfront.net/a9334987ece78b6fe8bf130ef00b74847c1d3da6/2020/07/16/alexa-blog-0_1.jpg)
Fonte: [Build an Alexa controlled robot with AWS RoboMaker](https://aws.amazon.com/pt/blogs/robotics/build-alexa-controlled-robot/)

> O _link_ citado aborda exatamente o sistema proposto para esse projeto, porém trechos desatualizados e pequenas inconsistências de dados requerem o uso adicional de outras fontes. 

Além da _skill_ Alexa e do controle de _hardware_ observa-se as etapas de função Lambda e AWS IoT, que serão exploradas a seguir neste trabalho. Abaixo destes é vista a tarefa do desenvolvedor vinculada ao AWS RoboMaker, responsável por elaborar os códigos, testá-los e aplicá-los em _hardware_. Todas estas conexões são feitas por meio da internet em serviços da Amazon, em que os pontos compartilham suas identificações e endereços para correto envio de dados.

O _hardware_ deve ser imaginado para se determinar as funções dos códigos e os equipamentos utilizados. Como já mencionado, há uma limitação de testes práticos e uso de periféricos, que dependeriam da disponibilidade nos laboratórios do IFSC. Optou-se então por comprometer-se com a movimentação do robô, o que dependeria de motores DC ligados às rodas e _drivers_ de corrente para a conexão com a Raspberry Pi. Esta alternativa é simples mas possibilita que se verifique o funcionamento apenas com circuitos básicos de LEDs ligados à placa. Além disso, ela é de fácil implementação assim que se obtenha acesso aos recursos da instituição e coloca à prova todo o sistema de _software_ e acionamento da Raspberry.


## Componentes necessários

- Conta no AWS Educate;
	> Entre em contato com seu professor ou instituição para saber como adquirir gratuitamente uma conta de estudante. É possível que este projeto seja desenvolvível com conta comum, mas esta não foi testada e pode requerer investimento financeiro;
- Conta no Alexa Developer Console;
- Raspberry 3 B+;
	> Modelo utilizado, não restrito;
- Cartão de 8 GB ou mais com OS Ubuntu 18.04
	> A versão do sistema operacional é restrita devido à compatibilidade com _softwares_ utilizados na etapa de simulação.

## Bons guias iniciais

Este pode ser o primeiro contato do leitor com robótica, Alexa e plataforma AWS. Em tal caso sugere-se alguns guias e tutoriais gratuitos para fornecer uma boa base no início do projeto:
- [Codecademy - Learn to Program Alexa](https://www.codecademy.com/learn/learn-alexa)
	- [Build Your First Alexa Skill (SDK v2)](https://www.codecademy.com/learn/learn-alexa/modules/learn-alexa-skills-kit)
	- [Create Your Lambda Function (SDK v2)](https://www.codecademy.com/learn/learn-alexa/modules/learn-alexa-lambda)
- Tutoriais do AWS Educate - _Badges_:
	-  _AWS RoboMaker - Introduction_;
    -   _RoboMaker Course 0: Robotic Fundamentals_;
    -   _RoboMaker Course 1b: Getting Started with AWS_;
    -   _AWS RoboMaker Course 2: ROS2 and ROS_;
    -   _IoT Badge_;
    -   _Alexa Badge_.

## Núcleos de trabalho
- **Primeira etapa**:
	- Desenvolvimento de arquivos para comunicação dentro das plataformas AWS e Alexa;
    - Escrita de algoritmo de controle do robô;
    - Simulação do robô no ambiente AWS RoboMaker;
- **Segunda etapa**:
    - Instalação de softwares e bibliotecas necessárias no sistema operacional usado pelo robô;
    - Adaptação do algoritmo para uso em Raspberry Pi 3 B+;
    - Teste laboratorial.

# Primeira etapa

A primeira etapa do projeto diz respeito aos sistemas em nuvem e simulação de _hardware_. De acordo com a imagem anterior há três estágios por trás da comunicação em nuvem: _skill_ Alexa, função Lambda e AWS IoT Topic. Estes três pontos são essencialmente interdependentes para testagem, mas cada um será descrito individualmente.

## Desenvolvimento de _Skill_ Alexa

Para se construir um robô controlado por comandos em Alexa é necessário que se tenha um reconhecimento de voz inteligente. Dispositivos Alexa devem ser capazes de identificar as palavras relacionadas a este caso específico e permitir a correta tomada de decisões. Uma _skill_ Alexa é um conjunto definido de instruções em linguagem humana a serem falados em voz alta pelo usuário final e detectados pelo dispositivo. O desenvolvedor deve considerar nesta etapa todas as ações que o robô pode tomar a cargo do usuário e como isso será comunicado, mas tanto a _skill_ quanto o Alexa Developer Console propiciam facilidade para se adaptar ou adicionar comandos no decorrer do tempo.

### Criação da _skill_

Tendo entrado no [Alexa Developer Console](https://developer.amazon.com/alexa/console/ask) com sua conta, a tela inicial será similar à imagem a seguir. Dê inicio aos passos:

1. Clique em `Criar Skill`.
<p align="center">
    <img width="100%" height="100%" src="imagens/imagem_00_AlexaInicio.jpg">
</p>

2. Preencha as seleções da primeira página:
	- **"Skill name"**: nome do conjunto de comandos utilizado no projeto. Este nome não será usado em nenhum código, mas deve ser de fácil identificação na possibilidade de a mesma pessoa trabalhar com várias _skills_ para projetos diferentes. Neste projeto utiliza-se o nome `PI3Robot-Skill-01`;
	- **"Default language"**: língua falada pelo usuário que dará o comando de voz. Deverá ser a mesma ao se definir os comandos em breve. A língua escolhida foi a inglesa, embora haja suporte para a portuguesa (PT/BR);
	- **"1. Choose a model to add to your skill"**: modelo pré-definido para dar início à _skill_. Nenhum dos oferecidos é envolvido com o projeto, portanto escolha `Custom`;
	- **"2. Choose a method to host your skill's backend resources"**:  função Lambda fornecida e hospedada pela Alexa na conta do desenvolvedor, para ser conectada à _skill_, criada automaticamente pelo console. Esta será desenvolvida individualmente no console AWS, portanto selecione `Provision your own`;
	> Embora a função Lambda seja criada posteriormente e hospedada a partir da conta AWS do estudante, seu código será  uma expansão do que o Alexa Development Console fornece no caso de se escolher a opção `Alexa-hosted (Python)`. 
	- Clique em `Create skill` no canto superior direito da tela.

<p align="center">
    <img width="100%" height="100%" src="imagens/imagem_01_CriarSkill01.jpg">
</p>

3. **"Choose a template to add to your skill"**: os comandos serão escritos do zero, portanto escolha `Start from Scratch`. Clique em `Choose` e a _skill_ será criada.

<p align="center">
    <img width="100%" height="100%" src="imagens/imagem_02_CriarSkill02.jpg">
</p>

Após criar a _skill_ o console fornece uma página conforme a figura a seguir.

<p align="center">
    <img width="100%" height="100%" src="imagens/imagem_03_CriarSkill03.jpg">
</p>

### Parâmetros e comandos da _skill_

Sendo concluída a criação da _skill_ é necessário definir as características da comunicação entre o dispositivo Alexa e o usuário. [Este tutorial da Codecademy](https://www.codecademy.com/learn/learn-alexa/modules/learn-alexa-skills-kit) explica com proficiência estes detalhes, de onde se tira a imagem a seguir.  

<p align="center">
    <img width="100%" height="100%" src="imagens/imagem_04_ParametrosSkill01.jpg">
</p>

A frase ilustra o que o usuário deve falar para se comunicar com o dispositivo Alexa. São destacadas as seguintes partes com seus exemplos:

- **"Wake word"**: palavra-chave para o dispositivo começar a voz captada. Trata-se do próprio nome `Alexa`;
- **"Starting phrase"**: início da frase, especifica qual tipo de requisição será passado. Pode ser de diferentes tipos, mas aqui será restrito ao `ask` pois será feito um "pedido" para que o robô se mova;
- **"Skill invocation name"**: Nome de invocação da _skill_. Não é o nome escolhido na etapa anterior, trata-se de um nome simples e memorável que o usuário irá falar para invocar tal _skill_. O exemplo utiliza o nome `History Buff` para chamar uma _skill_ de pesquisa de fatos históricos, mas neste projeto o usuário deve chamar pelo nome do robô;
- **"Utterance"**: especifica qual comando será buscado na _skill_ utilizada, por exemplo qual movimento será requisitado para se passar ao robô.

Estes dois últimos fatores devem ser configurados pelo desenvolvedor. O primeiro, nome de invocação da _skill_, pode ser alterado na aba **"Invocation"**, no lado esquerdo da tela. A figura a seguir mostra o caso, onde é visto também que o nome escolhido para chamar a _skill_ foi `robot one`.

<p align="center">
    <img width="100%" height="100%" src="imagens/imagem_05_ParametrosSkill02.jpg">
</p>

Cada possível comando passado por Alexa recebe o nome de _"Intent"_ (intenção). Deverão ser criados todos os _intents_ a se usar com o robô, portanto é necessário listar todos os movimentos que o sistema deverá reconhecer. Considerando que o _hardware_ terá um par de motores DC, controlando os lados esquerdo e direito, é possível 


