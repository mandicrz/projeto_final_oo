<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notas de Corte</title>
    <link rel="stylesheet" type="text/css" href="/static/css/passou.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montagu+Slab:opsz,wght@16..144,100..700&display=swap"> 
</head>
<body>
    <header class="header">
        <h1 class="header-title">Calculadora Vestibular Tradicional UnB</h1>
        <nav class="header-nav">
            <div class="nav-icons">
                <a href="#" id="dark-mode-toggle" class="icon-button" ><img src="/static/img/dark_mode.png" alt=""></a>
                <form  action="/home/{{current_user}}" method="GET">
                    <button type="submit" class="icon-button"><img src="/static/img/Home.png" alt=""></button>
                </form>
                <div class="user-menu">
                    <a href="#" class="icon-button"><img src="/static/img/user.png" alt=""></a>
                    <div class="user-menu-content">
                        <form id="logout" action="/editar-informacoes" method="GET">
                            <button type="submit">Editar informações</button>
                        </form>
                        <form id="logout" action="/logout" method="POST">
                            <button type="submit">Logout</button>
                        </form>
                    </div>
                </div>   
            </div>
        </nav>
    </header>

    <form action="/passou" method="POST">
        <label>Sistema de disputa</label>
                <select name="sistema">
                    <option value="Universal">Universal</option>
                    <option value="Sistema de Cotas para Negros">Sistema de Cotas para Negros</option>
                    <option value="Publica renda <= 1.5 PPI">Publica renda <= 1.5 PPI</option>
                    <option value="Publica renda <= 1.5 PPI e PCD">Publica renda <= 1.5 PPI e PCD</option>
                    <option value="Publica renda <= 1.5  nao PPI">Publica renda <= 1.5  nao PPI</option>
                    <option value="Publica renda <= 1.5 nao PPI e PCD">Publica renda <= 1.5 nao PPI e PCD</option>
                    <option value="Publica renda >= 1.5 PPI">Publica renda >= 1.5 PPI</option>
                    <option value="Publica renda >= 1.5 PPI e PCD">Publica renda >= 1.5 PPI e PCD</option>
                    <option value="Publica renda >= 1.5  nao PPI">Publica renda >= 1.5  nao PPI</option>
                    <option value="Publica renda >= 1.5 nao PPI e PCD">Publica renda >= 1.5 nao PPI e PCD</option>
                </select>
    
        % if transfered3:
            <label>Selecione o argumento para comparar</label>
                    <select name="Argumentos_1_Salvos">
                        % for arg1 in argGrupo1:
                        <option value={{arg1}} type="number">{{arg1}}</option>
                        %end 
                    </select>
                    <select name="Argumentos_2_Salvos">
                        % for arg2 in argGrupo2:
                        <option value={{arg2}} type="number">{{arg2}}</option>
                        %end 

                    </select>
        %else:
            <p>Você não tem argumentos no sistema, vá para calcular argumento e depois volte aqui<p/>
        %end

        <button id="verificar" type="submit">Verificar</button>
    <form/>
    % if transfered2:
    <div>
        <table class="tabela">
            <tr>
                <th colspan="4">Aprovado | Grupo 1</th>
            </tr>
        % for notas in passou1:

            <tr>

                <td>{{notas[0]}}</td>
                <td>{{notas[1]}}</td>
                <td>{{notas[2]}}</td>
                <td>{{notas[i]}}</td>

            </tr>
        % end 

        </table>

        <table class="tabela">
            <tr>
                <th colspan="4">Reprovado | Grupo 1</th>
            </tr>
        % for notas in naoPassou1:

            <tr>

                <td>{{notas[0]}}</td>
                <td>{{notas[1]}}</td>
                <td>{{notas[2]}}</td>
                <td>{{notas[i]}}</td>

            </tr>
        % end 
        </table>

                <table class="tabela">
            <tr>
                <th colspan="4">Aprovado | Grupo 2</th>
            </tr>
        % for notas in passou2:

            <tr>

                <td>{{notas[0]}}</td>
                <td>{{notas[1]}}</td>
                <td>{{notas[2]}}</td>
                <td>{{notas[i]}}</td>

            </tr>
        % end 

        </table>
        
        <table class="tabela">
            <tr>
                <th colspan="4">Reprovado | Grupo 2</th>
            </tr>
        % for notas in naoPassou2:

            <tr>

                <td>{{notas[0]}}</td>
                <td>{{notas[1]}}</td>
                <td>{{notas[2]}}</td>
                <td>{{notas[i]}}</td>

            </tr>
        % end 
        </table>
        
    <div/>
    % end
    <script src="/static/js/index.js"></script>

</body>
</html>