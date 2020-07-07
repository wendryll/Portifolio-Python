"""Faça um programa que tenha uma função nota() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
-Quantidades de notas              -A maior nota
-A menor nota                      -A média da turma
-A situação(opcional)              -Adicione também as docstrings"""  

def nota(* notas,situacao = False):
    """
    -> Função para analiasar notas do aluno
        parametro *notas: diveresas notas do aluno
        parametro situação:(opcional) mostrar ou não a situação 
        return: retorna a ficha do aluno
    """
    aluno = dict()
    aluno['total'] = len(notas)
    aluno['maior'] = max(notas)
    aluno['menor'] = min(notas)
    aluno['media'] = (sum(notas)/len(notas))
    if situacao == True:
        if aluno['media'] > 6:
            aluno['situacao'] = 'Aprovado'
        else:
            aluno['situcao'] = 'Reprovado'
    return aluno

r = nota(5,6,7,8,situacao=True)
print(r)