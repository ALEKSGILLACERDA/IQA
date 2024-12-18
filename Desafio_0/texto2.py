texto = """
Python é uma linguagem de programação de alto nível, [5] 
interpretada de script, imperativa, orientada a objetos, funcional, de 
tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. [1] Atualmente, 
possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização 
sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem 
padrões e especificações formais, a linguagem, como um todo, não é formalmente especificada. O 
padrão na prática é a implementação CPython. A linguagem foi projetada com a filosofia de enfatizar 
a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do 
código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos 
poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros
"""

texto_modificado = texto.replace("Python", "Fython").replace("CPython", "CFython").replace("python", "fython")

print(texto_modificado)