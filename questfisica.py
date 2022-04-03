#perguntas e respostas

print('Bem vindo ao jogo de perguntas e respostas.\nEscolha uma alternativa, (a), (b) ou (c), e veja quantos pontos você acertou!')

perguntas = {
    'Pergunta 1': {
        'pergunta': ' Qual a raiz quadrada de 9?',
        'respostas': {
            'a': '1',
            'b': '3',
            'c': '6',
        },
        'resposta certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': ' Qual o número de pi?',
        'respostas': {
            'a': '3,14',
            'b': '3',
            'c': '3,15',
        },
        'resposta certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': ' Qual a terceira lei da termodinâmica?',
        'respostas': {
            'a': 'Um corpo em repouso tende a continuar em repouso se não há a interação com um segundo corpo.',
            'b': 'As trocas de calor que têm tendência para igualar temperaturas diferentes, o que acontece de forma espontânea.',
            'c': 'A entropia de um sistema com temperatura igual a zero absoluto tem uma constante pouco variável.',
        },
        'resposta certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': ' Qual a segunda lei da robótica?',
        'respostas': {
            'a': 'Os robôs devem obedecer às ordens dos humanos, exceto nos casos em que tais ordens entrem em conflito com a primeira lei.',
            'b': 'Um robô não pode ferir um humano ou permitir que um humano sofra algum mal.',
            'c': 'Um robô deve proteger sua própria existência, desde que não entre em conflito com as leis anteriores',
        },
        'resposta certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': ' Qual a fórumla da relativividade geral?',
        'respostas': {
            'a': 'Q = k x A x (TD-TE)/l, em que Q é o débito de calor de D para E, A é a área da secção reta, l o comprimento da barra, TD e TE as temperaturas nos extremos da barra e k é a condutibilidade térmica do material de que é feita a barra.',
            'b': 'Se um fluido estiver escoando em um estado de fluxo contínuo, então a pressão depende da velocidade do fluido.',
            'c': 'A energia (E) pode ser representada pela massa do objeto (m) multiplicada pela velocidade da luz ao quadrado (c²).',
        },
        'resposta certa': 'c',
    },
    'Pergunta 6': {
        'pergunta': 'A fórmula: F(n + 2) = F(n + 1) + F(n) , com n ≥ 1 e F(1) = F(2) = 1 , se refere a qual trato matemático?',
        'respostas': {
            'a': 'Sequência de Fibonacci.',
            'b': 'Recursiva de Newton.',
            'c': 'Retorno sequencial.',
        },
        'resposta certa': 'a',
    },
    'Pergunta 7': {
        'pergunta': 'Qual a terceira lei de Kepler?',
        'respostas': {
            'a': 'Todos os planetas movem-se ao redor do Sol em órbitas elípticas, estando o Sol em um dos focos.',
            'b': 'O quadrado do período orbital (T²) de um planeta é diretamente proporcional ao cubo de sua distância média ao Sol (R³).',
            'c': 'Ao traçarmos uma reta que vai de um planeta até o Sol, a área varrida por essa reta ao longo da órbita será sempre igual para intervalos de tempos iguais, independentemente de qual seja a posição inicial do planeta.',
        },
        'resposta certa': 'b',
    },

}

print()
respostacerta = 0

for pk,pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')
    print('Alternativas:')
    for rk,rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    respostausuario = input('Sua resposta é: ')
    if respostausuario == pv['resposta certa']:
        print('Você acertou essa pergunta.')
        respostacerta += 1
    else:
        print('Você errou essa pergunta, estude mais.')
    print()

print('Você acertou {} perguntas de um total de 7 perguntas.'.format(respostacerta))

if respostacerta < 5:
    print('Você acertou muito pouco, estude mais!')
elif respostacerta == 7:
    print('Parabéns você acertou todas!')
else:
    print('Você acertou 5 ou mais perguntas, parabéns, continue estudando!')



