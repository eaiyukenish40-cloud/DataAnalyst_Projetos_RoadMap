-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Dia do cliente com mais interações (considerando aqueles que participaram desde o 1° dia de aula)

WITH primeiroDia AS (
    SELECT 
        DISTINCT IdCliente AS primeirosClientes,
        substr(DtCriacao,1,10)
    FROM transacoes
    WHERE substr(DtCriacao,1,10) = '2025-08-25'
),

-- Quais alunos assistiram aulas em cada dia
diasCurso AS (
    SELECT DISTINCT
        primeirosClientes,
        substr(DtCriacao,1,10) AS presenca_dia,
        COUNT(*) AS quantidadeAssistida
    FROM primeiroDia pd

    JOIN transacoes t ON t.IdCliente = primeirosClientes
    AND substr(DtCriacao,1,10) >= '2025-08-25' AND substr(DtCriacao,1,10) < '2025-08-30'
    GROUP BY primeirosClientes, presenca_dia
    ORDER BY primeirosClientes, presenca_dia
),
ranking AS (
    SELECT 
        *,
        row_number() OVER(PARTITION BY primeirosClientes ORDER BY quantidadeAssistida DESC) AS ordenacao
    FROM diasCurso
)
SELECT*
FROM ranking
WHERE ordenacao = 1
