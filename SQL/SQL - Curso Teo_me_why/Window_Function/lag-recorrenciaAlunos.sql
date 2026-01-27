-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

WITH ClienteDia AS(
    SELECT
        IdCliente,
        substr(DtCriacao,1,10) AS dtDia
    FROM transacoes

    WHERE substr(DtCriacao,1,4) = '2025'

    ORDER BY IdCliente, dtDia
),
diaLag AS(
    SELECT
        *,
        LAG(dtDia) OVER(PARTITION BY IdCliente ORDER BY dtDia) AS lagDia

    FROM ClienteDia
),
diferencaDia AS(
    SELECT *,
        julianday(dtDia) - julianday(lagDia) AS recorrencia
    FROM diaLag
    
)
SELECT IdCliente, 
    AVG(recorrencia)
FROM diferencaDia
GROUP BY  IdCliente