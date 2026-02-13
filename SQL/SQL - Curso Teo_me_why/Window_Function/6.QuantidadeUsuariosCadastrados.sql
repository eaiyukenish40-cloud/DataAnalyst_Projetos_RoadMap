-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Quantidade de usuários cadastrados (absoluto e acumulado) ao longo do tempo?

WITH usuarios_cadastrados AS (
    SELECT
        substr(DtCriacao,1,7) AS DtMes,
        COUNT(DISTINCT idCliente) AS qtdeUsuariosCadastrados
    FROM clientes

    GROUP BY DtMes
    ORDER BY DtMes
)
SELECT
    DtMes,
    qtdeUsuariosCadastrados,
    SUM(qtdeUsuariosCadastrados) OVER(ORDER BY DtMes) AS qtdeUsuariosCadastradosAcumulados
FROM usuarios_cadastrados