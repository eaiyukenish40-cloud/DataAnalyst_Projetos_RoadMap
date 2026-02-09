-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Dentre os clientes de Jan/25 quantos assistiram o curso SQL?

-- seleciona os clientes que participaram do curso em janeiro de 2025
WITH clienteJan AS (
    SELECT
        DISTINCT IdCliente
    FROM transacoes
    WHERE DtCriacao >= '2025-01-01' AND DtCriacao < '2025-02-01' 
)

SELECT
    COUNT(DISTINCT cj.IdCliente) AS quantidadeClientesJAN,
    COUNT(DISTINCT t.IdCliente) AS quantidadeClientesCurso,
    100.* COUNT(DISTINCT t.IdCliente)/COUNT(DISTINCT cj.IdCliente) AS PercentualParticipacaoCursoBaseJan
FROM clienteJan cj
LEFT JOIN transacoes t ON t.IdCliente = cj.IdCliente AND t.DtCriacao >= '2025-08-25' AND t.DtCriacao < '2025-08-30'


-- WHERE t.DtCriacao >= '2025-08-25' AND t.DtCriacao < '2025-08-30' 



-- período do curso
-- Esta query está errada, pois ela primeiro faz o join por meio do ID, e depois filtra pro período no where. Excluíndo os valores null de data (linhas) onde não houve a correspondencia de IDs que não participaram do curso. Assim, para corrigir isso, devemos colocar a condição de data no ON do JOIN, para que ele já faça o filtro de participação no curso durante o processo de junção, e não depois. Assim, ele irá contar os clientes que participaram do curso dentro do período estipulado, mesmo que eles não tenham participado do curso em janeiro.