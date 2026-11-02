# CEAF/SES-MG: documentação complementar da monografia

Este conjunto reúne documentação complementar da pesquisa de Luiz Gustavo de Carvalho Pena, desenvolvida no curso de Administração Pública da Fundação João Pinheiro, sobre a correspondência entre a demanda do CEAF/SES-MG e as capacidades farmacêuticas localizadas em Minas Gerais.

**Data da extração:** 1 de novembro de 2026.  
**Versão documental:** 1.0.1 (atualizada em 2 de novembro de 2026).  
**Escopo:** Quadros A.4, B.1 e D.2, acompanhados das notas de interpretação e das referências.

## Conteúdo

| Material | Conteúdo | Leitura | Dados estruturados |
| --- | --- | --- | --- |
| Quadro A.4 | 25 procedimentos, organizados em quatro grupos | [Procedimentos de reprodução](A4_procedimentos.md) | [JSON](A4_procedimentos.json) |
| Quadro B.1 | 37 estabelecimentos do universo regulatório, com função e habilitação sanitária | [Matriz de estabelecimentos](B1_estabelecimentos.md) | [JSON](B1_estabelecimentos.json) |
| Quadro D.2 | 49 evidências científicas, tecnológicas e institucionais, identificadas de E01 a E49 | [Catálogo de evidências](D2_evidencias_cti.md) | [JSON](D2_evidencias_cti.json) |

A [atualização documental 1.0.1](ATUALIZACAO_1.0.1.md), as [notas sobre o alcance do levantamento de CT&I](alcance_cti.md) e a [lista de referências da monografia](referencias.md) complementam a leitura.

## Como utilizar

Os arquivos Markdown permitem consultar os quadros diretamente no GitHub. Os arquivos JSON preservam os mesmos campos para leitura por programas. No Quadro A.4, as quatro linhas de agrupamento permanecem registradas no JSON, além dos 25 procedimentos.

Foram preservados os textos, os identificadores e as remissões da monografia. As referências a capítulos, seções e outros apêndices devem ser lidas conforme a numeração do trabalho. As datas de extração deste pacote são distintas das datas de consulta e de vigência das fontes.

O material permite conferir os procedimentos descritos e as evidências catalogadas. A reprodução dos resultados quantitativos também depende das planilhas de compras, das bases auxiliares e das memórias de cálculo indicadas na monografia, que não integram este pacote inicial. Na incorporação futura dessas bases, deve ser preservada a revisão de 50 itens utilizada nos resultados finais, com identificação das alterações por ID.

## Versão correspondente à monografia

A versão documental 1.0.1 complementa os três quadros extraídos em 1 de novembro de 2026 com referências e ressalvas temporais de 2 de novembro. A versão 1.0.0 permanece no commit f3116ff39b716a605b89f9d5d9bae506c41dd634. A referência inserida no apêndice deve indicar a versão e o registro correspondente no histórico do repositório. Atualizações posteriores devem ser identificadas separadamente, permitindo consultar o material utilizado na monografia.

O arquivo [SHA256SUMS.txt](SHA256SUMS.txt) registra os resumos digitais dos arquivos deste pacote para conferência de integridade.
