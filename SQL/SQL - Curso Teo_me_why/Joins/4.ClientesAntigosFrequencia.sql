-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Clientes antigos tem mais frequencia de transação?

SELECT
    COUNT(DISTINCT t.IdTransacao) AS QtdeTransacao,
    t.IdCliente,
    CAST(julianday('now') - julianday(substr(c.DtCriacao,1,19)) AS INT) AS DiasDesdeCadastro
FROM transacoes t
LEFT JOIN clientes c ON c.IdCliente = t.IdCliente
GROUP BY t.IdCliente, DiasDesdeCadastro
ORDER BY DiasDesdeCadastro DESC, QtdeTransacao DESC


