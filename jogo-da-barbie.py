# Jogo da Barbie
# Um jogo de decisões na qual vários personagens e cenários podem ser criados baseados nas respostas dadas pelo usuário

class JogoDaBarbie:
    def __init__(self):
        self.pergunta1 = 'Você é fã de filmes Clássicos ou filmes Modernos? (Clássicos/Modernos) '
        self.pergunta2 = 'Você prefere Comprar algo ou Estilizar algo? (Comprar/Estilizar) '
        self.pergunta3 = 'Você prefere o estilo mais Fashion ou o estilo mais Casual? (Fashion/Casual) '

    def iniciar(self):
        resposta1 = str(input(self.pergunta1)).upper().strip()
        if resposta1 == 'CLÁSSICOS':
            resposta1b = str(input(self.pergunta2)).upper().strip()
            if resposta1b == 'COMPRAR':
                resposta1c = str(input(self.pergunta3)).upper().strip()
                if resposta1c == 'FASHION':
                    print('Você é a Clássica Barbie Fashionista! Você adora comprar e estar por dentro de todas as '
                          'tendências!')
                elif resposta1c == 'CASUAL':
                    print('Você é a Clássica Barbie Designer de Moda! Você ama comprar mas não tem medo de optar por '
                          'looks mais fora do padrão!')
            if resposta1b == 'ESTILIZAR':
                resposta1d = str(input(self.pergunta3)).upper().strip()
                if resposta1d == 'CASUAL':
                    print('Você é a Clássica Barbie Designer de Interiores! Você adorar decorar e estilizar, '
                          'sem perder mão de outfits chiques e casuais!')
                elif resposta1d == 'FASHION':
                    print('Você é a Clássica Barbie Arquiteta! Você gosta de decorar e se manter na moda!')
        if resposta1 == 'MODERNOS':
            resposta1e = str(input(self.pergunta2)).upper().strip()
            if resposta1e == 'COMPRAR':
                resposta1f = str(input(self.pergunta3)).upper().strip()
                if resposta1f == 'FASHION':
                    print('Você é a Moderna Barbie Personal Shopper! Você ama comprar e estar na frente de todas as '
                          'tendências!')
                elif resposta1f == 'CASUAL':
                    print('Você é a Moderna Barbie Artista! Super moderna e descolada!')
            if resposta1e == 'ESTILIZAR':
                resposta1g = str(input(self.pergunta3)).upper().strip()
                if resposta1g == 'FASHION':
                    print('Você é a Moderna Barbie Programadora! Você é moderninha sem abrir mão do estilo!')
                elif resposta1g == 'CASUAL':
                    print('Você é a Moderna Barbie Publicitária! Você é moderninha e casual e ama passar horas '
                          'criando novas campanhas!')


jogo = JogoDaBarbie()
jogo.iniciar()
