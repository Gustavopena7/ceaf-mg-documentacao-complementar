# Histórico das versões

## 1.1.3 · 22 de novembro de 2026

O Quadro A.4 e a memória reúnem doze cenários. O S04 foi retirado porque o corte de 2025 aplicado às compras da Biolab era um parâmetro de simulação, sem ato citado que datasse naquele ano a autorização da embalagem das apresentações. Os demais cenários conservam seus códigos. A classificação P1+P2 continua baseada nas etapas registradas pela Anvisa para as apresentações adquiridas.

### Conciliações dos Apêndices A e C

| Data | Registro da alteração |
| --- | --- |
| 30/10/2026 | Revisão das rotas industriais após a consulta inicial ao cadastro de medicamentos da Anvisa em 07/08/2026. As datas das bulas e dos atos de pós-registro situam as autorizações em relação às compras. |
| 31/10, 09/11 e 10/11/2026 | A versão anterior da base do CEAF utilizada na conferência da matriz CEAF–NCM reunia os dados de 31/10. As notas foram atualizadas em 09 e 10/11. A extração do Comex Stat utilizada na matriz é a de 03/09/2026, para 2014–2025. |
| 16/11/2026 | A conciliação das classes industriais levou cinco itens a P5. A base consolidada reúne 105 itens P1 e 184 P2. Os cálculos estão em `Consolidacao_16nov` e as fontes sanitárias por item, em `Vigencia_10nov`, na planilha suplementar. S05 foi calculado antes dessa conciliação. A estimativa usou a AFE mais antiga do grupo no município e abrangeu 173 itens, com R$ 11,82 milhões (0,30%). |
| 21/11/2026 | A conferência do CNPJ completo do estabelecimento favorecido alcançou 228 itens, dos quais 97 foram vinculados a estabelecimentos mineiros. A aba `Conciliacao_CNPJ_21nov` registra o fundamento de cada correção. A Tabela C.1 incorpora essa localização. A conferência da Tabela C.2 confirmou as contagens e os valores nominais da base conciliada. |
| 22/11/2026 | A consulta por apresentação confirmou a embalagem primária e secundária em Pouso Alegre nos 17 itens de gabapentina da Biolab, dos quais onze são programáticos. O controle do arquivo utilizado nos Capítulos 7 e 8 consta da aba `Controle_de_versoes` e do [manifesto da versão 1.1.3](versoes/1.1.3/manifesto.json). |

### Localização das conferências

- **Enquadramento administrativo (A.2).** A classificação histórica da responsabilidade pela aquisição, identificada no Quadro A.1, contém a aba `Camada_881`. Quando o campo `Grupo histórico proposto` está preenchido para o ID do item, ele prevalece sobre `Grupo_declarado_no_ano` nos Gráficos 4.1, 4.5 e 4.6.
- **Execução financeira (A.3).** As abas `Itens_desistentes` e `Concilia_4_processos` da planilha suplementar identificam os seis itens com desistência documentada. A aba `Sensibilidade_desistencias` registra o efeito da retirada desses casos. Na conciliação fiscal, a exclusão de R$ 614.154,76 atribuídos a oito registros duplicados elevou o resíduo nominal de R$ 0,04 para R$ 614.154,80.
- **Matrizes territoriais e comerciais (Tabelas C.1 e C.2).** O campo `Classificacao_P_final` da base de aquisições fornece a classe industrial usada na Tabela C.1. As colunas auxiliares P1+P2 da matriz CEAF–NCM conservam classificações anteriores. Na planilha suplementar, `CEAF_Comex` classifica os 178 fármacos, `NCM_detalhe` discrimina 84 associações fármaco–NCM e `Protocolo_fontes` registra as fontes e as regras de agregação.
- **Valor ausente no recorte do Quadro 8.1 (Apêndice C).** A aba `P2_10nov` identifica `C000936` entre os sete itens P2 com a descrição “Embalagem a granel”. O registro integra a contagem e conserva o valor homologado em branco. A soma desse grupo utiliza os outros seis registros.

As abas mencionadas remetem aos arquivos indicados no Quadro A.1 e no [dicionário dos arquivos](versoes/1.1.3/dicionario_de_arquivos.csv). O acesso às planilhas administrativas por item segue as permissões dos arquivos de origem.

## 1.1.2 · 22 de novembro de 2026

A memória adota a classificação final do Capítulo 7, incorpora o histórico sanitário por apresentação e publica a Figura A.3. Os arquivos de controle identificam a base utilizada, a composição da carteira e os treze cenários do Quadro A.4.

## Edições arquivadas

- [Versão 1.1.2 · 22 de novembro de 2026](https://github.com/Gustavopena7/ceaf-mg-documentacao-complementar/tree/81249b848974334eab83adf341dcdb9a1989b5f8)
- [Versão 1.1.1 · 11 de novembro de 2026](https://github.com/Gustavopena7/ceaf-mg-documentacao-complementar/tree/43cc2b098a6c16bf5b8bf4d9042f9d61f28b8cfe)
- [Versão 1.1.0 · 11 de novembro de 2026](https://github.com/Gustavopena7/ceaf-mg-documentacao-complementar/tree/6c4f96b7d5896b5b18e06bb00e7e678560d99447)
- [Versão 1.0.1 · 2 de novembro de 2026](https://github.com/Gustavopena7/ceaf-mg-documentacao-complementar/tree/73fc8c757be502a7ee831e38416d74fdfad1496d)
- [Versão 1.0.0 · 1 de novembro de 2026](https://github.com/Gustavopena7/ceaf-mg-documentacao-complementar/tree/f3116ff39b716a605b89f9d5d9bae506c41dd634)
