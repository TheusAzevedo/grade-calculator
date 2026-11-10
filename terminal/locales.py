import os

# textos por idioma
translations = {
    "en": {
        "portalTitle": "               ACADEMIC PORTAL               ",
        "menuSignIn": "1. Sign In",
        "menuRegister": "2. Create Student Account",
        "menuLanguage": "3. Change Location / Language",
        "currentLoc": "Global | EN",
        "locHeader": "----------- YOUR LOCATION / IDIOMA -----------",
        "locCurrent": "Current Selection: ",
        "regTitle": "--- STUDENT REGISTRATION ---",
        "signInTitle": "--- SIGN IN ---",
        "fieldFirstName": "First Name: ",
        "fieldLastName": "Last Name: ",
        "fieldEmail": "Email: ",
        "fieldPassword": "Password (Min 6 chars): ",
        "fieldPasswordLogin": "Password: ",
        "fieldConfirmPassword": "Confirm Password: ",
        "errRequired": "\n❌ Validation Error: All fields are required.",
        "errName": "\n❌ Security Error: Names must contain only letters and be at least 2 chars long.",
        "errEmail": "\n❌ Security Error: Invalid email format. Use: user@domain.com",
        "errPassLength": "\n❌ Security Error: Password must be at least 6 characters long.",
        "errPassMatch": "\n❌ Validation Error: Passwords do not match.",
        "errEnumMitigation": "\n❌ Unable to complete registration with the information provided. Please verify your email or try again later.",
        "successReg": "\n✅ Account processed! Your PERMANENT ID (RA) is: ",
        "errWrongCreds": "\n❌ Wrong email or password.",
        "studentHeader": "Student - ",
        "menuViewReport": "1. View My Report Card",
        "menuLogout": "2. Logout",
        "reportHeader": "--- OFFICIAL ACADEMIC REPORT ---",
        "reportName": "Name:    ",
        "reportGrades": "Grades:  ",
        "reportAverage": "Average: ",
        "reportStatus": "Status:  ",
        "noGradesYet": "Your grades have not been released by the teacher yet.",
        "menuLaunchGrades": "1. Enter Student Grades (By ID)",
        "menuViewHistory": "2. View Grade History",
        "menuLogoutTeacher": "3. Logout",
        "launchHeader": "--- LAUNCH STUDENT GRADES ---",
        "fieldStudentID": "Enter Student ID (RA): ",
        "errIDNotFound": "\n❌ Error: Student ID not found in database.",
        "fieldGrade": "Grade ",
        "errNumber": "⚠ Enter a valid number.",
        "errGradeBounds": "⚠ Grade must be between 0 and 10.",
        "successLaunch": "\n✅ Report card updated successfully!",
        "historyEmpty": "No records yet.",
        "pressEnter": "Press Enter to continue...",
        "pressEnterBack": "\nPress Enter to go back...",
        "pressEnterTry": "\nPress Enter to try again..."
    },
    "pt": {
        "portalTitle": "               PORTAL ACADÊMICO              ",
        "menuSignIn": "1. Entrar (Sign In)",
        "menuRegister": "2. Criar Conta de Aluno",
        "menuLanguage": "3. Mudar Localização / Idioma",
        "currentLoc": "Brasil | PT",
        "locHeader": "----------- SUA LOCALIZAÇÃO / IDIOMA -----------",
        "locCurrent": "Seleção Atual: ",
        "regTitle": "--- CADASTRO DE ALUNO ---",
        "signInTitle": "--- TELA DE LOGIN ---",
        "fieldFirstName": "Primeiro Nome: ",
        "fieldLastName": "Sobrenome: ",
        "fieldEmail": "E-mail: ",
        "fieldPassword": "Senha (Mín. 6 caracteres): ",
        "fieldPasswordLogin": "Senha: ",
        "fieldConfirmPassword": "Confirmar Senha: ",
        "errRequired": "\n❌ Erro de Validação: Todos os campos são obrigatórios.",
        "errName": "\n❌ Erro de Segurança: Os nomes devem conter apenas letras e ter no mínimo 2 caracteres.",
        "errEmail": "\n❌ Erro de Segurança: Formato de e-mail inválido. Use: usuario@dominio.com",
        "errPassLength": "\n❌ Erro de Segurança: A senha deve ter pelo menos 6 caracteres.",
        "errPassMatch": "\n❌ Erro de Validação: As senhas não coincidem.",
        "errEnumMitigation": "\n❌ Não foi possível concluir o cadastro com os dados informados. Verifique seu e-mail ou tente novamente mais tarde.",
        "successReg": "\n✅ Conta processada! Seu ID Permanente (RA) é: ",
        "errWrongCreds": "\n❌ E-mail ou senha incorretos.",
        "studentHeader": "Aluno - ",
        "menuViewReport": "1. Visualizar Meu Boletim",
        "menuLogout": "2. Sair (Logout)",
        "reportHeader": "--- BOLETIM ACADÊMICO OFICIAL ---",
        "reportName": "Nome:    ",
        "reportGrades": "Notas:   ",
        "reportAverage": "Média:   ",
        "reportStatus": "Status:  ",
        "noGradesYet": "Suas notas ainda não foram lançadas pelo professor.",
        "menuLaunchGrades": "1. Lançar Notas do Aluno (Por ID)",
        "menuViewHistory": "2. Visualizar Histórico de Notas",
        "menuLogoutTeacher": "3. Sair (Logout)",
        "launchHeader": "--- LANÇAMENTO DE NOTAS ---",
        "fieldStudentID": "Digite o ID do Estudante (RA): ",
        "errIDNotFound": "\n❌ Erro: ID do estudante não encontrado no banco de dados.",
        "fieldGrade": "Nota ",
        "errNumber": "⚠ Digite um número válido.",
        "errGradeBounds": "⚠ A nota deve estar entre 0 e 10.",
        "successLaunch": "\n✅ Boletim atualizado com sucesso!",
        "historyEmpty": "Nenhum registro encontrado.",
        "pressEnter": "Pressione Enter para continuar...",
        "pressEnterBack": "\nPressione Enter para voltar...",
        "pressEnterTry": "\nPressione Enter para tentar novamente..."
    }
}

current_lang = "en"


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def location_menu():
    global current_lang
    while True:
        limpar()
        t = translations[current_lang]
        print("=" * 47)
        print(t["locHeader"])
        print("=" * 47)
        print(t["locCurrent"] + "[ " + t["currentLoc"] + " ]")
        print()

        print("[ Worldwide ]")
        print("  1. 🌐 Global | EN")
        print()
        print("[ Americas ]")
        print("  2. 🇧🇷 Brazil | PT")
        print("  3. 🇦🇷 Argentina | ES (Disabled)")
        print("  4. 🇨🇦 Canada | EN    (Disabled)")
        print("=" * 47)
        print("  5. Back to Portal (Voltar)")
        print("=" * 47)

        op = input("> ").strip()
        if op == "1":
            current_lang = "en"
        elif op == "2":
            current_lang = "pt"
        elif op == "5":
            break