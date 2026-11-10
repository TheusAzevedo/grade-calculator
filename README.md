![Repo Size](https://shields.io)
![Languages](https://shields.io)
![Status](https://shields.io)

# Integrated Academic Portal & Grade Calculator

## Brazilian Portuguese Version

### Como Testar o Projeto (Credenciais de Acesso)

Para testar as diferentes regras de negócio e permissões do sistema, utilize os acessos abaixo:

#### Visão do Estudante (Student)
- Login Padrão: `student@school.com`
- Senha Padrão: `student123`
- Nota: Você também pode criar um novo cadastro informando um e-mail válido. O sistema gerará um ID (RA) único para o aluno de forma permanente.

#### Visão do Professor (Teacher Staff)
- Login Padrão: `teacher@school.com`
- Senha Padrão: `teacher123`
- Chave de Acesso Institucional (Access Key): `SCHOOL2026`

### Testes Automatizados (Python)

Para validar a integridade das expressões regulares (Regex) e os filtros de segurança defensiva do terminal sem precisar preencher os dados manualmente, você pode executar a suíte de testes unitários integrada.

Abra o terminal na raiz do projeto e execute o seguinte comando:

```bash
python -m unittest terminal/test_calculator.py
```

## English Version

### How to Test the Project (Access Credentials)

To test the different business rules and system permissions, use the credentials below:

#### Student View
- Default Login: `student@school.com`
- Default Password: `student123`
- Note: You can also create a new account by providing a valid email format. The system will automatically generate a unique Student ID (RA) for the user.

#### Teacher Staff View
- Default Login: `teacher@school.com`
- Default Password: `teacher123`
- Institutional Access Key (Master Token): `SCHOOL2026`

### Automated Unit Testing (Python)

To validate the integrity of the regular expressions (Regex) and defensive security filters in the terminal without manual inputs, you can run the integrated unit testing suite.

Open your terminal in the root directory and execute the following command:

```bash
python -m unittest terminal/test_calculator.py
```