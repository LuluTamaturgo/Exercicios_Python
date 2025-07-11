tabela fnde_data_programa_QUOTA
Esta tabela registra o histórico de repasses do FNDE relativos à Quota Salário‑Educação (QUOTA) — transferência constitucional que complementa o financiamento da educação básica.
Cada linha corresponde a uma ordem bancária creditada a um município em um determinado exercício (ano) e parcela. O repositório é usado para:

monitorar a pontualidade e o valor dos repasses;

consolidar montantes por UF, município ou período;

cruzar informações com prestações de contas, execução orçamentária e indicadores educacionais.

| Coluna             | Tipo / Restrições                            | Descrição funcional                                                                                                                         |
| ------------------ | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`               | **bigint** • PK • auto\_increment • NOT NULL | Identificador técnico exclusivo da linha (surrogate key). Facilita integrações internas sem depender de códigos externos.                   |
| `ano`              | **int** • NOT NULL                           | Exercício financeiro a que a ordem bancária se refere (ex.: 2025). Permite análises comparativas ano a ano.                                 |
| `uf`               | **varchar(2)** • NOT NULL                    | Unidade federativa (sigla IBGE, ex.: “BA”). Essencial para agrupamentos regionais e geração de mapas temáticos.                             |
| `municipio_codigo` | **varchar(20)** • NOT NULL                   | Código IBGE do município beneficiário. Funciona como chave de integração com cadastros territoriais e com outras tabelas FNDE.              |
| `municipio_nome`   | **varchar(200)** • NOT NULL                  | Nome oficial do município (ex.: “Salvador”). Mantém redundância para consultas rápidas e relatórios sem necessidade de junções.             |
| `data_pagamento`   | **date** • NOT NULL                          | Data em que o FNDE liquidou a ordem bancária. Útil para auditar prazos entre cronograma previsto e execução efetiva.                        |
| `ordem_bancaria`   | **varchar(100)** • NOT NULL                  | Número/código da ordem bancária gerada pelo SIAFI. Serve para conciliação com extratos e comprovantes.                                      |
| `valor`            | **decimal(15,2)** • NOT NULL                 | Montante creditado em reais (R\$). Precisão de 2 casas decimais; base para indicadores de investimento per capita.                          |
| `parcela`          | **varchar(50)** • NOT NULL                   | Identificador da parcela dentro do exercício (ex.: “Quota Única”, “1ª Parcela”). Possibilita verificar calendário de liberações.            |
| `programa`         | **varchar(100)** • NOT NULL                  | Nome do programa. Embora nesta tabela tipicamente “QUOTA”, deixa‑se genérico para manter compatibilidade com cargas automatizadas.          |
| `banco`            | **varchar(100)** • NOT NULL                  | Banco de destino (ex.: “Banco do Brasil”). Importante para processos de conciliação bancária.                                               |
| `agencia`          | **varchar(100)** • NOT NULL                  | Agência onde a conta está registrada. Ajuda a identificar divergências cadastrais.                                                          |
| `conta_corrente`   | **varchar(100)** • NOT NULL                  | Número da conta corrente beneficiária. Fundamental em auditorias antifraude e no rastreio de estornos.                                      |
| `data_extracao`    | **datetime(6)** • NOT NULL                   | Timestamp de quando a linha foi extraída do sistema‑fonte (até microssegundos). Suporte a controles de versionamento e cargas incrementais. |

### Índices
- Index em (`id`,`ano`,`uf`,`municipio_codigo`,`municipio_nome`,`data_pagamento`,`ordem_bancaria`,`valor`,`parcela`,`programa`,`banco`,`agencia`,`conta_corrente`,
`data_extracao`) conforme definido em `Meta.indexes`.