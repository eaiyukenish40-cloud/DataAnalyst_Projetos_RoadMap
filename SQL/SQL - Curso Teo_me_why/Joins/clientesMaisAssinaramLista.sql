-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto
WITH joins AS(
    SELECT 
        t.IdCliente,
        (t.DtCriacao,1,10)
    FROM transacoes t
    LEFT JOIN transacao_produto tp ON t.IdTransacao = tp.IdTransacao
    LEFT JOIN produtos p ON p.IdProduto = tp.IdProduto
    WHERE DescNomeProduto = 'Lista de presença' AND substr(DtCriacao,1,10) = '2025-08-29'
)
SELECT*
FROM joins