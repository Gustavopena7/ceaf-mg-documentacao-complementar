# Documentação complementar CEAF–MG — versão 1.1.0

Atualização de 11 de novembro de 2026. Acrescenta as versões compactas da matriz de 37 estabelecimentos e do catálogo de 49 evidências, a equivalência entre nomes descritivos e identificadores dos arquivos e duas conferências quantitativas da base conciliada de 9.585 itens. Os arquivos da versão 1.0.1 permanecem no histórico e na raiz como documentação da versão anterior.

## Conteúdo

- `matriz_estabelecimentos_resumida.csv`: matriz B.1 incorporada ao apêndice; a hierarquia A/B/C corresponde ao lastro das fontes, não à intensidade tecnológica. As incertezas permanecem expressas.
- `catalogo_evidencias_resumido.csv`: Quadro D.2 com identificador, objeto e chamada autor-data.
- `catalogo_evidencias_completo.json`: catálogo com descrições e identificadores preservados; chamadas Brasil (2025a) conciliadas com as Referências.
- `referencias_da_monografia.txt`: referências da versão examinada, para localizar as chamadas do catálogo.
- `contagem_unidades.csv`: agrupamento dos 9.585 itens por unidade de compra.
- `rotas_nacionais_e_multiplanta.csv`: valores por classificação P, com denominador exclusivamente formado pelas origens NACIONAL e MULTIPLANTA.
- `dicionario_de_arquivos.csv` e `manifesto.json`: localização dos arquivos de apoio, nomes originais, checksum da base e limites de reprodução.

## Alcance do depósito

O depósito contém documentação e agregados. Os arquivos administrativos individualizados e os denominadores originais do rateio não estão integralmente neste pacote. Os arquivos de apoio no Drive dependem das permissões de acesso. A versão identificada pelo commit fixa o conteúdo deste depósito, mas não fixa os arquivos externos: a identidade da base é conferida pelo checksum do manifesto.

As consultas regulatórias sustentam rotas documentadas. Não demonstram, por si, operação em cada ano de compra ou a origem do lote entregue. A base individualiza plantas mineiras, mas não a UF de todas as plantas nacionais; por isso não é apresentada uma distribuição completa por UF.

## Reprodução dos dois agregados

O script `reproduzir_agregados.py` lê a aba Dados da base conciliada, valida IDs únicos e calcula as duas tabelas. A soma monetária usa os valores armazenados, preservando casas decimais; o arredondamento é feito apenas na apresentação. As tabelas não reclassificam registros.
