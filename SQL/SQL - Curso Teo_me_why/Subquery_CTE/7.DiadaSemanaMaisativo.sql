-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Qual o dia da semana mais ativo de cada usuário?

WITH diadaSemana AS (
    SELECT
        IdCliente,
        strftime('%w', DtCriacao) as DiaSemana,
        COUNT(DISTINCT IdTransacao) as numTransacoes
    FROM transacoes
    GROUP BY IdCliente, DiaSemana
)
SELECT
    IdCliente,
    MAX(numTransacoes) as MaxTransacoes,
    CASE 
        WHEN DiaSemana = '0' THEN 'Domingo'
        WHEN DiaSemana = '1' THEN 'Segunda-feira'
        WHEN DiaSemana = '2' THEN 'Terça-feira'
        WHEN DiaSemana = '3' THEN 'Quarta-feira'
        WHEN DiaSemana = '4' THEN 'Quinta-feira'
        WHEN DiaSemana = '5' THEN 'Sexta-feira'
        WHEN '6' THEN 'Sábado'
    END as Dia
FROM diadaSemana
GROUP BY IdCliente
ORDER BY MaxTransacoes DESC