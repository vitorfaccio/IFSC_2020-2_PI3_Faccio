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

A pandemia de Covid-19 iniciada em 2020 causou a proibição de aulas presenciais e o uso de laboratórios, acarretando em uma forte limitação do escopo desta atividade na questão de implementação e testes práticos. A unidade curricular PI3 tem o propósito de unir aprendizados de _software_ e _hardware_ dentro de um único projeto, porém para contornar a dependência de testes físicos complexos optou-se por um sistema mais virtual, com ênfase em comunicação e processamento em nuvem, e _hardware_ simplificado mas aberto a aprimoramentos futuros. 

Neste sentido surgiu a oportunidade de explorar a plataforma Amazon Web Services (AWS) e seu ambiente de desenvolvimento de robótica, o AWS RoboMaker, ainda pouco abordado no curso. De maneira complementar, o sistema de reconhecimento de voz Alexa e uma placa Raspberry Pi foram cogitados como bons elementos para a integração de sistemas, constituindo o _frontend_ do _software_ e o _hardware_.

**Este repositório tem como função relatar os processos elaborados durante a unidade curricular mas também servir de tutorial para desenvolvedores. As etapas são descritas de forma a permitir a replicação do projeto, seguindo estratégias e _links_ disponíveis até o período de _commit_, abril de 2021.**

## Proposta

-  Fazer o controle de um robô de forma remota, com comando por Alexa e acionamento elétrico em Raspberry Pi;
    
-   Utilização da plataforma Amazon Web Services (AWS) para comunicação entre os dispositivos.

O diagrama a seguir apresenta a arquitetura base do projeto proposto, retirada do tutorial [Build an Alexa controlled robot with AWS RoboMaker](https://aws.amazon.com/pt/blogs/robotics/build-alexa-controlled-robot/). O texto aborda exatamente o sistema proposto para esse projeto, porém _links_ desatualizados e pequenas inconsistências de dados sugerem o uso adicional de outras fontes.

![enter image description here](https://d2908q01vomqb2.cloudfront.net/a9334987ece78b6fe8bf130ef00b74847c1d3da6/2020/07/16/alexa-blog-0_1.jpg)
Fonte: [Build an Alexa controlled robot with AWS RoboMaker](https://aws.amazon.com/pt/blogs/robotics/build-alexa-controlled-robot/)

A figura mostra os dois pontos a serem conectados, o reconhecimento de voz por um dispositivo Alexa e o acionamento de um robô. Além da _skill_ Alexa e do controle de _hardware_ observa-se as etapas de função Lambda e AWS IoT, que serão exploradas a seguir neste trabalho. Abaixo destes é vista a tarefa do desenvolvedor vinculada ao AWS RoboMaker, responsável por elaborar os códigos, testá-los e aplicá-los em _hardware_.

## Componentes necessários

- Conta no AWS Educate;
	- Entre em contato com seu professor ou instituição para saber como adquirir gratuitamente uma conta de estudante;
	- É possível que este projeto seja desenvolvível com conta comum, mas esta não foi testada e pode requerer investimento financeiro;
- Conta no Alexa Developer Console;
- Raspberry 3 B+;
	- Modelo utilizado, não restrito;
- Cartão de 8 GB ou mais com OS Ubuntu 18.04
	- A versão do sistema operacional é restrita devido à compatibilidade com _softwares_ utilizados na etapa de simulação.

## Bons guias iniciais

Este pode ser o primeiro contato do leitor com robótica, Alexa e plataforma AWS. Desta forma sugere-se alguns guias e tutoriais gratuitos para fornecer uma boa base no início do projeto:
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
    - Instalação de softwares e bibliotecas necessárias no sistema operacional usado;
    - Adaptação do algoritmo para uso em Raspberry Pi 3 B+;
    - Teste laboratorial.

# Primeira etapa
