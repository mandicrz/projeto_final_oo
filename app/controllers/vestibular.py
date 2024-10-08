from csv import reader 
class Vestibular():
    
    def __init__(self):
        self.grupo = self._setGrupo()
        self.notaCorte = self._setNotaCorte()
        
        #media
        self.media_esp = 9.723
        self.media_ing = 15.680
        self.media_fra = 12.710
        self.media_parte_2 = 59.640
        self.media_parte_3 = 32.146
        self.media_red = 7.107
        
        #desvio padrão
        self.dp_esp = 5.894
        self.dp_ing = 6.260
        self.dp_fra = 6.873
        self.dp_parte_2 = 18.954
        self.dp_parte_3 = 24.914
        self.dp_red = 1.777
    
    #retorna uma matriz onde cada linha representa um curso 
    # coluna 0 = grupo e 1 = nome do curso
    
    def _setGrupo(self):
        with open('app/controllers/csv/ED_1_VESTUNB_2024_ABERTURA_organized-_2_.csv') as arquivo:
            cursos=[]
            leitor_csv = reader(arquivo)
            for linha in leitor_csv:
                cursos.append(linha)
            return cursos
    
    def _setNotaCorte(self):
        with open('app/controllers/csv/2024_Boletim-informativo_VestUnB_organized-_1_.csv') as arquivo:
            cursos=[]
            leitor_csv = reader(arquivo)
            for linha in leitor_csv:
                cursos.append(linha)
            return cursos
        
    def calcEstg(self,acertos_ta_estg,erros_ta_estg,acertos_tb_estg,acertos_tc_estg,erros_tc_estg,acertos_td_estg):
        pontuacao_estg = acertos_ta_estg - erros_ta_estg + (acertos_tb_estg)*2 + (acertos_tc_estg)*2 -(erros_tc_estg)*0.667+ acertos_td_estg
        return pontuacao_estg
    def calcP2(self,acertos_ta_parte_2,erros_ta_parte_2,acertos_tb_parte_2,acertos_tc_parte_2,erros_tc_parte_2,acertos_td_parte_2):
        pontuacao_parte_2 = acertos_ta_parte_2 - erros_ta_parte_2 + (acertos_tb_parte_2)*2 + (acertos_tc_parte_2)*2 -(erros_tc_parte_2)*0.667+ acertos_td_parte_2
        return pontuacao_parte_2
    def calcP3(self,acertos_ta_parte_3,erros_ta_parte_3,acertos_tb_parte_3,acertos_tc_parte_3,erros_tc_parte_3,acertos_td_parte_3):
        pontuacao_parte_3 = acertos_ta_parte_3 - erros_ta_parte_3 + (acertos_tb_parte_3)*2 + (acertos_tc_parte_3)*2 -(erros_tc_parte_3)*0.667+ acertos_td_parte_3
        return pontuacao_parte_3
    
    def argEstg(self, calcEstg, lingua):
        if lingua == 'ingles':
            nota_estg=10*(calcEstg-self.media_ing)/self.dp_ing
        elif lingua == 'espanhol' :
            nota_estg=10*(calcEstg-self.media_esp)/self.dp_esp
        else:
            nota_estg=10*(calcEstg-self.media_fra)/self.dp_fra
        return nota_estg
    
    def argP2(self,calcP2):
        nota_parte_2=10*(calcP2-self.media_parte_2)/self.dp_parte_2
        return nota_parte_2
    
    def argP3(self,calcP3):
        nota_parte_3=10*(calcP3-self.media_parte_3)/self.dp_parte_3
        return nota_parte_3
    def argRed(self,notaRedacao):
        nota_red= 10*(notaRedacao-self.media_red)/self.dp_red
        return nota_red
    def argFinal(self,argEstg,argP2,argP3,argRed):
        argumento_final_gp_1 = 2*argEstg + 6*argP2 + 5*argP3 + 1.5*argRed
        argumento_final_gp_2 = argEstg + 4*argP2 + 8*argP3 + 1.5*argRed
        return argumento_final_gp_1,argumento_final_gp_2

class Vestibulando():
    def __init__(self):
        self.vestibular= Vestibular()
        self.cota= ""

        # Parte 1: Estrangeira
        self.acertos_ta_estg = 0
        self.erros_ta_estg = 0
        self.acertos_tb_estg = 0
        self.acertos_tc_estg = 0
        self.erros_tc_estg = 0
        self.erros_td_estg = 0

        # Parte 2: Humanas
        self.acertos_ta_parte_2 = 0
        self.erros_ta_parte_2 = 0
        self.acertos_tb_parte_2 = 0
        self.acertos_tc_parte_2 = 0
        self.erros_tc_parte_2 = 0
        self.erros_td_parte_2 = 0

        # Parte 3: Exatas
        self.acertos_ta_parte_3 = 0
        self.erros_ta_parte_3 = 0
        self.acertos_tb_parte_3 = 0
        self.acertos_tc_parte_3 = 0
        self.erros_tc_parte_3 = 0
        self.erros_td_parte_3 = 0
        
        # Redação
        self.notaRedacao = 0.0

    def passou(self,arg1,arg2,sistema):
        i=21
        if sistema =='Universal':
            i = 21
        elif sistema == 'Sistema de Cotas para Negros':
            i = 3
        elif sistema == 'Publica renda <= 1.5 PPI':
            i = 5
        elif sistema == 'Publica renda <= 1.5 PPI e PCD':
            i = 7
        elif sistema == 'Publica renda <= 1.5  nao PPI':
            i = 9
        elif sistema == 'Publica renda <= 1.5 nao PPI e PCD':
            i = 11
        elif sistema == 'Publica renda >= 1.5 PPI':
            i = 13
        elif sistema == 'Publica renda >= 1.5 PPI e PCD':
            i = 15
        elif sistema == 'Publica renda >= 1.5  nao PPI':
            i = 17
        elif sistema == 'Publica renda >= 1.5 nao PPI e PCD':
            i = 19

        
        passou1 = []
        naoPassou1 = []
        passou2 = []
        naoPassou2 = []

        for notas in self.vestibular.notaCorte:
            try:
                if notas[i] == "-" or isinstance(notas[i], list):
                    notas[i] = -9999
    
                for grupo in self.vestibular.grupo:
                    if grupo[1] == notas[2]:
                        if grupo[0] == 'I':
                            if arg1 < float(notas[i]):
                                if notas[i] == -9999:
                                    notas[i] = "-"
                                naoPassou1.append(notas)
                            else:
                                if notas[i] == -9999:
                                    notas[i] = "-"
                                passou1.append(notas)
                        else:
                            if arg2 < float(notas[i]):
                                if notas[i] == -9999:
                                    notas[i] = "-"
                                naoPassou2.append(notas)
                            else:
                                if notas[i] == -9999:
                                    notas[i] = "-"
                                passou2.append(notas)
            except (ValueError, TypeError) as e:
                print(f"Erro ao processar o valor: {notas[i]} - {str(e)}")

        return passou2, passou1, naoPassou2, naoPassou1, i





            

        
        