-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Quem iniciou o curso, quantas aulas em média assistiu?


-- Para esse exercício, precisamos identificar quem participou da primeira aula.
WITH primeiroDia AS (
    SELECT 
        DISTINCT IdCliente AS primeirosClientes
    FROM transacoes
    WHERE substr(DtCriacao,1,10) = '2025-08-25'
),

-- Quais alunos assistiram aulas em cada dia
diasCurso AS (
    SELECT DISTINCT
        IdCliente AS clientesDias,
        substr(DtCriacao,1,10) AS presenca_dia
    FROM transacoes
    WHERE substr(DtCriacao,1,10) >= '2025-08-25' AND substr(DtCriacao,1,10) < '2025-08-30'
),
-- Identificar quem do primeiro dia, quantas aulas assistiu
join_alunos_desde_primeiro AS (
    SELECT
        clientesDias,
        COUNT(*) AS qtde_dias,
        presenca_dia
    FROM primeiroDia pd
    JOIN diasCurso ON primeirosClientes = clientesDias
    GROUP BY clientesDias
)
-- Em média, quantas aulas esses alunos assistiram?
SELECT 
    avg(qtde_dias)
FROM join_alunos_desde_primeiro
