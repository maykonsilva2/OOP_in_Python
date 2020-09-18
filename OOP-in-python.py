'''
* NO CÒDIGO È OBRIGATÓRIO TER COMENTÁRIOS. 
    [x]- Deve existir uma Classe Mãe
    [x]- Todos os atributos da classe devem ser modificados apenas por métodos
    [x]- Deve ser possível visualizar todos os atributos do:
        [x]- aluno 
        []-funcionário.
    Criar um código que realize um cadastro de alunos e funcionarios em uma escola
        [x]- Cadastro aluno.
            Definir:
            1°- Nome
            2º- Idade
            3º- Bairro onde mora
            4º- classe escolar
            5º- Ano escolar
            6º- Nome do responsável do aluno
        [x]- Cadastro funciónario.
            Definir:
            1°- Nome
            2º- Idade
            3º- Bairro onde mora
            4º- Cargo
            5º- Sálario recebido

'''
 # Classe Pai
class Cadastro(object):
    def __init__(self, parametroNome, parametroIdade, parametroEndereco):
        self.__nome = parametroNome
        self.__idade = parametroIdade
        self.__endereco = parametroEndereco

        # Métodos que modificam os atributos da Classe Cadastro
#Método set e get nome
    def set_nome(self, a):
        self.__nome = a
    def get_nome(self):
        return self.__nome

#Método set e get idade
    def set_idade(self, a):
        self.__idade = a
    def get_idade(self):
        return self.__idade

# Método set e get endereço
    def set_endereco(self, a):
        self.__endereco = a
    def get_endereco(self):
        return self.__endereco

# Classe Filha
class cadastro_aluno(Cadastro):
    def __init__(self, parametroNome, parametroIdade, parametroEndereco, parametroClasse,parametroAnoEscolar, parametroResponsavel):
        super().__init__(parametroNome, parametroIdade, parametroEndereco)
        self.__classeEscolar = parametroClasse
        self.__anoEscolar = parametroAnoEscolar
        self.__responsavel = parametroResponsavel

    ''' O super() é utilizado entre heranças de classe, temos uma sub classe cadastro_aluno
    que herda da super classe Cadastro e utiliza o super() para chamar o método cosntrutor da classe Pai 
    em seu próprio método.
        A classe cadastro_aluno tem parametros adicionais como endereço e ano escolar do aluno e métodos
    '''

# Métodos que modificam os atributos do cadastro Aluno

#Método set e get da classe escolar do Aluno
    def set_classeEscolar(self, b):
        self.__classeEscolar = b
    def get_classeEscolar(self):
        return self.__classeEscolar

#Método set e get Ano Escolar do Aluno
    def set_anoEscolar(self, b):
        self.__anoEscolar = b
    def get_anoEscolar(self):
        return self.__anoEscolar

    
#Método set e get Responsavel do Aluno
    def set_responsavel(self, b):
        self.__responsavel = b
    def get_responsavel(self):
        return self.__responsavel

#Classe filha
class cadastro_funcionario(Cadastro):
    def __init__(self, parametroNome, parametroIdade, parametroEndereco, paramentroCargo, parametroSalario):
        super().__init__(parametroNome, parametroIdade, parametroEndereco)
        self.__cargo = paramentroCargo
        self.__salario = parametroSalario

# Métodos que modificam os atributos do cadastro funcionario
#Método set e get Cargo  do funcionario
    def set_cargo(self, c):
        self.__cargo = c
    def get_cargo(self):
        return self.__cargo

# Método set e get salario do funcionario
    def set_salario(self, c):
        self.__salario = c
    def get_salario(self):
        return self.__salario

def Formulario_aluno():
    # Chamada dos métodos
    print('\n############ Cadastrar Alunos ####################')
    print('###########Insira os dados a baixo#################\n')

    nomeAluno = input('Insira o nome do aluno: ')
    idadeAluno = input('Insira a idade do aluno: ')
    enderecoAluno = input('Insira o endereço do Aluno: ')
    classeEscolar = input('Insira a classe escolar do Aluno: ')
    anoEscolarAluno = input('Insira o ano escolar do Aluno: ')
    responsavelAluno = input('Insira o nome do Responsável pelo Aluno(a): ')


    #Intanciando a classe funcionario na variavél funcionario
    aluno = cadastro_aluno(nomeAluno, idadeAluno, enderecoAluno, classeEscolar,anoEscolarAluno, responsavelAluno )


    #Chamando os métodos da classe que encapsulam os dados inserido pelo usuario atribuindo os valores nas variavéis.
    mostrarNome_Aluno = aluno.get_nome()
    mostrarIdade_Aluno = aluno.get_idade()
    mostrarEndereco_Aluno = aluno.get_endereco()
    mostrarClasseEscolar = aluno.get_classeEscolar()
    mostrarAnoEscolar = aluno.get_anoEscolar()
    mostrarResponsavel_aluno = aluno.get_responsavel()

    #Impressão dos dados
    print('\n##########DADOS DO ALUNO##############\n')
    print('> O nome do aluno é: {}\n> Idade: {} anos\n> Mora no endereço: {}\n> Está  na classe escolar {} do {} ano escolar\n> O Responsável pelo Aluno: {}'.format(mostrarNome_Aluno, mostrarIdade_Aluno, mostrarEndereco_Aluno, mostrarClasseEscolar,mostrarAnoEscolar, mostrarResponsavel_aluno))
    print('########################################################')
    menu()

def formulario_funcionario():
    print('\n############ Cadastrar Funcionario ####################')
    print('###########Insira os dados a baixo#################\n')

    # Pegando as entradas dos dados do funcionario
    nomeFuncionario = input('Insira o nome do Funcionario: ')
    idadeFuncionario = input('Insira a Idade do Funcionario: ')
    enderecoFuncionario = input('Insira o endereço do Funcionario: ')
    cargoFuncionario = input('Insira o Cargo  do Funcionario: ')
    salarioFuncionario = input('Insira valor do salario do Funcionario: ')

    #Intanciando a classe funcionario na variavél funcionario
    funcionario = cadastro_funcionario(nomeFuncionario, idadeFuncionario, enderecoFuncionario, cargoFuncionario, salarioFuncionario)

    #Chamando os métodos da classe que encapsulam os dados inserido pelo usuario, atribuindo os valores nas variavéis.

    mostrarNome_func = funcionario.get_nome()
    mostrarIdade_func = funcionario.get_idade()
    mostrarEndereco_func = funcionario.get_endereco()
    mostrarCargo_func = funcionario.get_cargo()
    mostrarSlario_func = funcionario.get_salario()

    #Impressão dos dados
    print('\n##########DADOS DO Funcionario##############\n')
    print('> O nome do Funcionario é: {}\n> Idade: {} anos\n> Mora no endereço: {}\n> Exerce o cargo de {}    \n> Recebe o salario no valor R${}'.format(mostrarNome_func, mostrarIdade_func, mostrarEndereco_func, mostrarCargo_func,mostrarSlario_func))
    print('########################################################')
    menu()
# Menu Principal 

def menu():
    print('\n######Formulario de Cadastro#########')
    id_menu = input('Se deseja CADASTRAR UM ALUNO digite 1 e precione enter.\nSe deseja CADASTRAR UM FUNCIONÀRIO digite 2 e precione enter.')

    if id_menu == '1':
        Formulario_aluno()
    elif id_menu == '2':
        formulario_funcionario()
    else:
        print('\n###########OPÇÃO INVÁLIDA!, POR FAVOR ESCOLHA ENTRE AS OPÇÕES 1 E 2 DO MENU.#########\n')
        menu()

menu()