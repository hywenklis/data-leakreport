# Secure Report
**Secure Report** é uma aplicação web que oferece um canal seguro e prático para a denúncia de vazamentos de dados, com foco na proteção da privacidade e na confidencialidade das informações fornecidas. A plataforma permite que qualquer pessoa faça uma denúncia e acompanhe seu status, enquanto garante segurança e suporte a todo momento.

## 📌 Sobre o Projeto

A crescente importância da segurança da informação e da proteção de dados pessoais inspirou o desenvolvimento do **Secure Report**. Esta aplicação visa auxiliar pessoas e organizações a denunciarem vazamentos de dados de maneira segura e anônima, permitindo que a privacidade de todos seja preservada.

O projeto foi desenvolvido com foco em:

- **Segurança**: Todo o processo de denúncia é protegido e confidencial.
- **Transparência**: Relatórios para acompanhamento do status das denúncias.
- **Acessibilidade**: Interface intuitiva e fácil de usar.

---

## ⚙️ Funcionalidades

- **🔒 Denúncias Seguras**: Permite o envio de denúncias de forma anônima ou identificada, garantindo que as informações sejam tratadas com confidencialidade.
- **📊 Acompanhamento de Status**: Ferramenta de monitoramento que permite ao usuário acompanhar o progresso e status da denúncia.
- **📞 Suporte ao Usuário**: Canal direto de contato com a equipe de suporte, disponível para auxiliar o usuário em qualquer etapa do processo.

---

## 📝 Como Funciona

1. **Preenchimento do Formulário**: O usuário acessa o formulário de denúncia e fornece as informações necessárias de forma segura.
2. **Envio e Processamento**: A denúncia é armazenada de maneira segura, preservando a privacidade.
3. **Acompanhamento**: O usuário pode acompanhar o status da denúncia e visualizar relatórios diretamente pelo sistema.
4. **Suporte Disponível**: Caso precise de ajuda, o usuário pode contatar a equipe de suporte a qualquer momento.

---

## 📷 Capturas de Tela

### Página Inicial
*Interface limpa e funcional para introduzir o usuário ao sistema.*
  ![image](https://github.com/user-attachments/assets/6b5bf87e-d4c6-4e77-b5cb-8493aaeb7323)

### Formulário de Denúncia
*Formulário projetado para ser intuitivo e seguro, protegendo a confidencialidade das informações.*
![image](https://github.com/user-attachments/assets/62d049ac-79a4-4e7e-b798-2b958a71e92f)
![image](https://github.com/user-attachments/assets/201c26f6-6231-405f-8bb5-87d91e28fd6c)
![image](https://github.com/user-attachments/assets/95bb3049-32fb-40bd-80b9-ac265a3c1e4e)

### Acompanhamento de Status
*Painel para monitoramento do status das denúncias, promovendo transparência e controle.*
![image](https://github.com/user-attachments/assets/65961f72-04be-42e9-8204-5f4869188750)
![image](https://github.com/user-attachments/assets/ab34bee3-317e-4587-9554-b1d5332e65a0)

## 🛠️ Tecnologias Utilizadas

O **Secure Report** foi desenvolvido utilizando uma combinação de tecnologias robustas e eficientes, garantindo desempenho e segurança:

- **Front-end**: HTML, CSS (Bootstrap), FontAwesome, Google Fonts
- **Back-end**: Django (Python)
- **Banco de Dados**: PostgreSQL
- **Contêinerização**: Docker

---

## 🚀 Instalação e Configuração

### Pré-requisitos
- **Python** e **Django** instalados no sistema
- **Docker** para rodar a aplicação e o banco de dados em contêineres

### Passo a Passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/hywenklis/data-leakreport.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd data-leakreport
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente e o banco de dados conforme necessário.

5. Execute a aplicação:
   ```bash
   python manage.py runserver
   ```

### Docker

Para iniciar a aplicação usando Docker:

```bash
docker-compose up -d
```

Após subir o Docker, entre no contêiner `web` para rodar as migrações necessárias:

```bash
docker exec -it nome_do_container_web python manage.py migrate
```
