-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Quantos clientes SQL chegaram até o 5° dia?

-- o raciocínio foi encontrar primeiramente quais eram os clientes do 1° dia. Consulta 1. Depois com essa informação já filtrada, quem deles continuaram até o 5° dia

With ClientesPrimeiroDia AS (
    SELECT
        DISTINCT IdCliente
    FROM transacoes
    WHERE substr(DtCriacao,1,10) = '2025-08-25'
)
SELECT
    COUNT(DISTINCT t2.IdCliente)
FROM transacoes t2
JOIN ClientesPrimeiroDia cp ON cp.IdCliente = t2.IdCliente
WHERE substr(DtCriacao,1,10) = '2025-08-29'

